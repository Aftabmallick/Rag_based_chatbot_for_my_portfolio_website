import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import read_Doc

from src.components.data_transformation import DataTransformation
from src.components.embeddings import Embedding
from src.components.prediction import RetriverPipeline

from dataclasses import dataclass
import warnings
warnings.filterwarnings("ignore")




@dataclass
class DataIngestionConfig:
    data_path: str = os.path.join('artifacts/')

class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered into data ingestion component")
        try:
            file_path = self.ingestion_config.data_path
            os.makedirs(os.path.dirname(file_path),exist_ok=True)            
            documents =read_Doc(file_path)

            logging.info("file reading complete")

            return documents


        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngestion()
    contents = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    chunk = data_transformation.initiate_data_transformer(contents)
    embed =Embedding()
    index = embed.initiate_embeddings(chunk)
    retriver = RetriverPipeline()
    ans= retriver.retireve_answers(query="Tell me about aftab mallick", index=index)
    print(ans)