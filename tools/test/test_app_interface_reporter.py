from tools.app_interface_reporter import prometheus_metrics_to_job_history
from reconcile.test.fixtures import Fixtures

# fxf = Fixtures('app_interface_reporter')
class TestAppInterfaceReporter:
    @staticmethod
    def testPrometheusMetricsToJobHistory():
        # metrics = fxf.get_anymarkup('metrics.yml')
        metrics = []
        prometheus_metrics_to_job_history(metrics, 'cluster-name')
