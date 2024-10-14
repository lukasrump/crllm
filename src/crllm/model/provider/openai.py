from langchain_openai import ChatOpenAI
from crllm.model.model import Model


class OpenAIModel(Model):
    def _get_model(self, model_config):
        return ChatOpenAI(**model_config)

    @staticmethod
    def get_required_config():
        return ["model"]
