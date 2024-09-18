import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore


index_name = "femma-index"
template = """
Answer the question based on the context below. If you can't
answer the question, reply "I don't know".

Context: {context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
openai_api_key = 'OpenAI API Key'
model = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-3.5-turbo")
pc = Pinecone(api_key="Pincone Database API Key")
index = pc.Index(index_name)
index.describe_index_stats()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
parser = StrOutputParser()


loader = TextLoader("context.txt")
text_documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
documents = text_splitter.split_documents(text_documents)

pinecone = PineconeVectorStore.from_documents(
    documents, embeddings, index_name=index_name
)