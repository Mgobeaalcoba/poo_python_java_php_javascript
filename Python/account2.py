class Account:
    id          = int
    name        = str
    document    = str
    email       = str
    password    = str

    def __init__(self, name, document): # Los parametros que siguen a "Self" son los datos obligatorios para instanciar
    # un objeto de tipo Account
        self.name = name
        self.document = document

"""
Es importante que los metodos constructores queden adentro de las clases y no por fuera.
Ya que sino no se ejecutaran con éxito. 
"""
