class Datos:
    def __init__(self):
        self.__sueldo = 0
        self.__gastos = []
        self.__ahorro = 0

    def get_sueldo(self):
        return self.__sueldo
    
    def get_gastos(self):
        return self.__gastos
    
    def get_ahorro(self):
        return self.__ahorro
    
    def añadir_gasto(self, gasto):
        self.__gastos.append(gasto)

    def editar_gasto(self, id, gasto):
        self.__gastos[id] = gasto

    def eliminar_gasto(self, gasto):
        self.__gastos.remove(gasto)

    def buscar_gasto(self, nombre):
        for x in range(len(self.__gastos)):
            if (self.__gastos[x]["nombre"] == nombre):
                return self.__gastos[x]
        return None
    
    def id_gasto(self, nombre):
        for x in range(len(self.__gastos)):
            if (self.__gastos[x]["nombre"] == nombre):
                return x
        return None
    
    def set_gastos(self, gastos):
        self.__gastos = gastos

    def set_sueldo(self, sueldo):
        self.__sueldo = sueldo

    def set_ahorro(self, ahorro):
        self.__ahorro = ahorro
    
    def diccionario_completo(self):
        diccionario = {
            "sueldo": self.__sueldo,
            "gastos": self.__gastos,
            "ahorro": self.__ahorro
        }
        return diccionario
    
    def __str__(self):
        return f"Sueldo bruto: {self.__sueldo}\nAhorro actual:{self.__ahorro}"