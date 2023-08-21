class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        return len(self.asientos)

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        for asiento in self.asientos:
            if self.registro != self.asientos[asiento].registro:
                return "Las piezas no son originales"
        return "Auto original"


class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        coloresValidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in coloresValidos:
            self.color = color


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tiposValidos = ["electrico", "gasolina"]
        if tipo in tiposValidos:
            self.tipo = tipo
