import logging
from langchain_core.prompts import ChatPromptTemplate
from crllm.config.config_service import config_service


class PromptBuilder:
    def build(self):
        config = config_service.get_config()

        logging.debug(config["prompt"])

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", config["prompt"]["template"]),
                (
                    "system",
                    """
This code could be relevant to understand the changes:
<context>
    {context}
</context>
                 """,
                ),
                ("human", "Do code review for the following code changes: \n {code}"),
            ]
        )

        return prompt
