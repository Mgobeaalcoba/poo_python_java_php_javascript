from os import name
from xml.dom.minidom import Document
from account2 import Account

class Car:
    id = int
    license = str
    driver = Account("","")
    passegenger = int

    def __init__(self, license, driver):
        self.license = license
        self.driver = driver

"""
Es importante que los metodos constructores queden adentro de las clases y no por fuera.
Ya que sino no se ejecutaran con éxito. 
"""