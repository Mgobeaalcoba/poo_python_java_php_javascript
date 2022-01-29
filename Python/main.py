from car import Car # Importo la clase Car de mi file car para poder crear objetos concretos

if __name__ == "__main__":
    print("Hola Mundo")

    """ 
    Aca estoy creando objetos desde las clases pero sin usar un metodo constructor. 
    """

    car = Car() #Creo mi primer objeto car usando la clase car que ya defini en mi otro file
    car.license = "AMS234" #Defino los atributos de objeto.
    car.driver = "Andres Herrera" # ""
    print(vars(car)) # El metodo vars se usa para imprimir todos los atributos del objeto creado

    car2 = Car()
    car2.license = "QWE567"
    car2.driver = "Matha"
    print(vars(car2))