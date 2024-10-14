from langchain_openai import AzureChatOpenAI
from crllm.model.model import Model


class AzureModel(Model):
    def _get_model(self, model_config):
        return AzureChatOpenAI(**model_config)

    @staticmethod
    def get_required_config():
        return ["azure_deployment", "api_version"]
