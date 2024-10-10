import logging
from crllm.code import loaders
from crllm.config.config_service import config_service


class CodeLoader:
    def __init__(self) -> None:
        self.loaders = {}

    def get_code(self, path):
        config = config_service.get_config()

        loader_name = config["crllm"]["loader"]

        result = loaders.loaders[loader_name](path)
        logging.debug(result)
        return result


loader = CodeLoader()
