from error import DimensionError

class Foto:
    """
    Clase para representar una foto en una galería con ancho y alto específicos.

    Atributos:
        MAX (int): Valor máximo permitido para ancho y alto.
        _ancho (int): Ancho de la foto.
        _alto (int): Alto de la foto.
    """

    MAX = 1000  # Valor máximo para ancho y alto

    def __init__(self, ancho, alto):
        """
        Inicializa una instancia de Foto con ancho y alto.

        Args:
            ancho (int): Ancho de la foto.
            alto (int): Alto de la foto.
        """
        self.ancho = ancho
        self.alto = alto
    
    @property
    def ancho(self):
        """
        Obtiene el ancho de la foto.

        Returns:
            int: Ancho de la foto.
        """
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        """
        Establece el ancho de la foto, lanzando una excepción si el valor no está en el rango permitido.

        Args:
            valor (int): Nuevo valor para el ancho.

        Raises:
            DimensionError: Si el valor está fuera del rango permitido (menor a 1 o mayor al máximo permitido).
        """
        if valor < 1 or valor > Foto.MAX:
            raise DimensionError("Ancho fuera del rango permitido", dimension=valor, maximo=Foto.MAX)
        self._ancho = valor
    
    @property
    def alto(self):
        """
        Obtiene el alto de la foto.

        Returns:
            int: Alto de la foto.
        """
        return self._alto

    @alto.setter
    def alto(self, valor):
        """
        Establece el alto de la foto, lanzando una excepción si el valor no está en el rango permitido.

        Args:
            valor (int): Nuevo valor para el alto.

        Raises:
            DimensionError: Si el valor está fuera del rango permitido (menor a 1 o mayor al máximo permitido).
        """
        if valor < 1 or valor > Foto.MAX:
            raise DimensionError("Alto fuera del rango permitido", dimension=valor, maximo=Foto.MAX)
        self._alto = valor
