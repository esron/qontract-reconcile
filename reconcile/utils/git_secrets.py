import logging
import os
import subprocess
import tempfile

import requests
from sretoolbox.utils import retry

from reconcile.utils import git


@retry()
def scan_history(repo_url, existing_keys):
    logging.info(f"scanning {repo_url}")
    if requests.get(repo_url, timeout=60).status_code == 404:
        logging.info(f"not found {repo_url}")
        return []

    with tempfile.TemporaryDirectory() as wd:
        git.clone(repo_url, wd)
        subprocess.run(["git", "secrets", "--install"], check=False, cwd=wd)
        result = subprocess.run(
            ["git", "secrets", "--scan-history"],
            capture_output=True,
            check=False,
            cwd=wd,
        )
        if result.returncode == 0:
            return []
        logging.info(f"found suspects in {repo_url}")
        suspected_files = get_suspected_files(result.stderr.decode("utf-8"))
        leaked_keys = get_leaked_keys(wd, suspected_files, existing_keys)
        if leaked_keys:
            logging.info(f"found suspected leaked keys: {leaked_keys}")
        return leaked_keys


def get_suspected_files(error):
    suspects = []
    for e in error.split("\n"):
        if not e:
            break
        if e.startswith("warning"):
            continue
        commit_path_split = e.split(" ")[0].split(":")
        commit, path = commit_path_split[0], commit_path_split[1]

        suspects.append((commit, path))
    return set(suspects)


def get_leaked_keys(repo_wd, suspected_files, existing_keys):
    all_leaked_keys = []
    for s in suspected_files:
        commit, file_relative_path = s[0], s[1]
        git.checkout(commit, repo_wd)
        file_path = os.path.join(repo_wd, file_relative_path)
        with open(file_path, encoding="locale") as f:
            content = f.read()
        leaked_keys = [key for key in existing_keys if key in content]
        all_leaked_keys.extend(leaked_keys)

    return all_leaked_keys
