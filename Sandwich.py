import uuid

class Sandwich:
    def __init__(self, tipo, tamaño):
        """
        Inicializa el sándwich con el tipo y tamaño especificado.
        """
        self.tipo = tipo
        self.tamaño = tamaño  # Tamaño en cm: 15 o 30
        self.precio_base = 0.0

    def getDescripcion(self):
        """
        Devuelve la descripción del sándwich.
        """
        return f"{self.tipo} ({self.tamaño} cm)"

    def getPrecio(self):
        """
        Devuelve el precio base del sándwich.
        """
        return self.precio_base

    def getTamaño(self):
        """
        Devuelve el tamaño del sándwich (15 o 30).
        """
        return self.tamaño


class Pavo(Sandwich):
    def __init__(self, tamaño):
        super().__init__("Pavo", tamaño)
        self.precio_base = 12.0 if tamaño == 15 else 16.0


class Pollo(Sandwich):
    def __init__(self, tamaño):
        super().__init__("Pollo", tamaño)
        self.precio_base = 12.0 if tamaño == 15 else 16.0


class Beef(Sandwich):
    def __init__(self, tamaño):
        super().__init__("Beef", tamaño)
        self.precio_base = 14.0 if tamaño == 15 else 18.0


class Italiano(Sandwich):
    def __init__(self, tamaño):
        super().__init__("Italiano", tamaño)
        self.precio_base = 13.0 if tamaño == 15 else 17.0


class Veggie(Sandwich):
    def __init__(self, tamaño):
        super().__init__("Veggie", tamaño)
        self.precio_base = 10.0 if tamaño == 15 else 14.0


class Atun(Sandwich):
    def __init__(self, tamaño):
        super().__init__("Atún", tamaño)
        self.precio_base = 12.0 if tamaño == 15 else 16.0


class Combo(Sandwich):
    def __init__(self, tipo1, tipo2, tamaño):
        """
        Un "Combo" es una combinación de dos tipos de sándwiches con el mismo tamaño.
        """
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.tamaño = tamaño
        self.precio_base = self.calcular_precio(tipo1, tipo2, tamaño)
    def calcular_precio(self, tipo1, tipo2, tamaño):
        precio1 = Sandwich(tipo1, tamaño).getPrecio()
        precio2 = Sandwich(tipo2, tamaño).getPrecio()
        return precio1 + precio2

    def getDescripcion(self):
        return f"Combo: {self.tipo1} + {self.tipo2} ({self.tamaño} cm)"

    def getPrecio(self):
        return self.precio_base