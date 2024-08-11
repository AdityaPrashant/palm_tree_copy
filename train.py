from palmTreesCounter import logger
from palmTreesCounter.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from palmTreesCounter.pipeline.stage_02_get_base_model import BaseModelTrainingPipeline
from palmTreesCounter.pipeline.stage_03_model_trainer import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage - {STAGE_NAME} started <<<<<<")
    objective = DataIngestionTrainingPipeline()
    objective.main()
    logger.info(f">>>>>> Stage - {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Base Model Configuration"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> Stage - {STAGE_NAME} Started <<<<<<")
   base_model = BaseModelTrainingPipeline()
   base_model.main()
   logger.info(f">>>>>> Stage - {STAGE_NAME} Completed <<<<<<\n\n")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> Stage - {STAGE_NAME} Started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> Stage - {STAGE_NAME} Completed <<<<<<\n\n")
except Exception as e:
        logger.exception(e)
        raise e
