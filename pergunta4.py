# 4.	Dado o array [9, 2, 3, 1, 4] encontre todos os números que estão faltando para completar o intervalo 0 a n, onde n é o maior número dentro do array. 
# Adicione os números faltando dentro do array. 

lista = [9, 2, 3, 1, 4]

maior_numero = max(lista)

todos_os_numeros = set(range(maior_numero + 1))

numeros_presentes = set(lista)

numeros_faltando = todos_os_numeros - numeros_presentes

lista.extend(numeros_faltando)

lista.sort()

print("Lista completa:", lista)
