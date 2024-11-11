import logging
from git import Repo
from crllm.code.loaders.ignore_utils import should_ignore_file
from crllm.code.loaders.exceptions.no_code_found import NoCodeFoundException
from crllm.config.config_service import config_service


def git(path):
    config = config_service.get_config()
    use_changed_lines = config["crllm"]["git_changed_lines"]

    repo = Repo(path)
    diff = repo.index.diff(None, create_patch=True)

    if len(diff) == 0:
        raise NoCodeFoundException("No changed files found!")

    code = ""

    if not use_changed_lines:
        changed_files = [item.a_path for item in diff if item.a_path is not None]

        logging.info("Found changed files: %s", changed_files)

        for file in changed_files:
            full_file_path = f"{path}/{file}"

            if should_ignore_file(full_file_path, path):
                continue

            with open(file, encoding="UTF8") as file:
                code += "\nFile name: " + str(file) + "\n"
                code += file.read()
    else:
        for line in diff:
            full_file_path = f"{path}/{line.a_path}"

            if should_ignore_file(full_file_path, path):
                continue

            code += str(line) + "\n"

    return code
