import toml
from crllm.init_project import init_project


def test_init(tmpdir, monkeypatch):
    file_path = tmpdir.mkdir("test")

    def answer():
        yield {"provider": "ollama", "loader": "file"}
        yield {"model": "llama3"}

    gen = answer()
    monkeypatch.setattr("inquirer.prompt", lambda x: next(gen))

    init_project(str(file_path))

    config_file = toml.load(file_path.join("crllm_config.toml"))

    assert config_file["crllm"]["provider"] == "ollama"
    assert config_file["crllm"]["loader"] == "file"
    assert config_file["model"]["model"] == "llama3"
