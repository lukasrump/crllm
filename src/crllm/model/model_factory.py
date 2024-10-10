from crllm.config.config_service import config_service
from crllm.model.model import Model
from crllm.model.provider import providers


class ModelFactory:
    def get_model(self) -> Model:
        config = config_service.get_config()
        provider = config["crllm"]["provider"]

        return providers[provider]()
