from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories

from src.datascience.entity.config_entity import (DataIngestionConfig,DataValidationConfig,
                                                  DataTransformationConfig,ModelTrainerConfig,
                                                  ModelEvaluationConfig)

# Defining the ConfigurationManager class to manage configuration settings
class ConfigurationManager:  
    def __init__(self,  
                 config_filepath=CONFIG_FILE_PATH,  # Path to the main configuration file  
                 params_filepath=PARAMS_FILE_PATH,  # Path to the parameters file  
                 schema_filepath=SCHEMA_FILE_PATH):  # Path to the schema file  
        print(config_filepath)

        # Reading configuration settings from the YAML files  
        self.config = read_yaml(config_filepath)  # Loads the main configuration file  
        self.params = read_yaml(params_filepath)  # Loads the parameters file  
        self.schema = read_yaml(schema_filepath)  # Loads the schema file  

        # Creating necessary directories specified in the configuration  
        create_directories([self.config.artifacts_root])  # Ensures the artifact root directory exists  

    # Method to get the data ingestion configuration  
    def get_data_ingestion_config(self) -> DataIngestionConfig:  
        # Extracting data ingestion-related settings from the configuration  
        config = self.config.data_ingestion  

        # Creating the root directory for data ingestion if it doesn’t exist  
        create_directories([config.root_dir])  

        # Creating an instance of DataIngestionConfig with necessary parameters  
        data_ingestion_config = DataIngestionConfig(  
            root_dir=config.root_dir,  # Directory for storing ingested data  
            source_URL=config.source_URL,  # URL to fetch the data from  
            local_data_file=config.local_data_file,  # Path to store the downloaded data file  
            unzip_dir=config.unzip_dir  # Path where extracted files will be stored  
        )  

        # Returning the configured data ingestion object  
        return data_ingestion_config  
    


    # Function to retrieve the Data Validation configuration
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation  # Access data validation settings
        schema = self.schema.COLUMNS  # Extract schema column definitions from YAML

        # Ensure the root directory for data validation exists
        create_directories([config.root_dir])

        # Create a DataValidationConfig instance with extracted settings
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,  # Directory for validation-related files
            STATUS_FILE=config.STATUS_FILE,  # Path to the validation status file
            unzip_data_dir=config.unzip_data_dir,  # Directory where unzipped data is stored
            all_schema=schema,  # Schema dictionary containing column definitions
        )

        return data_validation_config  # Return the configured DataValidationConfig object
    
    # Function to retrieve the Data Validation configuration
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name

        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config=self.config.model_evaluation
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path = config.model_path,
            all_params=params,
            metric_file_name = config.metric_file_name,
            target_column = schema.name,
            mlflow_uri="https://dagshub.com/ashissahu/testproj2.mlflow"


        )
        return model_evaluation_config