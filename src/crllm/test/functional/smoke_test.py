import sys
from crllm.cli import cli


def test_cli(monkeypatch, capfd):

    file_path = "./src/crllm/test/functional/smoke_test.py"
    config_path = "./src/crllm/test/functional/config.toml"

    monkeypatch.setattr(sys, "argv", ["crllm", file_path, "-c", config_path])
    cli()
    out, err = capfd.readouterr()

    assert not err
    assert "This is a dry run!" in out
