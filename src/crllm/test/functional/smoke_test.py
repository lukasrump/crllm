import sys
from crllm.cli import cli
from crllm.code.loaders.file import file


def test_cli(monkeypatch, capfd, tmpdir):

    file_path = "./src/crllm/test/functional/smoke_test.py"
    config_path = "./src/crllm/test/functional/config.toml"
    output_path = str(tmpdir.join("output.md"))

    monkeypatch.setattr(
        sys, "argv", ["crllm", file_path, "-c", config_path, "-o", output_path]
    )
    cli()
    out, err = capfd.readouterr()

    assert not err
    assert "This is a dry run!" in out
    assert file(output_path) == "This is a dry run!"
