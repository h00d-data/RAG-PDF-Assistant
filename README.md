# 📄 RAG PDF Assistant

### Intelligent Document Question Answering with LLM + Vector Search

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Elasticsearch](https://img.shields.io/badge/Search-Elasticsearch-orange)
![LLM](https://img.shields.io/badge/AI-LLM-green)
![Architecture](https://img.shields.io/badge/Architecture-RAG-purple)
![License](https://img.shields.io/badge/License-MIT-green)

Sistema de **consulta inteligente em documentos PDF** utilizando arquitetura **RAG (Retrieval Augmented Generation)**.

O projeto permite que usuários façam perguntas em linguagem natural e recebam respostas baseadas no conteúdo de documentos indexados.

A solução integra:

* LLM (Large Language Model)
* Embeddings semânticos
* Busca vetorial
* Elasticsearch
* Processamento de PDFs
* Docker para ambiente reproduzível

---

# 🧠 Arquitetura do Sistema

O fluxo abaixo representa o pipeline completo do sistema:

```
                    ┌────────────────────┐
                    │   Documentos PDF   │
                    └─────────┬──────────┘
                              │
                              ▼
                  ┌─────────────────────┐
                  │   Extração de Texto │
                  │       (pypdf)       │
                  └─────────┬───────────┘
                            │
                            ▼
                ┌─────────────────────────┐
                │  Geração de Embeddings  │
                │     (OpenAI API)        │
                └─────────┬───────────────┘
                          │
                          ▼
           ┌──────────────────────────────────┐
           │   Elasticsearch Vector Index     │
           │ Armazenamento Vetorial (kNN)    │
           └───────────────┬──────────────────┘
                           │
                           ▼
           ┌──────────────────────────────────┐
           │      Busca Semântica (kNN)       │
           │   Recupera documentos relevantes │
           └───────────────┬──────────────────┘
                           │
                           ▼
           ┌──────────────────────────────────┐
           │        Contexto Recuperado       │
           │ enviado para o modelo de linguagem│
           └───────────────┬──────────────────┘
                           │
                           ▼
                 ┌───────────────────────┐
                 │        LLM API        │
                 │    geração resposta   │
                 └───────────┬───────────┘
                             │
                             ▼
                     ┌───────────────┐
                     │    Resposta   │
                     │   ao usuário  │
                     └───────────────┘
```

Este padrão arquitetural é conhecido como:

**Retrieval Augmented Generation (RAG)**

Utilizado amplamente em:

* assistentes corporativos
* busca em bases de conhecimento
* análise de contratos
* suporte técnico automatizado
* sistemas jurídicos
* pesquisa acadêmica

---

# 📂 Estrutura do Projeto

```
rag_pdf_agent/

documentos/
    exemplo.pdf

extrair_pdf.py
indexar_embeddings.py
buscar_contexto.py
agente_rag.py

requirements.txt
Dockerfile
docker-compose.yml
README.md
```

### Componentes

| Arquivo               | Função                              |
| --------------------- | ----------------------------------- |
| extrair_pdf.py        | extrai texto dos PDFs               |
| indexar_embeddings.py | gera embeddings e indexa documentos |
| buscar_contexto.py    | busca semântica baseada em vetores  |
| agente_rag.py         | agente que consulta o LLM           |
| documentos/           | base de conhecimento em PDF         |

---

# ⚙️ Tecnologias Utilizadas

* Python
* OpenAI API
* Elasticsearch
* Vector Search
* Retrieval Augmented Generation (RAG)
* pypdf
* Docker
* Docker Compose

---

# 🔑 Configuração da API

Defina sua chave da API:

```
export OPENAI_API_KEY="sua_chave_aqui"
```

Ou adicionando ao `.bashrc`

```
nano ~/.bashrc
```

Adicionar:

```
export OPENAI_API_KEY="sua_chave_aqui"
```

Aplicar:

```
source ~/.bashrc
```

---

# 🐳 Executando com Docker

Subir ambiente:

```
docker compose up --build
```

---

# 📥 Indexar PDFs

Após subir os containers:

```
docker exec -it rag_agent python indexar_embeddings.py
```

Esse processo:

1. lê os PDFs
2. extrai texto
3. gera embeddings
4. indexa no Elasticsearch

---

# 💬 Executar o Assistente

```
docker exec -it rag_agent python agente_rag.py
```

Exemplo:

```
Pergunta: O que é overfitting?
```

O sistema irá:

1️⃣ gerar embedding da pergunta
2️⃣ buscar trechos relevantes
3️⃣ enviar contexto ao LLM
4️⃣ retornar resposta baseada nos documentos

---

# 📊 Conceitos Demonstrados

Este projeto demonstra experiência em:

* arquitetura RAG
* embeddings semânticos
* busca vetorial
* integração com APIs de LLM
* processamento de documentos
* containerização com Docker
* engenharia de sistemas de IA

---

# 🚀 Possíveis Evoluções

Melhorias naturais do projeto:

* chunking de documentos
* embeddings locais
* pipeline de ingestão com Airflow
* API REST com FastAPI
* interface web com Streamlit
* uso de FAISS ou Weaviate

---

# 📌 Casos de Uso

Arquiteturas RAG são utilizadas para:

* assistentes empresariais
* análise de documentos
* busca em bases internas
* suporte técnico
* automação de atendimento
* sistemas jurídicos

---

# 📜 Licença

Este projeto é **open-source**.

Você pode:

* usar
* modificar
* adaptar
* utilizar em projetos pessoais ou comerciais

desde que **mantenha a atribuição ao autor original**.

---

# 👨‍💻 Autor

Desenvolvido por **h00d**.

Caso utilize este projeto, apenas mantenha a referência ao autor no código ou documentação.
![License](https://img.shields.io/badge/License-MIT-green)
---

⭐ Se este projeto foi útil, considere dar uma estrela no repositório.


