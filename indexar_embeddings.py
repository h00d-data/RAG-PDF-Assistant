import os
from openai import OpenAI
from elasticsearch import Elasticsearch
from extrair_pdf import extrair_texto_pdf

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

es = Elasticsearch("http://elasticsearch:9200")

PASTA_DOCUMENTOS = "documentos"


def indexar_documentos():

    for arquivo in os.listdir(PASTA_DOCUMENTOS):

        if arquivo.endswith(".pdf"):

            caminho = os.path.join(PASTA_DOCUMENTOS, arquivo)

            print(f"Processando {arquivo}...")

            texto = extrair_texto_pdf(caminho)

            if not texto.strip():
                continue

            emb = client.embeddings.create(
                model="text-embedding-3-small",
                input=texto
            )

            vetor = emb.data[0].embedding

            doc = {
                "arquivo": arquivo,
                "texto": texto,
                "embedding": vetor
            }

            es.index(index="pdf_docs", document=doc)

            print("Indexado:", arquivo)


if __name__ == "__main__":

    indexar_documentos()

    print("Indexação concluída.")
