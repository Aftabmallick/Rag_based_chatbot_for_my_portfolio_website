import os
import sys

import langchain_core
from src.exception import CustomException
from src.logger import logging
from src.utils import read_Doc

from dataclasses import dataclass
import os
from dotenv import load_dotenv, find_dotenv


from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone
import pinecone 
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")


load_dotenv(Path(".env"))

@dataclass
class EmbeddingConfig:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'))
        self.pc=pinecone.init(
            api_key=os.getenv('PINECONE_API_KEY'),
            environment=os.getenv('PINECONE_ENVIRONMENT')
        )
        self.index_name =os.getenv('PINECONE_INDEX_NAME')
class Embedding:
    def __init__(self):
        self.embedding_config = EmbeddingConfig()

    def initiate_embeddings(self,chunked_data):
        try:
            logging.info("Entered into embedding step")
            #print("********************************************")
            #print(type(chunked_data[0]))
            index=Pinecone.from_documents(chunked_data,self.embedding_config.embeddings ,index_name=self.embedding_config.index_name)
            logging.info("Succefully uploaded data in pinecone")
            #pinecone.download_index(index, 'index/index.pine')
            #logging.info("Succefully downloaded index file locally")
            return index
        except Exception as e:
            raise CustomException(e,sys)
class AccessIndex:
    def __init__(self) -> None:
        self.embeddings = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'))
        self.index_name =os.getenv('PINECONE_INDEX_NAME')
        self.index=Pinecone.from_documents([langchain_core.documents.base.Document(" ")],self.embeddings ,index_name=self.index_name)
    def access_index(self):
        try:           
            return self.index
        except Exception as e:
            raise CustomException(e,sys)
    def delete_index(self):
        try:
            self.index.delete(delete_all=True)
            logging.info("Succefully Deleted all index")
        except Exception as e:
            raise CustomException(e,sys)