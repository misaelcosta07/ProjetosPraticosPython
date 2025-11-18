#cabeçalho do jogo
print("--- Jogo Pedra, Papel e Tesoura (2 Jogadores) ---")
print("-----------------------------------------------------")
print("Regras do jogo:\n")
print("Escolham entre 'pedra', 'papel' ou 'tesoura'.")
print("-----------------------------------------------------")
# Coletas de dados usuario
jogador1 = input("Primeiro jogador entre com a sua jogada:\n")
jogador2 = input("Segundo jogador entre com a sua jogada:\n")
print("-----------------------------------------------------")
# tratar os dados coletados dos usuarios
jogador1 = jogador1.lower().strip()
jogador2 = jogador2.lower().strip()
print(f"primeiro jogador jogou:\n{jogador1}")
print(f"Segundo jogador jogou:\n{jogador2}")
print("-----------------------------------------------------")
#logica para determinar o vencedor
if jogador1 == jogador2:
    print("Resultado: EMPATE!")
elif (jogador1 =="pedra" and jogador2 =="tesoura") or (jogador1 =="tesoura" and jogador2 =="papel") or (jogador1 =="papel" and jogador2 =="pedra"): 
    print("Resultado: jogador 1, VENCEU.")
else :
     print("Resultado: jogador 2, VENCEU.")
print("-----------------------------------------------------")
print("FIM DE JOGO")