from pypdf import PdfReader


def extrair_texto_pdf(caminho):

    reader = PdfReader(caminho)

    texto = ""

    for pagina in reader.pages:
        conteudo = pagina.extract_text()

        if conteudo:
            texto += conteudo + "\n"

    return texto
