from langchain_ollama import ChatOllama
from crllm.model.model import Model


class OllamaModel(Model):
    def _get_model(self, model_config):
        return ChatOllama(**model_config)

    @staticmethod
    def get_required_config():
        return ["model"]
