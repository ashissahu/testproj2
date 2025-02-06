import os
from src.datascience import logger
import pandas as pd  # Used for handling and processing CSV files
from src.datascience.entity.config_entity import (DataValidationConfig)

# Define the DataValidation class to validate data against a predefined schema
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        """
        Initializes the DataValidation class with a configuration object.

        Parameters:
        config (DataValidationConfig): Configuration object containing validation settings.
        """
        self.config = config  # Store the configuration settings

    def validate_all_columns(self) -> bool:
        """
        Validates if all the required columns are present in the dataset.

        Returns:
        bool: True if validation is successful, False otherwise.
        """
        try:
            validation_status = None  # Initialize validation status as None

            # Read the CSV file containing the data to be validated
            data = pd.read_csv(self.config.unzip_data_dir)

            # Get the list of all columns present in the dataset
            all_cols = list(data.columns)

            # Retrieve the expected schema columns from the configuration
            all_schema = self.config.all_schema.keys()

            # Iterate over each column in the dataset
            for col in all_cols:
                # Check if the column exists in the predefined schema
                if col not in all_schema:
                    validation_status = False  # Mark validation as failed
                    with open(self.config.STATUS_FILE, 'w') as f:  # Open status file for writing
                        f.write(f"Validation status: {validation_status}")  # Log the status
                else:
                    validation_status = True  # Mark validation as successful
                    with open(self.config.STATUS_FILE, 'w') as f:  # Open status file for writing
                        f.write(f"Validation status: {validation_status}")  # Log the status

            return validation_status  # Return final validation result

        except Exception as e:
            raise e  # Raise any exceptions encountered during validation
