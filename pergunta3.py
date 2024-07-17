# 3.	Dado o array de números inteiros [1, 15, 2, 7, 2, 5, 7, 1, 4] crie uma função que recebe um argumento X e retorne true ou false caso haja no array uma 
# combinação de soma entre dois números que resulte no input X. Exemplo: Se X=2, a função deve retornar true pois existem dois números 1 dentro do array 1+1 = 2. 
# Caso X=1231 a função deve retornar false pois não existe uma combina de dois números capazes de somar 1231.

lista = [1, 15, 2, 7, 2, 5, 7, 1, 4]

def verificaSoma(lista, X):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == X:
                return True
    return False

X = int(input('Insira um número: '))
resultado = verificaSoma(lista, X)
print(resultado)
