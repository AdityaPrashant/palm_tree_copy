from palmTreesCounter.constants import *
from palmTreesCounter.utils.common import read_yaml, create_directories
from palmTreesCounter.entity.config_entity import (DataIngestionConfig)

class ConfigurationManager:
    """
    Class to manage the configuration of the application.

    It reads configuration parameters from YAML files and provides methods to access them.

    Attributes:
        config (dict): Dictionary containing configuration parameters.
        params (dict): Dictionary containing model parameters.
    """
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        """
        Initializes the ConfigurationManager with configuration and parameters file paths.

        Args:
            config_filepath (str, optional): Path to the configuration YAML file. 
                                              Defaults to CONFIG_FILE_PATH.
            params_filepath (str, optional): Path to the parameters YAML file. 
                                             Defaults to PARAMS_FILE_PATH.
        """
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Returns a DataIngestionConfig object containing the configuration 
        parameters for data ingestion.

        Returns:
            DataIngestionConfig: Object with data ingestion configuration parameters.
        """

        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            dataset_identifier=config.dataset_identifier,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config