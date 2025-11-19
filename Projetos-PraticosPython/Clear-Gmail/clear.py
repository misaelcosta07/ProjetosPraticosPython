import imaplib

email = "misaelcosta069@gmail.com"
senha = "mffhmpbidkmwqgry"


mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("misaelcosta069@gmail.com", "mffhmpbidkmwqgry")
mail.select("inbox")

# Pegar todos os UIDs de emails ANTES de 2025
status, dados = mail.uid("SEARCH", None, 'BEFORE 01-Jan-2025')

uids = dados[0].split()
total = len(uids)

print(f"Total a apagar: {total}")

# Transformar os UIDs em inteiros e ordenar
uids = sorted([int(x) for x in uids])

# Tamanho do range — pode ser 500, 1000, 2000
STEP = 800

# Criar blocos de ranges
for i in range(0, len(uids), STEP):
    inicio = uids[i]
    fim = uids[min(i + STEP - 1, len(uids) - 1)]
    range_uid = f"{inicio}:{fim}"

    print(f"Apagando range UID {range_uid}...")

    # Apagar o range inteiro de uma vez
    mail.uid("STORE", range_uid, "+FLAGS", "\\Deleted")
    mail.expunge()

    print(f"Range {range_uid} concluído.")

mail.close()
mail.logout()

print("✔ Limpeza finalizada com sucesso!")


