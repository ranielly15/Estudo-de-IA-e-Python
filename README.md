# 🤖 Chat com PDFs usando RAG (Retrieval-Augmented Generation)

Este projeto é um sistema de perguntas e respostas baseado em documentos PDF. Ele utiliza a técnica **RAG** para permitir que uma Inteligência Artificial (OpenAI) responda dúvidas baseadas exclusivamente no conteúdo dos arquivos fornecidos, reduzindo alucinações e focando no contexto real.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework de IA:** LangChain (Versão atualizada 0.2+)
* **Banco Vetorial:** ChromaDB
* **Modelo de LLM:** OpenAI (GPT-3.5/4)
* **Gerenciamento de Ambiente:** Venv + Dotenv

## 🚀 Funcionalidades

1.  **Carregamento de PDFs:** Lê automaticamente todos os arquivos `.pdf` armazenados na pasta `base`.
2.  **Processamento de Texto:** Divide os documentos em pedaços menores (*chunks*) para otimizar a leitura da IA.
3.  **Busca Semântica:** Transforma textos em vetores numéricos (embeddings) para encontrar os trechos mais relevantes para a pergunta do usuário.
4.  **Chat Interativo:** Interface via terminal para conversar com os documentos.

## 📚 Aprendizados e Desafios Superados
https://www.youtube.com/@HashtagProgramacao
Este projeto foi inspirado em um tutorial do canal **(https://www.youtube.com/@HashtagProgramacao)**, mas foi **refatorado e atualizado** para funcionar com as versões mais recentes das bibliotecas em 2025.

Durante o desenvolvimento, os seguintes desafios foram resolvidos:
* **Atualização do LangChain:** Adaptação do código para as novas importações (`langchain_chroma`, `langchain_text_splitters`) que mudaram recentemente.
* **Ambiente Windows:** Resolução de conflitos de DLL e configuração correta de variáveis de ambiente no Windows.
* **Segurança:** Implementação de variáveis de ambiente (`.env`) para proteger a chave da API, garantindo que dados sensíveis não subam para o GitHub.

## ⚙️ Como rodar o projeto localmente

Siga os passos abaixo para testar na sua máquina:

### 1. Clone o repositório
```bash
git clone [https://github.com/ranielly15/Estudo-de-IA-e-Python.git](https://github.com/ranielly15/Estudo-de-IA-e-Python.git)
cd Estudo-de-IA-e-Python

### 2. Crie um ambiente virtual
python -m venv venv
.\venv\Scripts\activate  # No Windows

3. Instale as dependências
pip install langchain langchain-community langchain-openai langchain-chroma chromadb openai pypdf python-dotenv

4. Configure a Chave de API
Crie um arquivo chamado .env na raiz do projeto e adicione sua chave da OpenAI:
OPENAI_API_KEY=sk-sua-chave-aqui-123456...

5. Execute
Primeiro, gere o banco de dados:
python criar_db.py

Depois, inicie o chat:
python main.py
