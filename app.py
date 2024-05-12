import streamlit as st
from langchain_core.messages import AIMessage,HumanMessage
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.chains import create_history_aware_retriever,create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

import os
from src.components.embeddings import AccessIndex

def get_context_retriever_chain(vector_store,opkey):
    llm = ChatOpenAI(openai_api_key=opkey)

    retriever = vector_store.as_retriever()
    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("user","{input}"),
        ("user","Given the above conversation, generate a search query to look up in order to get information relevent to this conversation")
    ])
    retriever_chain = create_history_aware_retriever(llm,retriever,prompt)
    return retriever_chain

def get_conversational_rag_chain(retriever_chain,opkey):
    llm = ChatOpenAI(openai_api_key=opkey)
    prompt = ChatPromptTemplate.from_messages([
        ("system","Your name is Aftab Mallick.Next your resume and more details will be provided.Answer the user's questions based on the below context:\n\n{context}"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user","{input}"),
    ])
    stuff_document_chain = create_stuff_documents_chain(llm,prompt)

    return create_retrieval_chain(retriever_chain,stuff_document_chain)
def get_response(user_input):
    #create conversation chain
    retriever_chain = get_context_retriever_chain(st.session_state.vector_store,os.getenv('OPENAI_API_KEY'))
    convesation_rag_chain=get_conversational_rag_chain(retriever_chain,os.getenv('OPENAI_API_KEY'))
    response = convesation_rag_chain.invoke({
            "chat_history":st.session_state.chat_history,
            "input":user_query
            })
    return response['answer']
st.set_page_config(page_title="Chat With Websites",page_icon="")

st.title("Ask about Me:")
st.write("Welcome to the chat app!")
if "chat_history" not in st.session_state:
        st.session_state.chat_history=[
            AIMessage(content = "Hello I am AI Aftab, How can I help you?"),
        ]
if "vector_store" not in st.session_state:
     vc = AccessIndex()
     st.session_state.vector_store = vc.access_index()

user_query=st.chat_input("Type your message here..")
if user_query is not None and user_query !="":
    response = get_response(user_query)
    
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=response))

    

#conversation
for message in st.session_state.chat_history:
    if isinstance(message,AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message,HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)