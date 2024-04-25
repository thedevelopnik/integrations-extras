from typing import Any, Callable, Dict  # noqa: F401
import pytest
from datadog_checks.base import AgentCheck  # noqa: F401
from datadog_checks.base.stubs.aggregator import AggregatorStub  # noqa: F401
from datadog_checks.dev.utils import get_metadata_metrics
from datadog_checks.teleport import TeleportCheck

EXPECTED_METRICS = {
    "teleport.audit.failed_disk_monitoring.count",
    "teleport.audit.emit.events.count",
    "teleport.audit.failed_emit_events.count",
    "teleport.audit.percentage_disk_space_used",
    "teleport.audit.server_open_files",
    "teleport.auth.generate.requests",
    "teleport.auth.generate.seconds.bucket",
    "teleport.auth.generate.seconds.count",
    "teleport.auth.generate.seconds.sum",
    "teleport.backend.batch.read.seconds.bucket",
    "teleport.backend.batch.read.seconds.count",
    "teleport.backend.batch.read.seconds.sum",
    "teleport.backend.batch.write.seconds.bucket",
    "teleport.backend.batch.write.seconds.count",
    "teleport.backend.batch.write.seconds.sum",
    "teleport.backend.read.seconds.bucket",
    "teleport.backend.read.seconds.count",
    "teleport.backend.read.seconds.sum",
    "teleport.backend.requests.count",
    "teleport.backend.write.seconds.bucket",
    "teleport.backend.write.seconds.count",
    "teleport.backend.write.seconds.sum",
    "teleport.migrations",
    "teleport.watcher.event_sizes.bucket",
    "teleport.watcher.event_sizes.count",
    "teleport.watcher.event_sizes.sum",
    "teleport.watcher.events.bucket",
    "teleport.watcher.events.count",
    "teleport.watcher.events.sum",
}

@pytest.mark.unit
def test_mock_assert_prometheus_metrics(dd_run_check, aggregator, check):
    dd_run_check(check)
    for metric_name in EXPECTED_METRICS:
        aggregator.assert_metric(metric_name)
    aggregator.assert_all_metrics_covered()
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())
    aggregator.assert_service_check("teleport.openmetrics.health", status=TeleportCheck.OK)
