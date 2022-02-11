class Ingrediente:
    def __init__(self,nombre="",cantidad=None,unidadMedida=""):
        #estos argumentos se asignan a los atributos
        self._nombre=nombre
        self._cantidad=cantidad
        self._unidad=unidadMedida

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,valor):
        self._nombre=valor

    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self,valor):
        self._cantidad=valor

    @cantidad.deleter
    def cantidad(self):
        del self._cantidad

    @property
    def unidadMedida(self):
        return self._unidad

    @unidadMedida.setter
    def unidadMedida(self,valor):
        self._unidad=valor

    @unidadMedida.deleter
    def unidadMedida(self):
        del self._unidad



    def __str__(self):
        return f'''Nombre: {self.nombre} Cantidad: {self.cantidad}{self.unidadMedida}'''












        
