from abc import ABC, abstractmethod
import logging
from crllm.config.config_service import config_service


class Model(ABC):
    def generate(self, prompt_template, prompt_args):
        config = config_service.get_config()
        model_config = config["model"]

        model = self._get_model(model_config)

        llm_chain = prompt_template | model
        result = llm_chain.invoke(prompt_args)

        logging.debug(result)

        return result.content

    @abstractmethod
    def _get_model(self, model_config):
        pass

    @staticmethod
    def get_required_config():
        return []
