import logging
from rich.console import Console
from rich.markdown import Markdown
from crllm.config.config_service import config_service
from crllm.code import code_loader
from crllm.model.model_factory import ModelFactory
from crllm.prompt_builder import PromptBuilder


def app(path: str):
    logging.info("Reading %s", path)

    code = code_loader.loader.get_code(path)

    prompt_builder = PromptBuilder()
    prompt = prompt_builder.build()

    model_factory = ModelFactory()

    model = model_factory.get_model()

    result = model.generate(prompt, {"code": code})

    markdown = Markdown(result)

    config = config_service.get_config()

    if config["crllm"]["output"] != "":
        with open(config["crllm"]["output"], "w", encoding="utf8") as file:
            file.write(str(result))

    console = Console()
    console.print(markdown)
