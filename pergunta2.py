# 2.	Dada a seguinte arvore binária de palavras, faça uma função que busque nessa arvore pela palavra-chave. O output da sua função deve ser o caminho 
# até chegar no item procurado. Por exemplo, se o input de buscar for “goiaba” o output deve ser uma string “Maça -> morango -> Goiaba”.

arvore = {
    'maça': {
        'morango': {
            'goiaba': None,
            'limão': None
        },
        'pera': {
            'abacaxi': {
                'laranja': {
                    'banana': None,
                    'cebola': None
                }
            }
        }
    }
}

def buscaFruta(arvore, chave, caminho=[]):
    if not arvore:
        return None

    for fruta, filhos in arvore.items():
        caminho.append(fruta) 

        if fruta.lower() == chave.lower():  
            return ' -> '.join(caminho)  

        resultado = buscaFruta(filhos, chave, caminho)
        if resultado:
            return resultado

        caminho.pop()  

    return None

fruta = input('Insira uma fruta dentro da seguinte tabela: '
'\nMaça, Morango, Goiaba, Limão, Pera, Abacaxi, Laranja, Banana, Cebola\n')

resultado = buscaFruta(arvore, fruta)
if resultado:
    print(resultado)
else:
    print('Fruta não encontrada.')