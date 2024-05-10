import os
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.embeddings import Embedding,AccessIndex
from src.components.prediction import RetriverPipeline
from src.exception import CustomException
from src.logger import logging

from langchain.chains.question_answering import load_qa_chain
from langchain import OpenAI
import warnings
warnings.filterwarnings("ignore")



class AnswerPipeline:
    def __init__(self) :
        pass
    def get_answer(self,query):

        embed =AccessIndex()
        index=embed.access_index()
        retriver = RetriverPipeline()
        ans= retriver.retireve_answers(query=query, index=index)
        return ans
    
if __name__ == "__main__":
    ans =AnswerPipeline()
    answer =ans.get_answer("tell me about aftab")
    print(answer)