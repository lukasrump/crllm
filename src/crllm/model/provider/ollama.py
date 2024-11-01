import os
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
from crllm.model.model import Model


class OllamaModel(Model):
    def _get_model(self, model_config):
        if os.environ.get("OLLAMA_URL"):
            model_config["base_url"] = os.environ.get("OLLAMA_URL")

        return ChatOllama(**model_config)

    def _get_embeddings(self, embeddings_config):
        return OllamaEmbeddings(**embeddings_config)

    @staticmethod
    def get_required_config():
        return ["model"]
