from payment2 import Payment
from datetime import date

class Tarjeta(Payment):
    franquicia = str
    fechavencimiento = date.today()
    cvv = int

    def __init__(self, id,franquicia, fechavencimiento, cvv):
        super().__init__(id)
        self.franquicia = franquicia
        self.fechavencimiento = fechavencimiento
        self.cvv = cvv
