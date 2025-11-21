from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

CAMINHO_DB = "db"

prompt_template = """ Responda a pergunta do usuário {pergunta} 
com base nessas informações: {base_conhecimento}
Se vocÊ  não encontarar a resposta para a pergunta do usuário nessas informações, responda que não sabe"""

def perguntar():
    pergunta = input("Escreva sua pergunta: ")

    #carregar o banco de dados 
    funcao_embedding = OpenAIEmbeddings()
    db = Chroma(persist_directory=CAMINHO_DB, embedding_function= funcao_embedding)

    #comparar a pergunta do usuáro (embedding) com os embeddings do banco de dados (similaridade)

    resultados = db.similarity_search_with_relevance_scores(pergunta, k=3)
    if len(resultados)==0 or resultados[0][1]<0.7:
        print("Desculpe, não sei a resposta para essa pergunta.")
        return
    
    textos_resultado = []
    for resultado in resultados:
        texto = resultado[0].page_content
        textos_resultado.apped(texto)

    base_conhecimento = "\n\n----\n\n".join(textos_resultado)
    prompt = ChatPromptTemplate.from_template(prompt_template)
    prompt = prompt.invok({"pergunta": pergunta, "base_conhecimento": base_conhecimento})
    #print(prompt)

    modelo = ChatOpenAI()
    texto_resposta = modelo.invoke(prompt).content
    print("Resposta da IA", texto_resposta)

perguntar()
