from langchain_ollama import ChatOllama
from crllm.model.model import Model


class OllamaModel(Model):
    def _getModel(self, model_config):
        return ChatOllama(**model_config)
