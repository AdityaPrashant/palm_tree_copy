from palmTreesCounter.constants import *
from palmTreesCounter.utils.common import read_yaml, create_directories
from palmTreesCounter.entity.config_entity import (BaseModelConfig, DataIngestionConfig)

class ConfigurationManager:
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
    

    def get_base_model_config(self) -> BaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        base_model_config = BaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return base_model_config
    

    