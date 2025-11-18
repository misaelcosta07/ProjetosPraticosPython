def calculadora(lista):
    n1,n2 = lista
    soma= n1+n2
    sub= n1-n2
    mult= n1*n2
    if n2!=0: 
        div = n1/n2
    else:
        div = None

    print("O resultado das operaçoes:")
    print(f"soma:{soma}")
    print(f"subtraçao:{sub}")
    print(f"multiplicaçao:{mult}")
    if div is None:
        print("Divisao: impossivel (divisao por zero)")
    else:
        print(f"divisao:{div}")


#entrada de dados para a funca, atraves de um lista para receber os numeros 
n1 = float(input("Digite o primeiro numero:\n"))
n2 = float(input("Digite o segundo numero:\n"))
# mostrar  os valores escolhidos para compor a lista
lista_num=[n1,n2]
print(lista_num)
#chamei a funçao 
calculadora(lista_num)