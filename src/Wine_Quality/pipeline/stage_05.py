from Wine_Quality.components.Model_evaluation import ModelEvaluation
from Wine_Quality.config.configuration import ConfigurationManager
from Wine_Quality import logger
from pathlib import Path


STAGE_NAME='Model Evaluation'

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()