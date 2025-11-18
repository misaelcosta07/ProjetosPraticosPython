#cabeçalho do jogo
print("--- Jogo Pedra, Papel e Tesoura (2 Jogadores) ---")
print("-----------------------------------------------------")
#tupla para valores imutaveis. 
# iremos passar os  unicos valores possiveis para as jogadas
opcoes_validas = ("pedra", "papel", "tesoura") 
print(f"Opções validas: {opcoes_validas}")
print("-" *25) #imprime uma linhapara separar 

# Coletas de dados usuario
jogador1 = input("Primeiro jogador entre com a sua jogada:\n")
jogador2 = input("Segundo jogador entre com a sua jogada:\n")

# tratar os dados coletados dos usuarios
jogador1 = jogador1.lower().strip()
jogador2 = jogador2.lower().strip()

print("-" *25)
print(f"primeiro jogador jogou:\n{jogador1}")
print(f"Segundo jogador jogou:\n{jogador2}")
print("-" *25)

#logica para determinar o vencedor
#1. verificar jogadas validas

if jogador1 not in opcoes_validas or jogador2 not in opcoes_validas:
    print("Umas ou ambas jogadas invalidas! por favor, use apenas 'pedra', 'papel', 'tesoura'.")
# logica principal do jogo
elif jogador1 == jogador2:
    print("Resultado: EMPATE")
elif (jogador1 == "pedra" and jogador2 == "tesoura" or 
      jogador1 == "tesoura" and jogador2 == "papel" or
      jogador1 == "papel" and jogador2 == "pedra"): 
      print("Resultado: Jogador 1 GANHOU!")
else: 
     print("Resultado: Jogador 2 GANHOU!")

print("\n----FIM DE JOGO----")