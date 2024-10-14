import logging
import os
import toml
import inquirer
from crllm.code.loaders import loaders
from crllm.model.provider import providers


def init_project(path: str):
    if os.path.isfile(os.path.join(path, "crllm_config.toml")):
        logging.error("Config file already exists")
        return

    logging.info("Initializing project in %s", path)

    questions = [
        inquirer.List(
            "provider",
            message="Choose provider",
            choices=providers.keys(),
        ),
        inquirer.List("loader", message="Choose loader", choices=loaders.keys()),
    ]

    answers = inquirer.prompt(questions)

    model = providers[answers["provider"]]()

    model_config = model.get_required_config()

    model_questions = [
        inquirer.Text(key, message=f"Enter {key}") for key in model_config
    ]

    model_answers = inquirer.prompt(model_questions)

    config = {
        "crllm": {
            "provider": answers["provider"],
            "loader": answers["loader"],
        },
        "model": model_answers,
    }

    with open(os.path.join(path, "crllm_config.toml"), "w", encoding="utf8") as file:
        toml.dump(config, file)

    logging.info("Finished.")
