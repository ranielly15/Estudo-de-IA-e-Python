from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
PASTA_BASE= "base"

def criar_db():

    #carregar documentos
    documentos = carregar_documentos()
    #dividir os documentos em pedaços de texto (chunks)
    chunks = dividir_chunks(documentos)
    # #vetorizar os chunks como processo de embedding
    vetorizar_chunks(chunks)

def carregar_documentos():
    carregador = PyPDFDirectoryLoader(PASTA_BASE, glob="*.pdf")
    documentos = carregador.load()
    return documentos

def dividir_chunks(documentos):
    separador_documentos = RecursiveCharacterTextSplitter(
        chunk_size= 2000, 
        chunk_overlap = 500, #garante que não perca contexto entre os chunks e tenha uma resposta mais completa para o usuário
        length_function = len,
        add_start_index = True
    )
    chunks = separador_documentos.split_documents(documentos)
    print(len(chunks))
    return chunks

def vetorizar_chunks(chunks):
    db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory= "db")
    print("Banco de Dados criado")


criar_db()