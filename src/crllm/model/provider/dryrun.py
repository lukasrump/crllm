from crllm.model.model import Model


class DryRunModel(Model):
    def _get_model(self, model_config):
        pass

    def _get_embeddings(self, embeddings_config):
        pass

    def generate(self, prompt_template, prompt_args):
        return "This is a dry run!"
