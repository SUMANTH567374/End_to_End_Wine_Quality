from Wine_Quality.pipeline.stage_01 import DataIngestion_Pipeline
from Wine_Quality.pipeline.stage_02 import DataValidation_Pipeline
from Wine_Quality.pipeline.stage_03 import DataTransformationPipeline
from Wine_Quality.pipeline.stage_04 import ModelTrainingPipeline
from Wine_Quality.pipeline.stage_05 import ModelEvaluationPipeline
from Wine_Quality import logger

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestion_Pipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidation_Pipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
STAGE_NAME = "Model Training "
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   Model_training = ModelTrainingPipeline()
   Model_training.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
STAGE_NAME = "Model Evaluation "
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   Model_Evaluation = ModelEvaluationPipeline()
   Model_Evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     