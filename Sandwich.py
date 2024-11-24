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
        super().__init__("Combo", tamaño)
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.descuento = 10  # Descuento en porcentaje para el combo
        self.precio_base = self.calcularPrecioCombo()

    def calcularPrecioCombo(self):
        """
        Calcula el precio del combo sumando los precios de los sándwiches individuales
        y aplicando un descuento.
        """
        # Creamos instancias de los sándwiches para calcular el precio combinado
        sandwich1 = self.crearSandwich(self.tipo1, self.tamaño)
        sandwich2 = self.crearSandwich(self.tipo2, self.tamaño)

        # Precio combinado con descuento
        precio_combinado = sandwich1.getPrecio() + sandwich2.getPrecio()
        return precio_combinado * (1 - self.descuento / 100)

    def crearSandwich(self, tipo, tamaño):
        """
        Crea una instancia de sándwich según el tipo y tamaño especificados.
        """
        sandwich_clases = {
            "Pavo": Pavo,
            "Pollo": Pollo,
            "Beef": Beef,
            "Italiano": Italiano,
            "Veggie": Veggie,
            "Atún": Atun,
        }

        if tipo not in sandwich_clases:
            raise ValueError(f"Tipo de sándwich no reconocido: {tipo}")

        return sandwich_clases[tipo](tamaño)

    def getDescripcion(self):
        """
        Devuelve la descripción del combo.
        """
        return f"Combo: {self.tipo1} + {self.tipo2} ({self.tamaño} cm)"

    def getPrecio(self):
        """
        Devuelve el precio final del combo con descuento.
        """
        return self.precio_base
