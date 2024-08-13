import logging
from langchain_core.prompts import ChatPromptTemplate
from crllm.config.config_service import ConfigService


class PromptBuilder:
    def __init__(self, configService=ConfigService()) -> None:
        self.configService = configService

    def build(self):
        config = self.configService.getConfig()

        logging.debug(config["prompt"])

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", config["prompt"]["template"]),
                ("human", "Do code review for the following code: \n {code}"),
            ]
        )

        return prompt
