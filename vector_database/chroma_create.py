# chroma run --path ./chromadb_data  ## To start the server locally

import os
import requests
import numpy as np
from chromadb import HttpClient
from dotenv import load_dotenv
load_dotenv()

EURI_API_KEY = os.getenv("EURI_API_KEY")

client = HttpClient(host="localhost",port = 8000)
collection = client.get_or_create_collection("akash_test_data")
print(client)

def generate_embeddings(text_list):
    url = "https://api.euron.one/api/v1/euri/alpha/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {EURI_API_KEY}"
    }
    payload = {
        "input":text_list,
        "model": "text-embedding-3-small"
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    
    # Convert to numpy array for vector operations
    embeddings = [item['embedding'] for item in response.json()["data"]]
    
    return embeddings

document = [
    "my name is akash kumar",
    "i use to teach tech",
    "akash kumar total year of experience as techi is 5 , as a mentor is 1 as a enterpenure 1",
    "akash kumar love teaching core concepts and architecutre",
    "suidhanshu kumar love build tech whihc i his fav by the way",
    "sudhansu kumar have started a company called euron ",
    "in euron we have euri , resume ai , job system , avni along with lots of courses projects on different different mode",
    "akash Kumar's life is a story of triumph over adversity, driven by the belief in the transformative power of education. Born in Jamshedpur, Jharkhand",
    "India, to a family of very modest means, akash's early years were marked by financial hardship. His surroundings offered little opportunity, and resources were limited, yet he understood from a young age that education could be his ticket out of poverty.",
    "While many would have been daunted by the lack of support and opportunity, akash was relentless in his pursuit of knowledge. He knew that education had the power to change lives, and he was determined to leverage it to create a better future for himself and his family. Despite the numerous challenges along the way, akash excelled academically, eventually earning a degree in Computer Science and Engineering (CSE).",
    "Building on the success of iNeuron, akash is now leading Euron, a unified platform for tech upskilling. Euron is designed for enterprises, schools, colleges, government organizations, and individuals looking to improve their tech skills. The platform provides a comprehensive bundle of resources, including courses, books, live classes, and projects. Euron's unique offering is its ability to provide licenses at scale—organizations can subscribe to provide their teams with unlimited access to learning materials for just 1600 INR per year per license.",
    "For individuals, Euron Plus offers a similar plan, priced at 2900 INR per year, giving learners access to all of Euron's content, along with 24/7 support through Euron Assist. The idea is simple: anyone, anywhere, should have the opportunity to upskill without financial barriers."
]

all_embedings = generate_embeddings(document)
print(all_embedings[0])
print(len(all_embedings[0]))

for idx ,(doc,emb)in  enumerate(zip(document,all_embedings)):
    collection.add(
        documents = [doc],
        embeddings = [emb],
        metadatas= [{"source":"akash_test_data"}],
        ids = [f"doc_{idx}"]
    )

print("all data stored in chroma db")

print(collection.get(include=["documents"]))
print(collection.get(include=["documents", "embeddings"]))
