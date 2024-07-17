# 1.	Dado o Array de inteiros abaixo, ordene-o de tal forma que os números “1” estejam à esquerda. Os itens devem ser modificados no lugar, ou seja, você não ira 
# trocar posições e sim colocar os números “1” no inicio do Array. [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]

lista = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]

indice = 0

for i in range(len(lista)):
    if lista[i] == 1:
        lista[indice] = 1
        indice += 1

for i in range(len(lista)):
    if lista[i] != 1:
        lista[indice] = lista[i]
        indice += 1

print(lista)