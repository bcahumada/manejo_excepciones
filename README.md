# Desafío - Manejo de Excepciones

## Descripción

En este desafío, se desarrolla una aplicación de galería de fotos que incluye manejo de excepciones personalizado para validar las dimensiones de las fotos. La aplicación debe asegurarse de que el ancho y el alto de una foto estén dentro de un rango válido y debe lanzar una excepción personalizada si se intenta establecer valores fuera de los límites permitidos.

## Requerimientos

1. **Crear la excepción `DimensionError`**:
    - Definir una excepción personalizada para manejar errores relacionados con dimensiones fuera del rango permitido.
    - La excepción debe tener un mensaje, una dimensión, y un valor máximo opcional.
    - Sobrecargar el método `__str__` para proporcionar mensajes de error detallados.

2. **Modificar la clase `Foto`**:
    - Implementar los métodos setter de los atributos `ancho` y `alto` para lanzar una excepción `DimensionError` cuando los valores no sean válidos.
    - Los valores válidos deben estar entre 1 y un valor máximo determinado por la clase.

## Archivos del Proyecto

### `error.py`

Define la excepción personalizada `DimensionError`.

```python
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
```

## Instrucciones para Ejecutar

Clona el repositorio:

```bash

git clone <URL_DEL_REPOSITORIO>
```

Instala las dependencias (si es necesario):

```bash

pip install -r requirements.txt
```

Ejecuta el código:

Para probar la funcionalidad de la clase Foto, crea instancias de la clase en un script o consola interactiva, e intenta asignar valores válidos e inválidos para verificar el manejo de excepciones.

### Ejemplos

**Crear una foto válida**

```python

from foto import Foto

foto = Foto(ancho=500, alto=600)
print(foto.ancho)  # Salida: 500
print(foto.alto)   # Salida: 600
```


**Crear una foto con dimensiones inválidas**

```python

from foto import Foto
from error import DimensionError

try:
    foto = Foto(ancho=1500, alto=600)  # Esto lanzará una excepción
except DimensionError as e:
    print(e)
```


## Requisitos

- Python 3.x

## Autor

Bárbara HA