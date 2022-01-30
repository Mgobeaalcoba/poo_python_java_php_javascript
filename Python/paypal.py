from payment2 import Payment

class Paypal(Payment):
    referencia = str
    sucursal = str

    def __init__(self, id, referencia, sucursal):
        super().__init__(id)
        self.referencia = referencia
        self.sucursal = sucursal
