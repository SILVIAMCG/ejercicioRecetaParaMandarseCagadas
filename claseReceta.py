#Menu de una clase receta dentro de la cual habra una lista de ingredientes. Cada
#ingrediente tendra los siguientes atributos:
#nombre
#cantidad
#unidad de medida

#La clase receta ademas de contener un menu y una lista de ingredientes, debe tener
#un nombre y una lista de pasos asi como los siguientes comportamientos:
#agregar ingrediente
#consultar ingrediente
#agregar paso
#consultar pasos

#atributos
#ingredientes, pasos, nombre

#comportamientos
#menu
#agregar ingrediente
#consultar ingredientes
#agregar y consultar pasos

from claseIngrediente import Ingrediente
import os

class Receta:
    OPC_AGREGAR_INGREDIENTE = 1
    OPC_CONSULTAR_INGREDIENTES = 2
    OPC_AGREGAR_PASO = 3
    OPC_CONSULTAR_PASO = 4
    OPC_SALIR = 0

    def __init__(self, nombre=""):
        self._nombre = nombre
        self._ingredientes = []
        self._pasos =[]

    def __str__(self):
        s= f"                          {self.nombre}\n"
        #se van sumando la informacion
        s += "Ingredientes: \n"
        #para cada ingrediente en la lista, imprimirlos
        for ingrediente in self.ingredientes:
            s += f"{ingrediente}\n"
        s += "\nPasos: \n"
        for i,paso in enumerate(self.pasos):
            s += f"{i+1}. {paso}\n"
        return s
            

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,valor):
        self._nombre = valor

    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def ingredientes(self):
        return self._ingredientes

    @ingredientes.setter
    def ingredientes(self,valor):
        self._ingredientes = valor

    @ingredientes.deleter
    def ingredientes(self):
        del self._ingredientes

    @property
    def pasos(self):
        return self._pasos

    @pasos.setter
    def pasos(self,valor):
        self._pasos = valor

    @pasos.deleter
    def pasos(self):
        del self._pasos


    #comportamientos
    def menu(self):
        continuar=True
        while continuar:
            #esto limpia la pantalla
            os.system('cls')

            #imprimir el menu
            print(f'''           {self.nombre}
    {self.OPC_AGREGAR_INGREDIENTE}) Agregar ingrediente
    {self.OPC_CONSULTAR_INGREDIENTES}) Consultar ingredientes
    {self.OPC_AGREGAR_PASO}) Agregar paso
    {self.OPC_CONSULTAR_PASO}) Consultar pasos
    {self.OPC_SALIR}) Salir
    ''')
            #seleccionar opciones del menu, llamando a sus respectivos metodos
            opc=int(input("Selecciona una opcion: "))
            if opc == self.OPC_AGREGAR_INGREDIENTE:
                self.agregarIngrediente()
            elif opc==self.OPC_CONSULTAR_INGREDIENTES:
                self.consultarIngredientes()
            elif opc==self.OPC_AGREGAR_PASO:
                self.agregarPaso()
            elif opc==self.OPC_CONSULTAR_PASO:
                self.consultar_pasos()
            elif opc==self.OPC_SALIR:
                continuar=False
            else:
                print("Opcion no valida...")
            input("Presiona enter para continuar")

        print("Nos vemos")
            

    def agregarIngrediente(self):
        #hacer un ciclo por si se desea agregar otro ingrediente
        continuar=True
        while continuar:
            os.system("cls")
            #encabezado
            print("                      Agregar Ingrediente")
            #empezar a pedir los datos
            nombre = input("Nombre: ")
            #la cantidad debe ser validada para que no se ingresen numeros negativos
            cantidad=-1
            while cantidad <=0:
                cantidad= input("Cantidad: ")
                #si hay un error se mantiene el ciclo
                try:
                    cantidad = float(cantidad)
                except:
                    cantidad = 0

            #pedir la unidad de medida
            unidad = input("Unidad de medida: ")

            #crear ingrediente, llamando a la clase ingrediente
            ingrediente = Ingrediente(nombre,cantidad,unidad)
            #agregar ingrediente a la lista
            self.ingredientes.append(ingrediente)
            #preguntar si se desea agregar otro ingrediente
            respuesta=input("¿Desea agregar otro ingrediente? (s/n)")
            if respuesta != "s" and respuesta!= "S":
                continuar=False
                        

    def consultarIngredientes(self):
        os.system("cls")
        print("                          Ingredientes")
        #si hay ingredientes que los muestre
        if len(self.ingredientes)==0:
            print("No hay ingredientes registrados")
        else:
            #ciclo para mostrar
            for ingrediente in self.ingredientes:
                print(f"{ingrediente}")

    def agregarPaso(self):
        continuar=True
        while continuar:
            os.system("cls")
            print("                      Agregar paso")
            paso= input("Paso: ")
            self.pasos.append(paso)
            respuesta=input("Deseas agregar otro paso? (s/n)")
            if respuesta != "s" and respuesta !="S":
                continuar=False

    def consultar_pasos(self):
        os.system("cls")
        print("                           Pasos")
        #ver si hay pasos registrados
        if len(self.pasos)==0:
            print("No hay pasos registrados")
        else:
            #listar los pasos con enumerate
            for i,paso in enumerate(self.pasos):
                print(f"{i+1}. {paso}")









    










