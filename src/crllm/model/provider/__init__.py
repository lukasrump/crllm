from crllm.model.provider.azure import AzureModel
from crllm.model.provider.dryrun import DryRunModel
from crllm.model.provider.ollama import OllamaModel
from crllm.model.provider.huggingface import HuggingFaceModel


providers = {
    "ollama": OllamaModel,
    "azure": AzureModel,
    "huggingface": HuggingFaceModel,
    "dryrun": DryRunModel,
}
