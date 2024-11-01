from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFaceEndpoint,
    HuggingFaceEmbeddings,
)
from crllm.model.model import Model


class HuggingFaceModel(Model):
    def _get_model(self, model_config):
        llm = HuggingFaceEndpoint(**model_config)

        return ChatHuggingFace(llm=llm)

    def _get_embeddings(self, embeddings_config):
        return HuggingFaceEmbeddings(**embeddings_config)

    @staticmethod
    def get_required_config():
        return ["repo_id", "task"]
