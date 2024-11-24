from Sandwich import Sandwich

class AdicionalDecorator(Sandwich):
    def __init__(self, sandwich):
        self.sandwich = sandwich

    def getDescripcion(self):
        return self.sandwich.getDescripcion()

    def getPrecio(self):
        return self.sandwich.getPrecio()


# Decoradores concretos para los adicionales

class Aguacate(AdicionalDecorator):
    def __init__(self, sandwich):
        super().__init__(sandwich)
        # Condiciones basadas en el tamaño del sandwich
        self.precio_adicional = 1.5 if sandwich.getTamaño() == 15 else 2.0

    def getDescripcion(self):
        return f"{self.sandwich.getDescripcion()} + Aguacate"

    def getPrecio(self):
        return self.sandwich.getPrecio() + self.precio_adicional


class DobleProteina(AdicionalDecorator):
    def __init__(self, sandwich):
        super().__init__(sandwich)
        # Precios basados en el tamaño del sandwich
        self.precio_adicional = 4.5 if sandwich.getTamaño() == 15 else 6.0

    def getDescripcion(self):
        return f"{self.sandwich.getDescripcion()} + Doble Proteína"

    def getPrecio(self):
        return self.sandwich.getPrecio() + self.precio_adicional


class Hongos(AdicionalDecorator):
    def __init__(self, sandwich):
        super().__init__(sandwich)
        # Precios basados en el tamaño del sandwich
        self.precio_adicional = 2.0 if sandwich.getTamaño() == 15 else 3.0

    def getDescripcion(self):
        return f"{self.sandwich.getDescripcion()} + Hongos"

    def getPrecio(self):
        return self.sandwich.getPrecio() + self.precio_adicional


class Refresco(AdicionalDecorator):
    def __init__(self, sandwich):
        super().__init__(sandwich)
        # Precio fijo para el refresco
        self.precio_adicional = 1.0

    def getDescripcion(self):
        return f"{self.sandwich.getDescripcion()} + Refresco"

    def getPrecio(self):
        return self.sandwich.getPrecio() + self.precio_adicional


class Sopa(AdicionalDecorator):
    def __init__(self, sandwich):
        super().__init__(sandwich)
        # Precios basados en el tamaño del sandwich
        self.precio_adicional = 3.5 if sandwich.getTamaño() == 15 else 4.2

    def getDescripcion(self):
        return f"{self.sandwich.getDescripcion()} + Sopa"

    def getPrecio(self):
        return self.sandwich.getPrecio() + self.precio_adicional


class Postre(AdicionalDecorator):
    def __init__(self, sandwich):
        super().__init__(sandwich)
        # Precios basados en el tamaño del sandwich
        self.precio_adicional = 2.5 if sandwich.getTamaño() == 15 else 3.0

    def getDescripcion(self):
        return f"{self.sandwich.getDescripcion()} + Postre"

    def getPrecio(self):
        return self.sandwich.getPrecio() + self.precio_adicional
