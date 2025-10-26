class Alumno:
    def __init__(self, nombre, apellido):
        self.__nombre=nombre
        self.__apellido=apellido
    
    #FORMA 1
    @property
    def nombre(self):
        return self.__nombre
    @property.setter
    def nombre(self, value):
        self.__nombre=value
    
    #FORMA 2
    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self,value):
        self.__apellido=value

    Apellido=property(get_apellido, set_apellido)

