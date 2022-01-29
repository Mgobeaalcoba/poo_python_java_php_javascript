from car2 import Car # Importo la clase Car de mi file car para poder crear objetos concretos
from account2 import Account # Lo mismo hago con Account
from uberx import UberX # Lo mismo hago con UberX

if __name__ == "__main__":
    print("Hola Mundo")

    """ 
    Acá voy a crear objetos pero con un metodo constructor. Para ello voy a usar: __init__ y self
    El método constructor en Python forma parte de esta familia de métodos y como aprendimos en 
    la clase anterior lo declaramos usando __init__.
    usamos la palabra clave self, esta es muy parecida a lo que venimos trabajando a otros lenguajes
    con this. Y como su nombre lo dice hace referencia a los datos que componen la clase
    """

    car = Car("AMS324", Account("Mariano Gobea","AND0044")) #Creo mi primer objeto car usando la clase car que ya defini en mi otro file
    # car.license = "AMS234" #Defino los atributos de objeto.
    # car.driver = "Andres Herrera" # ""
    # Al construir el objeto desde el metodo constructor, los atributos se pasan mediante los parametros
    # de la clase y ya no de forma individual. 
    print(vars(car)) # El metodo vars se usa para imprimir todos los atributos del objeto creado
    print(vars(car.driver)) # Para imprimir los datos del conductor. 

    car2 = Car("JYC798", Account("Lisandro Raccio","CAPO123"))
    # car2.license = "QWE567"
    # car2.driver = "Matha"
    print(vars(car2))
    print(vars(car2.driver))

    car3 = UberX("ETX983",Account("Nicole Fernandez","A37971987"),"Ford","Ka")
    print(car3.license)
    print(car3.driver.name)
    print(car3.driver.document)
    print(car3.brand)
    print(car3.model)

    """
    Con esta forma de imprimir, imprimo directamente los valores que asumen cada atributo de un objeto
    """
