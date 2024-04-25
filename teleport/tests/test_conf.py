import os
import pytest
from unittest import mock
from datadog_checks.dev import docker_run, get_docker_hostname, get_here
from datadog_checks.teleport import TeleportCheck

URL = 'http://{}:3000/metrics'.format(get_docker_hostname())
INSTANCE = {'url': URL,}

@pytest.fixture(scope="session")
def dd_environment():
    compose_file = os.path.join(get_here(), 'docker-compose.yml')
    with docker_run(compose_file, endpoints=[URL]):
        yield INSTANCE

@pytest.fixture
def instance():
    return INSTANCE.copy()

@pytest.fixture
def check(instance):
    return TeleportCheck("teleport", {}, [instance])

@pytest.mark.integration
@pytest.mark.usefixtures('dd_environment')
def test_prometheus_metrics():
    fixture_file = os.path.join(os.path.dirname(__file__), "fixtures", "metrics.txt")

    with open(fixture_file, "r") as f:
        content = f.read()

    with mock.patch(
        "requests.get",
        return_value=mock.MagicMock(
            status_code=200,
            iter_lines=lambda **kwargs: content.split("\n"),
            headers={"Content-Type": "text/plain"},
        ),
    ):
        return