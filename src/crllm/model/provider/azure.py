from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from crllm.model.model import Model


class AzureModel(Model):
    def _get_model(self, model_config):
        return AzureChatOpenAI(**model_config)

    def _get_embeddings(self, embeddings_config):
        return AzureOpenAIEmbeddings(**embeddings_config)

    @staticmethod
    def get_required_config():
        return ["azure_deployment", "api_version"]
