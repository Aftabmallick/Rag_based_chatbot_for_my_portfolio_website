import os
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.embeddings import Embedding,AccessIndex
from src.components.prediction import RetriverPipeline
from src.exception import CustomException
from src.logger import logging
import argparse


from langchain.chains.question_answering import load_qa_chain
from langchain import OpenAI
import warnings
warnings.filterwarnings("ignore")



class UpdatePipeline:
    def __init__(self) :
        pass
    def initiate_update(self):
        logging.info("Index update initiated")
        obj = DataIngestion()
        contents = obj.initiate_data_ingestion()
        data_transformation = DataTransformation()
        chunk = data_transformation.initiate_data_transformer(contents)
        embed =Embedding()
        index = embed.initiate_embeddings(chunk)
        logging.info("Index update Succefully")

    def delete_data(self):
        logging.info("Index delete initiated")
        embed =AccessIndex()
        embed.delete_index()
        logging.info("Index delete Succefully")


if __name__ == "__main__":
    up =UpdatePipeline()
    parser = argparse.ArgumentParser(description='Pipeline update script')

    parser.add_argument("-update", action="store_true", help="Initiate update")
    parser.add_argument("-delete", action="store_true", help="Delete data")
    
    args = parser.parse_args()
    if args.update:
        up.initiate_update()
    elif args.delete:
        up.delete_data()
    else:
        print("No valid argument provided.")