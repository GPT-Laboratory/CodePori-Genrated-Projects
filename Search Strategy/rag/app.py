from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_openai.embeddings import OpenAIEmbeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_core.messages import HumanMessage
from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)
index_name = "femma-index"
template = """
I will provide you with the question asked by the user and also the three most relevant answer from the pinecone index.
You need to understand the answers and provide a response to the user's question. 

here are the rules you must follow while writing a response:
 - All the information in context should be used to provide a response to the user's question.
 - The response should be formatted in a very good manner that is bold letters, bullet points whereever necesaary.
 - Also the response should not include saying here's the extracted  response from pinecone index. It should be a direct response to the user's question.
 

Question: {question}
pinecone_answers: {pinecone_answers}
"""
prompt = ChatPromptTemplate.from_template(template)
# Initialize the Chat model
# model = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo")
model = ChatOpenAI(openai_api_key="OpenAI API key", model="gpt-3.5-turbo")
# Initialize Pinecone
pc = Pinecone(api_key="Pincone Database API Key")
index = pc.Index(index_name)
index.describe_index_stats()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
parser = StrOutputParser()

pinecone = PineconeVectorStore(index_name=index_name, embedding=embeddings, pinecone_api_key="Pincone Database API Key")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    question = request.form['question']
    results = pinecone.similarity_search(question)[:3]

    # Prepare the prompt
    chat_prompt = template.format(pinecone_answers=results, question=question)
    
    messages = [HumanMessage(content=chat_prompt)]
    
    # Get the response from the model
    response = model.invoke(messages)
    return jsonify({'response': response.content})

if __name__ == '__main__':
    app.run(debug=True, port=5002)