import logging
import os
from deepmerge import always_merger
import toml

from crllm.config import CONFIG_DIR


class ConfigService:
    default_config_path = os.path.join(CONFIG_DIR, "config.toml")
    config_path = "./crllm_config.toml"
    config = None

    def set_config_path(self, path):
        self.config_path = path

    def get_config(self):
        if self.config:
            return self.config

        self.config = toml.load(self.default_config_path)

        if not os.path.isfile(self.config_path):
            return self.config

        project_config = toml.load(self.config_path)
        self.override_config(project_config)

        logging.debug(self.config)

        return self.config

    def override_config(self, config: dict):
        if not self.config:
            self.get_config()

        self.config = always_merger.merge(self.config, config)


config_service = ConfigService()
