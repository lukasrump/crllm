from crllm.code import code_loader
from crllm.code.loaders.file import file
from crllm.code.loaders.git_compare import git_compare
from crllm.code.loaders.git import git

loaders = {"git": git, "git_compare": git_compare, "file": file}
