# importei as biblitecas 
import imaplib  #permite acessar sua caixa de entrada pelo protocolo IMAP.
import email #biblioteca que ajuda a ler mensagens

# declarando meu email e senha 
email = "misaelcosta069gmail.com"
senha = "mffh mpbi dkmw qgry"

#conectar o servidor do imap do Gmail
"""
Abrem uma conexão segura com o Gmail
Entram na sua conta usando e-mail + senha app
"""
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("misaelcosta069@gmail.com", "mffh mpbi dkmw qgry" )

# Selecionar a caixa de entrada 
mail.select("inbox")

# Buscar emails antes de 01/01/2025
#"Google, me traga todos os e-mails enviados ANTES de 1º de janeiro de 2025".
status, dados = mail.search(None, 'BEFORE 01-jan-2025')

# Transformar os UIDs em lista
#Aqui estamos apenas pegando todos os IDs dos e-mails que têm que ser apagados.
email_ids = dados[0].split()
print(f"encontrados {len(email_ids)} emails para apagar")

# Apagar todos
#Só para você saber o tamanho da limpeza.
for uid in email_ids:
    mail.store(uid, "+FLAGS", "\\deleted")

# finalizar remoçao
mail.expunge() #o Gmail deleta de vez e libera espaço.
mail.close()
mail.logout()

print("limpeza completa") 