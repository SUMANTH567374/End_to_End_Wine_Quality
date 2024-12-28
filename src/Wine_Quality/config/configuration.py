from Wine_Quality.constants import *
from Wine_Quality.utils.common import read_yaml,create_directories
from Wine_Quality.entity.config_entity import DataIngestionConfig ,DataValidationConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
        )

        return data_ingestion_config
    
    
    def check_file_exists(self, filepath, file_type):
        """Check if the file exists and raise an error if it does not."""
        if not Path(filepath).exists():
            raise FileNotFoundError(f"{file_type} not found at {filepath}")
        else:
            print(f"{file_type} found at {filepath}")

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        # Create the directories as needed
        create_directories([config.root_dir])

        # Create and return the data validation configuration
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            Local_data_file_path = config.Local_data_file_path,
            all_schema=schema,
        )

        return data_validation_config
