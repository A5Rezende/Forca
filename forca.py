import random
from palavras_forca import palavras_forca
import string

def validar_palavra(palavras_forca):

    palavra = random.choice(palavras_forca)
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras_forca)

    return palavra.upper()

def forca():
    palavra = validar_palavra(palavras_forca)
    letras_palavra = set(palavra)
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()
    vidas = 7

    while len(letras_palavra) > 0 and vidas > 0:

        print("Vidas : {}".format(vidas))
        print('Você já usou as letras : ', ' '.join(letras_usadas))

        palavra_encontrada = [letra if letra in letras_usadas else '-' for letra in palavra]
        print('palavra : ', ' '.join(palavra_encontrada))

        tentativa = input("Escolha uma letra: ").upper()
        if tentativa in alfabeto - letras_usadas:
            letras_usadas.add(tentativa)
            if tentativa in letras_palavra:
                letras_palavra.remove(tentativa)

            else:
                vidas = vidas - 1

        else:
            print("tentativa invalida")
            vidas = vidas - 1

    print("--------------")
    palavra_encontrada = [letra if letra in letras_usadas else '-' for letra in palavra]
    print('palavra : ', ' '.join(palavra_encontrada))
    if vidas == 0:
        print("Suas vidas acabaram")

forca()