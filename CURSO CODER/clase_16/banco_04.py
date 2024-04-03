from entidades_04 import Persona, Empresa, Cliente

class Banco:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = {}
        
    def __str__(self):
        return f"Banco {self.nombre}"
    
    def crear_cuenta(self, cl:Cliente):
        self.cuentas[cl.nombre] = 0
        
    def mostrar_cuentas(self):
        texto = ""
        for x, y in self.cuentas.items():
            cuenta = f"La cuenta de {x} tiene saldo: {y}"
            texto += cuenta + "<br>"
            
        return texto
    
    def consultar_cuenta(self, cl:Cliente):
        pass
    
    def depositar(self, cl:Cliente, monto:int):
        self.cuentas[cl.nombre] += monto
  
# MRO (Method Order Resolution): Sirve par consultar el orden de búsqueda de los métodos
print(Persona.mro())