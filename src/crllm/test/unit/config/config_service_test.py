import pytest
from crllm.config.config_service import ConfigService


@pytest.fixture()
def mock_config_file(tmpdir):
    tmpdir.join("config.toml").write(
        """
    [crllm]
        loader = "foo"
        provider = "bar"
    """
    )

    return str(tmpdir.join("config.toml"))


def test_get_config(mock_config_file):
    config_service = ConfigService()
    config_service.set_config_path(mock_config_file)

    result = config_service.get_config()

    assert result["crllm"]["loader"] == "foo"
    assert result["crllm"]["provider"] == "bar"


def test_override(mock_config_file):
    config_service = ConfigService()
    config_service.set_config_path(mock_config_file)

    config_service.override_config({"crllm": {"loader": "test"}})

    result = config_service.get_config()

    assert result["crllm"]["loader"] == "test"
