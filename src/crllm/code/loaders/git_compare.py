from git import Repo
from crllm.code.loaders.ignore_utils import should_ignore_file
from crllm.config.config_service import config_service


def git_compare(path):
    repo = Repo(path)

    current_branch = repo.active_branch.name
    config = config_service.get_config()
    main_branch = config["crllm"]["git_main_branch"]

    diff = repo.git.diff(f"{main_branch}...{current_branch}")

    code = ""

    for line in diff.splitlines():
        if "b/" in line:
            file = line.split("b/")[1]
            full_file_path = f"{path}/{file}"

            if should_ignore_file(full_file_path, path):
                continue

            code += "\nFile name: " + file + "\n"

        code += line + "\n"

    return code
