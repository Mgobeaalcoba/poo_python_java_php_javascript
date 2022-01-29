from car import Car

class UberPool(Car): #Declaro la herencia de Car y agrego los atributos
# que no hereda de Car debajo
    brand = str
    model = str

    def __init__(self, license, driver, brand, model):
        super.__init__(license,driver) # Con super le paso a la clase
        # padre los parametros que le corresponden para iniciar un
        # objeto UberX
        self.brand = brand
        self.model = model

"""
Usando el metodo super es como se declara una clase hija de otra en 
Python al igual que en Java
"""
