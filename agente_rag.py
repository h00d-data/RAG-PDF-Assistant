import os
from openai import OpenAI
from buscar_contexto import buscar

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def main():

    pergunta = input("\nPergunta: ")

    contexto = buscar(pergunta)

    prompt = f"""
Use o contexto abaixo para responder a pergunta.

Contexto:
{contexto}

Pergunta:
{pergunta}
"""

    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "Responda usando apenas o contexto fornecido."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    resposta = resp.choices[0].message.content

    print("\nResposta:\n")
    print(resposta)


if __name__ == "__main__":
    main()
