import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataIngestionConfig)


# Component - Data Ingestion  

# Defining the DataIngestion class for handling data downloading and extraction  
class DataIngestion:  
    def __init__(self, config: DataIngestionConfig):  
        # Initializing with the data ingestion configuration  
        self.config = config  

    # Method to download the zip file from the source URL  
    def download_file(self):  
        # Checking if the file already exists in the local directory  
        if not os.path.exists(self.config.local_data_file):  
            # Downloading the file from the source URL and saving it locally  
            filename, headers = request.urlretrieve(  
                url=self.config.source_URL,  # URL to fetch the file  
                filename=self.config.local_data_file  # Path to save the downloaded file  
            )  
            # Logging the successful download and header information  
            logger.info(f"{filename} downloaded successfully! Details: \n{headers}")  
        else:  
            # Logging that the file already exists, avoiding redundant downloads  
            logger.info(f"File already exists at {self.config.local_data_file}")  

    # Method to extract the contents of the downloaded ZIP file  
    def extract_zip_file(self):  
        """  
        Extracts the ZIP file into the designated data directory.  
        """  
        unzip_path = self.config.unzip_dir  # Path to extract files  
        os.makedirs(unzip_path, exist_ok=True)  # Creating the extraction directory if it doesn’t exist  

        # Extracting the ZIP file using the zipfile module  
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:  
            zip_ref.extractall(unzip_path)  # Extracting all contents to the directory  

        # Logging the successful extraction  
        logger.info(f"Files extracted successfully to {unzip_path}")  
