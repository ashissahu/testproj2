from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger


STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        # Creating an instance of ConfigurationManager to read configuration files  
        config = ConfigurationManager()  
        # Retrieving the data ingestion configuration settings  
        data_ingestion_config = config.get_data_ingestion_config()  
        # Creating an instance of DataIngestion with the retrieved configuration  
        data_ingestion = DataIngestion(config=data_ingestion_config)  
        # Downloading the data file from the source URL  
        data_ingestion.download_file()  
        # Extracting the contents of the downloaded ZIP file  
        data_ingestion.extract_zip_file()  



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e