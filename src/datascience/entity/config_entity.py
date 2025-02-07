

# Importing the 'dataclass' decorator from the 'dataclasses' module  
# This helps in creating a simple class to store data without writing boilerplate code  
from dataclasses import dataclass  

# Importing 'Path' from the 'pathlib' module  
# 'Path' is used for handling filesystem paths in an object-oriented way  
from pathlib import Path




# Using the '@dataclass' decorator to automatically generate special methods  
# like '__init__', '__repr__', and '__eq__' for the class  
@dataclass  
class DataIngestionConfig:  
    # Root directory where all data-related files will be stored  
    root_dir: Path  
    # URL of the source data that needs to be downloaded  
    source_URL: str  
    # Local path where the downloaded data file will be stored  
    local_data_file: Path  
    # Directory where the extracted data will be stored after unzipping  
    unzip_dir: Path  


# Define a data class for storing data validation configuration  
@dataclass  
class DataValidationConfig:  
    root_dir: Path  # The root directory where validation-related files are stored  
    STATUS_FILE: str  # Path to the status file that tracks validation results  
    unzip_data_dir: Path  # Directory where unzipped data is stored for validation  
    all_schema: dict  # Dictionary containing schema definitions for validation  


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str