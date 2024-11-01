import logging
from langchain_core.prompts import ChatPromptTemplate
from crllm.config.config_service import config_service


class PromptBuilder:
    def build(self):
        config = config_service.get_config()

        logging.debug(config["prompt"])

        messages = [
            ("system", config["prompt"]["template"]),
            ("human", "Do code review for the following code changes: \n {code}"),
        ]

        if config["rag"]["enabled"]:
            self._insert_rag_message(messages)

        return ChatPromptTemplate.from_messages(messages)

    def _insert_rag_message(self, messages):
        messages.insert(
            1,
            (
                "system",
                """
This code could be relevant to understand the changes:
<context>
    {context}
</context>
                    """,
            ),
        )
