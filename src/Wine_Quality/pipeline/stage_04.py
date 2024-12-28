from Wine_Quality.components.Mode_training import ModelTrainer
from Wine_Quality.config.configuration import ConfigurationManager
from Wine_Quality import logger
from pathlib import Path

STAGE_NAME='Model Training'

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()