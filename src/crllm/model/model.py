from abc import ABC, abstractmethod
import logging
from crllm.config.config_service import config_service


class Model(ABC):
    def generate(self, promptTemplate, promptArgs):
        config = config_service.getConfig()
        model_config = config["model"]

        model = self._getModel(model_config)

        llm_chain = promptTemplate | model
        result = llm_chain.invoke(promptArgs)

        logging.debug(result)

        return result.content

    @abstractmethod
    def _getModel(self, model_config):
        pass
