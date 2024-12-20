import json
from blessed import Terminal
from datos import Datos

term = Terminal()
# Esta terminal sirve para los colores.

def multiPrint(lista_texto):
    # Hacer un print formateado y colorido.
    lista = list(lista_texto)
    for i in range(len(lista)):
        if lista[i][2] == None: # Valor 2, inicialización del formato (usado para limpiar o blink)
            lista[i][2] = ""
        if lista[i][1] == None: # Valor 1, usado para los colores
            lista[i][1] = term.bright_white
        if lista[i][0] == None: # Texto del print
            lista[i][0] = "-"
        print(f"{lista[i][2]}{lista[i][1]}{lista[i][0]}{term.normal}")

def limpiar():
    return f"{term.home}{term.on_black}{term.clear}{term.home}" # Devuelve el formato usado para limpiar la pantalla

def printWarn(texto):
    multiPrint(
        [
            ["ALERTA",term.red,limpiar()],
            [str(texto),term.bright_red,None],
            ["Presiona ENTER para continuar...",term.white,term.blink],
        ]
    )
    input() # Una forma más accesible de dar una alerta. Así no copiar y pegar el mismo código demasiadas veces.

def introMenu(): # El print utilizado para el menú principal.
    multiPrint(
        [
            ["------------------",term.red,limpiar()],
            ["- Pesos Más CLI. -",term.yellow,None],
            ["*Cuida tu dinero.*",term.bright_blue,None],
            ["------------------",term.red,None],
            ["- Menú Principal -",term.bright_red,None],
            ["",None,None],
            ["1: Carga tus datos",None,None],
            ["2: Editar datos (Sueldo, gastos comunes, etc)",None,None],
            ["3: Calculadora (Gastos Hormiga e Ahorro)",None,None],
            ["4: Guarda tus datos",None,None],
            ["5: Mostrar datos",None,None],
            ["",None,None],
            ["0: Salir del programa",None,None],
            ["------------------",term.red,None],
            ["",None,None],
            ["Selecciona una opción:",term.bright_green,term.blink]
        ]
    )
    op=input()
    return op

def cargar_datos():
    try: # El try es para checkear si es que falla la carga de datos.
        with open("data.json","r") as file:
            data = json.load(file)
        return data
    except:
        printWarn("No se han podido cargar tus datos.")
        return None
    
def guardar_datos(data = Datos):
    try: # El try es para checkear si es que falla la carga de datos.
        with open("data.json","w") as file:
            json.dump(data.diccionario_completo(), file)
        return True
    except:
        printWarn("No se han podido guardar tus datos.")
        return False

def cargarDatos(): # La función principal para cargar los datos. Tiene unos prints para la interfaz de usuario.
    multiPrint([
        ["¿Desea cargar y sobreescribir los datos del programa por los datos ya guardados?",term.red,limpiar()],
        ["(S/N)",term.bright_black,None],
        ["",None,None]
    ])
    data = {}
    op=input("Ingresa una opción: ")
    if op.lower() == "s":
        data = cargar_datos()
        if data == None:
            return Datos()
        datos = Datos()
        datos.set_sueldo(data["sueldo"])
        datos.set_ahorro(data["ahorro"])
        datos.set_gastos(data["gastos"])
        multiPrint([
            ["Se han cargado los datos correctamente.",term.bright_green,limpiar()],
            ["Presiona ENTER para continuar...",term.white,term.blink]
        ])
        input()
        return datos
    else:
        printWarn("No se ha cargado ningún dato.")
    return Datos()

def guardarDatos(datos = Datos): # La función principal para guardar los datos. Tiene unos prints para la interfaz de usuario.
    multiPrint([
        ["¿Desea guardar y sobreescribir los datos locales por los del programa?",term.red,limpiar()],
        ["(S/N)",term.bright_black,None],
        ["",None,None]
    ])
    op=input("Ingresa una opción: ")
    if op.lower() == "s":
        guardar_datos(datos)
        multiPrint([
            ["Se han guardado los datos correctamente.",term.bright_green,limpiar()],
            ["Presiona ENTER para continuar...",term.white,term.blink]
        ])
        input()
    else:
        printWarn("No se ha guardado ningún dato.")

def añadir_gasto(data = Datos): # Añade un gasto a una clase Datos proporcionada.
    multiPrint([
        ["-- Añadir Gasto --",term.bright_blue,limpiar()],
        ["Para salir de este menú, escribe 'EXIT'.",None,None],
    ])
    nombre = input(term.bright_green + "Ingresa el nombre del gasto: ")
    if nombre.lower() == "exit":
        return None
    valor_gasto = ""
    while valor_gasto == "":
        try:
            valor_gasto = int(input(term.bright_green + "Ingresa el valor del gasto: "))
        except:
            printWarn("El valor del gasto no es un número. (Asegúrate de escribir el valor sólo con números.)")
            valor_gasto = ""
    prioridad = 0
    while True:
        multiPrint([
            ["-- Prioridades. --",term.bright_blue,limpiar()],
            ["",None,None],
            ["1: Prioridad alta - Emergencias sanitarias, servicios básicos, arriendo, alimentación, medicamentos",term.bright_red,None],
            ["2: Prioridad media-alta - Transporte, insumos del trabajo", term.bright_yellow, None],
            ["3: Prioridad media - Vestuario, deudas, otros insumos, aseo personal del hogar", term.bright_green, None],
            ["4: Prioridad baja - Cosas cosméticas, uso personal, ahorro", term.bright_blue, None],
            ["",None,None],
            ["Selecciona una opción:",term.bright_green,term.blink]
        ])
        prioridad = input()
        if prioridad.isnumeric():
            prioridad = int(prioridad)
            break
        else:
            printWarn("No se ha seleccionado una opción válida.")
    gasto = {
        "nombre": nombre,
        "valor_gasto": valor_gasto,
        "prioridad": prioridad
    }
    data.añadir_gasto(gasto) # Función para añadir el gasto.
    multiPrint([
        ["El gasto ha sido añadido correctamente.",term.green,limpiar()],
        ["Presiona ENTER para continuar...",term.white,term.blink]
    ])
    input()

def editar_gasto(data = Datos): # Edita un gasto, buscando el gasto por nombre.
    multiPrint([
        ["-- Menú Editar. --",term.bright_blue,limpiar()],
        ["",None,None],
        ["Por favor, ingrese el nombre del gasto a editar.",term.bright_green,term.blink]
    ])
    nombre = input()
    gasto = data.buscar_gasto(nombre)
    #-----
    if (gasto != None):
        id_gasto = data.id_gasto(nombre)
        valor_gasto = ""
        while valor_gasto == "":
            try: # El try es para checkear que sea un número lo que ingrese el usuario.
                valor_gasto = int(input(term.bright_green + "Ingresa el valor del gasto: "))
            except:
                printWarn("El valor del gasto no es un número. (Asegúrate de escribir el valor sólo con números.)")
                valor_gasto = ""
        prioridad = ""
        while True:
            multiPrint([
                ["-- Prioridades. --",term.bright_blue,limpiar()],
                ["",None,None],
                ["1: Prioridad alta - Emergencias sanitarias, servicios básicos, arriendo, alimentación, medicamentos",term.bright_red,None],
                ["2: Prioridad media-alta - Transporte, insumos del trabajo", term.bright_yellow, None],
                ["3: Prioridad media - Vestuario, deudas, otros insumos, aseo personal del hogar", term.bright_green, None],
                ["4: Prioridad baja - Cosas cosméticas, uso personal, ahorro", term.bright_blue, None],
                ["",None,None],
                ["Selecciona una opción:",term.bright_green,term.blink]
            ])
            prioridad = input()
            if prioridad.isnumeric():
                prioridad = int(prioridad)
                break
            else:
                printWarn("No se ha seleccionado una opción válida.")
        gasto = {
            "nombre": nombre,
            "valor_gasto": valor_gasto,
            "prioridad": prioridad
        }
        data.editar_gasto(id_gasto, gasto)
        multiPrint([
            ["El gasto ha sido editado correctamente.",term.green,limpiar()],
            ["Presiona ENTER para continuar...",term.white,term.blink]
        ])
        input()
def eliminar_gasto(data = Datos):
    multiPrint([
        ["- Menú Eliminar. -",term.bright_blue,limpiar()],
        ["",None,None],
        ["Por favor, ingrese el nombre del gasto a eliminar.",term.bright_green,term.blink]
    ])
    nombre = input()
    gasto = data.buscar_gasto(nombre)
    if gasto != None:
        data.eliminar_gasto(gasto)
    multiPrint([
        ["El gasto ha sido eliminado correctamente.",term.green,limpiar()],
        ["Presiona ENTER para continuar...",term.white,term.blink]
    ])
    input()
def editar_sueldo(data = Datos):
    sueldo = ""
    while True:
        multiPrint([
            ["Por favor, ingresa tu sueldo bruto actual.",term.bright_blue,limpiar()],
        ])
        sueldo = input()
        if sueldo.isnumeric():
            sueldo = int(sueldo)
            break
        else:
            printWarn("No se ha escrito un sueldo numérico.")

    data.set_sueldo(sueldo)
    multiPrint([
        ["Tu sueldo ha sido editado correctamente.",term.green,limpiar()],
        ["Presiona ENTER para continuar...",term.white,term.blink]
    ])
    input()
    return True

def editarDatos(datos):
    op="op"
    while op!="0":
        multiPrint([
            ["------------------",term.red,limpiar()],
            ["-- Menú Editar. --",term.green,None],
            ["------------------",term.red,None],
            ["",None,None],
            ["1: Editar sueldo bruto mensual",None,None],
            ["2: Añadir un gasto común",None,None],
            ["3: Editar un gasto común",None,None],
            ["4: Eliminar un gasto común",None,None],
            ["0: Salir",None,None],
            ["",None,None],
            ["------------------",term.red,None],
            ["",None,None],
            ["Selecciona una opción:",term.bright_green,term.blink]
        ])
        op=input()
        match(op):
            case "1":
                editar_sueldo(datos)
            case "2":
                añadir_gasto(datos)
            case "3":
                editar_gasto(datos)
            case "4":
                eliminar_gasto(datos)
    multiPrint([
        ["Se han editado todos los cambios correctamente.",term.green,limpiar()],
        ["Presiona ENTER para continuar...",term.white,term.blink],
    ])
    input()
    return datos

def mostrarDatos(data = Datos):
    sueldo = data.get_sueldo()
    ahorro = data.get_ahorro()
    gastos = data.get_gastos()
    multiPrint([
        ["-Todos los Gastos-",term.bright_red,limpiar()]
    ])
    for x in range(len(gastos)):
        nombre = gastos[x]["nombre"]
        valor_gasto = gastos[x]["valor_gasto"]
        prioridad = gastos[x]["prioridad"]
        multiPrint([
            [f"Gasto N°{x}", term.white, None],
            [f"Nombre del gasto: {nombre}",term.bright_green,None],
            [f"Valor del gasto: {valor_gasto}",term.bright_yellow,None],
            [f"Prioridad del gasto: {prioridad}",term.bright_blue,None],
            ["",None,None]
        ])
    multiPrint([
        [f"Sueldo: {sueldo}",term.bright_magenta,None],
        [f"Ahorro Total: {ahorro}",term.bright_cyan,None],
        ["Presiona ENTER para continuar...",term.white,term.blink]
    ])
    input()

def menu_principal():
    datos = Datos()
    op = "op"
    while op != "0":
        op = introMenu()
        match(op):
            case "0":
                multiPrint([
                    ["Gracias por usar esta aplicación.",term.green,limpiar()],
                    ["Presiona ENTER para salir...",term.white,term.blink]
                ])
                input()
            case "1":
                datos = cargarDatos()
            case "2":
                datos = editarDatos(datos)
            case "3": 
                calculadora() # Falta la calculadora de ahorro.
            case "4":
                guardarDatos(datos)
            case "5":
                mostrarDatos(datos)
            case _:
                printWarn("Selecciona una opción válida.")

menu_principal()