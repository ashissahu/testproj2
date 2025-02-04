import os
import sys
import logging

# Define the log message format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#%(asctime)s) → Timestamp when the log is recorded.
#%(levelname)s) → Log level (INFO, WARNING, ERROR, etc.).
#%(module)s) → The module (filename) where the log was generated.
#%(message)s) → The actual log message.

# Define the directory where logs will be stored
log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log")

# Create the logs directory if it does not exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,  # Set logging level to INFO (logs INFO, WARNING, ERROR, CRITICAL)
    format=logging_str,  # Set the logging format
    handlers=[
        logging.FileHandler(log_filepath),  # Logs messages to a file
        logging.StreamHandler(sys.stdout)   # Logs messages to the console
    ]
)

# Create a custom logger with a specific name
logger = logging.getLogger("datasciencelogger")
