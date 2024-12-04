import json
from blessed import Terminal

term = Terminal()

def multiPrint(lista_texto):
    lista = list(lista_texto)
    for i in range(len(lista)):
        if lista[i][2] == None:
            lista[i][2] = ""
        if lista[i][1] == None:
            lista[i][1] = term.white
        if lista[i][0] == None:
            lista[i][0] = "-"
        print(f"{lista[i][2]}{lista[i][1]}{lista[i][0]}{term.normal}")

def limpiar():
    return f"{term.home}{term.on_black}{term.clear_eos}"

def printWarn(texto):
    multiPrint(
        [
            ["ATENCIÓN",term.red,limpiar()],
            [str(texto),term.bright_red,None],
            ["Presiona ENTER para continuar...",term.white,term.blink],
        ]
    )
    input()

def introMenu():
    multiPrint(
        [
            ["------------------",term.red,limpiar()],
            ["- Pesos Más CLI. -",term.yellow,None],
            ["*Cuida tu dinero.*",term.bright_blue,None],
            ["------------------",term.red,None],
            ["- Menú Principal -",term.bright_red,None],
            ["",None,None],
            ["1: Carga tus datos",None,None],
            ["2: Editar datos",None,None],
            ["3: Calculadora (Gastos Hormiga)",None,None],
            ["4: Guarda tus datos",None,None],
            ["------------------",term.red,None],
            ["",None,None],
            ["Selecciona una opción:",term.bright_green,term.blink]
        ]
    )
    op=input()
    return op

def menu_principal():
    op = -1
    while op != 0:
        op = introMenu()
        match(op):
            case 1:
                cargar_datos()
            case 2:
                editar_datos()
            case 3: 
                calculadora()
            case 4:
                guardar_datos()
            case _:
                printWarn("Selecciona una opción válida.")

menu_principal()