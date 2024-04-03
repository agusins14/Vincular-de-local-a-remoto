class Cliente:
    def __init__(self, nombre, identificador, email):
        self.nombre = nombre
        self.identificador = identificador
        self.email = email
        
    def __str__(self):
        return f"Cliente: {self.nombre}"


class Persona(Cliente):

    def __init__(self, nombre, identificador, edad, email):
        super().__init__(nombre, identificador, email)
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre} - Documento: {self.identificador}"


class Empresa(Cliente):

    def __init__(self, nombre, identificador, email):
        super().__init__(nombre, identificador, email)

    def __str__(self):
        return f"Empresa: {self.nombre} - Código: {self.identificador}"