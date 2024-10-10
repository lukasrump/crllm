import logging
from rich.console import Console
from rich.markdown import Markdown
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

    console = Console()
    console.print(markdown)
