from crllm.model.provider.azure import AzureModel
from crllm.model.provider.dryrun import DryRunModel
from crllm.model.provider.ollama import OllamaModel
from crllm.model.provider.huggingface import HuggingFaceModel
from crllm.model.provider.openai import OpenAIModel


providers = {
    "ollama": OllamaModel,
    "azure": AzureModel,
    "huggingface": HuggingFaceModel,
    "openai": OpenAIModel,
    "dryrun": DryRunModel,
}
