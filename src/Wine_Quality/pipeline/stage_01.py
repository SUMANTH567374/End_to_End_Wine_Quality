from Wine_Quality.components.data_Ingestion import DataIngestion
from Wine_Quality.config.configuration import ConfigurationManager
from Wine_Quality import logger

STAGE_NAME='Data Ingestion'

class DataIngestion_Pipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()