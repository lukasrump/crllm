from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from crllm.model.model import Model


class HuggingFaceModel(Model):
    def _get_model(self, model_config):
        llm = HuggingFaceEndpoint(**model_config)

        return ChatHuggingFace(llm=llm)
