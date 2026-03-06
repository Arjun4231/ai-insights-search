import os

from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFDirectoryLoader
from config import openapi_key
from config import model
from config import temp
from pathlib import Path

load_dotenv('.env')
os.environ['OPENAI_API_KEY'] = openapi_key

data_folder = Path("./docs")

pdf_loader = PyPDFDirectoryLoader(data_folder)
documents = pdf_loader.load()
chain = load_qa_chain(llm=OpenAI(temperature=temp,model_name=model))

def answer_query(query):
    return chain.run(input_documents=documents, question=query)

