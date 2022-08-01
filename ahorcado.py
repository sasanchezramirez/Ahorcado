from random import randint

def bring_line():
    list_lines = []
    line_number = randint(0,169)
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            list_lines.append(line)
    return list_lines[line_number] 

def guiones (palabra):
    num_guiones = list(enumerate(palabra))
    return num_guiones

def run():
    palabra = bring_line()
    num_guiones = guiones(palabra)
    print(num_guiones)






if __name__=="__main__":
    run()