from langchain_openai import AzureChatOpenAI
from crllm.model.model import Model


class AzureModel(Model):
    def _getModel(self, model_config):
        return AzureChatOpenAI(**model_config)
