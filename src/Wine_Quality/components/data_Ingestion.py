import os
import urllib.request as request
from Wine_Quality import logger
from Wine_Quality.utils.common import get_size
from Wine_Quality.entity.config_entity import DataIngestionConfig
import pathlib as path
import gdown

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        Downloads the file from the source URL to a local path.
        """
        file_exists = os.path.exists(self.config.local_data_file)
        logger.info(f"Checking file existence: {file_exists}")
        
        if not file_exists:
            try:
                logger.info(f"Downloading file from {self.config.source_URL}")
                # Use gdown to download from Google Drive
                gdown.download(self.config.source_URL, self.config.local_data_file, quiet=False)
                logger.info(f"File downloaded: {self.config.local_data_file}")
            except Exception as e:
                logger.error(f"Error downloading file: {e}")
        else:
            file_size = get_size(Path(self.config.local_data_file))
            logger.info(f"File already exists, size: {file_size}")