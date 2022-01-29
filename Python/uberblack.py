from car import Car

class UberBlack(Car):
    typeCarAccepted = [] # Le indico que el primer atributo es un arreglo
    seatsMaterial = []

    def __init__(self, license, driver, typeCarAccepted, seatsMaterial):
        super.__init__(license,driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial
