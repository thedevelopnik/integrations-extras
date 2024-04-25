from datadog_checks.base import OpenMetricsBaseCheckV2
from datadog_checks.teleport.config_models import ConfigMixin
from datadog_checks.teleport.metrics import METRIC_MAP


class TeleportCheck(OpenMetricsBaseCheckV2, ConfigMixin):
    __NAMESPACE__ = "teleport"

    DEFAULT_METRIC_LIMIT = 0

    def get_default_config(self):
        return {"metrics": [METRIC_MAP]}