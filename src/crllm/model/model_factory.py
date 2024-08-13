from crllm.config.config_service import config_service
from crllm.model.model import Model
from crllm.model.provider import providers


class ModelFactory:
    def getModel(self) -> Model:
        config = config_service.getConfig()
        provider = config["crllm"]["provider"]

        return providers[provider]()
