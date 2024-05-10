import os
import sys
from src.exception import CustomException
from src.logger import logging

from langchain.chains.question_answering import load_qa_chain
from langchain import OpenAI
import warnings
warnings.filterwarnings("ignore")



class RetriverPipeline:
    def __init__(self) :
        llm=OpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0.5)
        self.chain=load_qa_chain(llm,chain_type="stuff")
    def retrieve_query(self,index,query):
        try:
            matching_results=index.similarity_search(query,k=2)
            return matching_results
        except Exception as e:
            raise CustomException(e,sys)
    def retireve_answers(self,query,index):
        doc_search=self.retrieve_query(index,query)
        print(doc_search)
        response=self.chain.run(input_documents=doc_search,question=query)
        return response