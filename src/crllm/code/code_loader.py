import logging
from crllm.code import loaders
from crllm.config.config_service import config_service


class CodeLoader:
    def __init__(self) -> None:
        self.loaders = {}

    def getCode(self, path):
        config = config_service.getConfig()

        loaderName = config["crllm"]["loader"]

        result = loaders.loaders[loaderName](path)
        logging.debug(result)
        return result


loader = CodeLoader()
