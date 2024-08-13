import logging
from rich.console import Console
from rich.markdown import Markdown
from crllm.code import code_loader
from crllm.model.model_factory import ModelFactory
from crllm.prompt_builder import PromptBuilder


def app(path: str):
    logging.info("Reading %s", path)

    code = code_loader.loader.getCode(path)

    promptBuilder = PromptBuilder()
    prompt = promptBuilder.build()

    modelFactory = ModelFactory()

    model = modelFactory.getModel()

    result = model.generate(prompt, {"code": code})

    md = Markdown(result)

    console = Console()
    console.print(md)
