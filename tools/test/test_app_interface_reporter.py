from tools.app_interface_reporter import prometheus_metrics_to_job_history
from  .fixtures.app_interface_reporter.fixture import *

class TestAppInterfaceReporter:
    @staticmethod
    def testPrometheusMetricsToJobHistory(metrics):
        # expected_job_history = fxf.get_anymarkup('expected_job_history.yml')

        job_history = prometheus_metrics_to_job_history(metrics, 'cluster-name')
