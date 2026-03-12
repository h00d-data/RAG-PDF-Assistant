import os
from openai import OpenAI
from elasticsearch import Elasticsearch

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

es = Elasticsearch("http://elasticsearch:9200")


def buscar(pergunta):

    emb = client.embeddings.create(
        model="text-embedding-3-small",
        input=pergunta
    )

    vetor = emb.data[0].embedding

    resp = es.search(
        index="pdf_docs",
        knn={
            "field": "embedding",
            "query_vector": vetor,
            "k": 3,
            "num_candidates": 10
        }
    )

    textos = []

    for hit in resp["hits"]["hits"]:
        textos.append(hit["_source"]["texto"])

    return "\n".join(textos)
