class DimensionError(Exception):
    """
    Excepción personalizada para manejar errores relacionados con dimensiones fuera del rango permitido.

    Atributos:
        mensaje (str): Mensaje de error.
        dimension (int, opcional): Valor de la dimensión que causó el error.
        maximo (int, opcional): Valor máximo permitido para la dimensión.
    """
    
    def __init__(self, mensaje, dimension=None, maximo=None):
        """
        Inicializa la excepción con un mensaje, una dimensión opcional y un valor máximo opcional.

        Args:
            mensaje (str): Mensaje de error.
            dimension (int, opcional): Valor de la dimensión que causó el error.
            maximo (int, opcional): Valor máximo permitido para la dimensión.
        """
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo
    
    def __str__(self):
        """
        Retorna una representación en cadena del mensaje de error, incluyendo detalles adicionales si están disponibles.

        Returns:
            str: Mensaje de error detallado.
        """
        if self.dimension is not None and self.maximo is not None:
            return f"{self.args[0]} - Dimension: {self.dimension}, Maximo permitido: {self.maximo}"
        elif self.dimension is not None:
            return f"{self.args[0]} - Dimension: {self.dimension}"
        elif self.maximo is not None:
            return f"{self.args[0]} - Maximo permitido: {self.maximo}"
        return super().__str__()
