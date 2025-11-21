import os
from dotenv import load_dotenv

carregou = load_dotenv()

print(f"O arquivo .env foi encontrado? {carregou}")

chave = os.getenv("OPENAI_API_KEY")

if chave:
    print(f"SUCESSO! A chave foi lida. Começa com: {chave[7:]}")
else:
    print("ERRO!: O pythin não conseguiu ler a chave. Verifique o nome do arquivo.")