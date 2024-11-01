from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from crllm.model.model import Model


class OpenAIModel(Model):
    def _get_model(self, model_config):
        return ChatOpenAI(**model_config)

    def _get_embeddings(self, embeddings_config):
        return OpenAIEmbeddings(**embeddings_config)

    @staticmethod
    def get_required_config():
        return ["model"]
