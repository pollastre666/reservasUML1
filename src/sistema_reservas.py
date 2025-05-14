class Sala:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

class Reserva:
    def __init__(self, fecha, hora_inicio, hora_fin, usuario, sala):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.usuario = usuario
        self.sala = sala

class ClienteVIP(Usuario):
    def __init__(self, nombre, correo, puntos):
        super().__init__(nombre, correo)
        self.puntos = puntos
