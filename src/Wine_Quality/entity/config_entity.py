from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    Local_data_file_path: Path
    STATUS_FILE: str
    all_schema: dict
    
    