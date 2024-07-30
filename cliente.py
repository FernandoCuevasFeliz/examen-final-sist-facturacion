class Cliente:
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        return f"Cliente ID: {self.id}, Nombre: {self.nombre}, Dirección: {self.direccion}"
