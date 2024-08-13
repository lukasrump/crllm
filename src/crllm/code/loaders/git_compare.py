from git import Repo
from crllm.config.config_service import config_service


def git_compare(path):
    repo = Repo(path)

    current_branch = repo.active_branch.name
    config = config_service.getConfig()
    main_branch = config["crllm"]["git_main_branch"]

    diff = repo.git.diff(f"{main_branch}...{current_branch}", unified=0)

    code = ""

    for line in diff.splitlines():
        code += line + "\n"

    return code
