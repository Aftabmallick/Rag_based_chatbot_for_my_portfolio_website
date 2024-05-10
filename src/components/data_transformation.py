import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import chunk_data

from dataclasses import dataclass

class DataTransformation:
    def __init__(self):
        pass
    def initiate_data_transformer(self,text_data):
        try:
            logging.info("Data transformation started")
            chunked_data = chunk_data(data=text_data)
            logging.info("Data transformation successful")

            return chunked_data
            
        except Exception as e:
            raise CustomException(e,sys)