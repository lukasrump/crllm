import logging
import os
from deepmerge import always_merger
import toml

from crllm.config import CONFIG_DIR


class ConfigService:
    configPath = os.path.join(CONFIG_DIR, "config.toml")
    config = None

    def get_config(self, path="./crllm_config.toml"):
        if self.config:
            return self.config

        self.config = toml.load(self.configPath)

        if not os.path.isfile(path):
            return self.config

        project_config = toml.load(path)
        self.config = always_merger.merge(self.config, project_config)

        logging.debug(self.config)

        return self.config


config_service = ConfigService()
