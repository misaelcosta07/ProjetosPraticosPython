from groq import Groq
from chave import get_client

client = get_client()

#funçao para traduzir o texto usando IA
def traduzir_texto(texto, idioma):
    prompt = f"Traduza o texto abaixo para {idioma.lower()}.Apenas a tradução sem comentários. Importante: ** Mantenha o sentido do texto, após a tradução**\n\n{texto}"

    resposta =  client.chat.completions.create(model ="openai/gpt-oss-20b", messages = [{"role": "user", "content":prompt }])
         
    return resposta.choices[0].message.content

texto_traduzir = input("Digite o texto:\n")
idioma = input("Qual o idioma destino?\n")

traducao = traduzir_texto(texto_traduzir, idioma)

print("\n Tradução:")
print(traducao)