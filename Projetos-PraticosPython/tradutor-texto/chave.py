
from dotenv import load_dotenv # ler o arquivo .env
import os # permite acessar o sistema operacional de variaveis de ambientes
from groq import Groq # import o client oficial api groq

 #Função que cria e devolve um cliente pronto pra usar.
def get_client():
    load_dotenv() #Carrega as variáveis do arquivo .env.
    api_key= os.getenv("Groq_API_KEY") # PEGA O valor da variavel

    # verificar erro e impedir o programa de continuar
    if api_key is None:
        raise ValueError("ERRO: variavel Groq_API_KEY nao encontrada. verifique o arquivo " \
        ".env")
    return Groq(api_key = api_key) #Cria o cliente autenticado e devolve para ser usado em outro arquivo.
