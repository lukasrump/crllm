from abc import ABC, abstractmethod
import logging
import os
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_community.vectorstores import FAISS


from crllm.config.config_service import config_service


class Model(ABC):
    def generate(self, prompt_template, prompt_args):
        config = config_service.get_config()
        model_config = config["model"]
        rag_config = config["rag"]

        model = self._get_model(model_config)

        chain = prompt_template | model

        if config["rag"]["enabled"]:
            self.add_rag_context(prompt_args, rag_config)

            logging.debug(
                prompt_template.format(
                    context=prompt_args["context"], code=prompt_args["code"]
                )
            )

        result = chain.invoke(prompt_args)

        logging.debug(result)
        logging.info(result.usage_metadata)

        return result.content

    def add_rag_context(self, prompt_args, rag_config):
        vectorstore = self._get_vector_store(rag_config)

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        prompt_args["context"] = format_docs(
            vectorstore.similarity_search(prompt_args["code"], 3)
        )

    def _get_vector_store(self, rag_config):
        embedding_config = {"model": rag_config["embedding_model"]}

        if rag_config["cache_enabled"]:
            if os.path.exists(rag_config["cache_path"]):
                vectorstore = FAISS.load_local(
                    rag_config["cache_path"],
                    embeddings=self._get_embeddings(embedding_config),
                    allow_dangerous_deserialization=True,
                )
                return vectorstore

        loader = GenericLoader.from_filesystem(
            path=rag_config["src_path"],
            glob=rag_config["src_glob"],
            parser=LanguageParser(),
            show_progress=True,
        )

        docs = loader.load()

        vectorstore = FAISS.from_documents(
            documents=docs, embedding=self._get_embeddings(embedding_config)
        )

        if rag_config["cache_enabled"]:
            os.makedirs(os.path.dirname(rag_config["cache_path"]), exist_ok=True)
            vectorstore.save_local(rag_config["cache_path"])

        return vectorstore

    @abstractmethod
    def _get_model(self, model_config):
        pass

    @abstractmethod
    def _get_embeddings(self, embeddings_config):
        pass

    @staticmethod
    def get_required_config():
        return []
