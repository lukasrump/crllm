from crllm.model.model import Model


class DryRunModel(Model):
    def _getModel(self, model_config):
        pass

    def generate(self, promptTemplate, promptArgs):
        return "This is a dry run!"
