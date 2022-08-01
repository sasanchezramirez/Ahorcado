from random import randint

def bring_line():
    list_lines = []
    line_number = randint(0,169)
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            list_lines.append(line)
    return list_lines[line_number] 

def comparision (palabra):
    letras = []
    for index, letra in enumerate(palabra):
        letras.append(letra)
    letras.pop(len(letras)-1)
    print("_ "*len(letras))

    user_input = input("ingrese una letra")
    for index, letra in enumerate(palabra):
        if user_input == letra:
            print("hay un match en ", index)
    return letras    
    # num_guiones = list(enumerate(palabra))
    # for letra in num_guiones:
    #     return num_guiones

def run():
    palabra = bring_line()
    num_guiones = comparision(palabra)
    print(num_guiones)






if __name__=="__main__":
    run()