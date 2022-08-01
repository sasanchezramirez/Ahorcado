from ntpath import join
from random import randint
import os

def bring_line():
    list_lines = []
    line_number = randint(0,169)
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            list_lines.append(line)
    return list_lines[line_number] 
    


def run():
    palabra = bring_line()
    palabra = list(palabra)
    palabra.pop(len(palabra)-1)
    print(palabra)
    letras = []
    for index, letra in enumerate(palabra):
        letras.append(letra)
    letras.pop(len(letras)-1)
    palabra_en_juego = "_"*len(palabra)
    palabra_en_juego = list(palabra_en_juego)
 

    
    
    while palabra_en_juego != palabra:
        print(palabra_en_juego, type(palabra_en_juego))
        palabra_en_juego = list(palabra_en_juego)
        user_input = input("ingrese una letra")
        if user_input in palabra:           
            for index, letra in enumerate(palabra):
                if letra == user_input:
                    palabra_en_juego[index] = letra
            palabra_en_juego = "".join(palabra_en_juego)
            palabra_en_juego = list(palabra_en_juego)
        os.system("cls")
    return palabra_en_juego
    





if __name__=="__main__":
    run()