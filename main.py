from foto import Foto
from error import DimensionError

def main():
    """
    Función principal para ejecutar ejemplos de uso de la clase Foto y manejo de excepciones.
    """
    print("Ejemplos de uso de la clase Foto")

    # Crear una foto con dimensiones válidas
    try:
        foto_valida = Foto(ancho=500, alto=600)
        print(f"Foto creada con éxito: Ancho = {foto_valida.ancho}, Alto = {foto_valida.alto}")
    except DimensionError as e:
        print(f"Error al crear la foto: {e}")

    # Intentar crear una foto con ancho inválido
    try:
        foto_invalida_ancho = Foto(ancho=1500, alto=600)  # Esto lanzará una excepción
    except DimensionError as e:
        print(f"Error al crear la foto con ancho inválido: {e}")

    # Intentar crear una foto con alto inválido
    try:
        foto_invalida_alto = Foto(ancho=500, alto=-10)  # Esto lanzará una excepción
    except DimensionError as e:
        print(f"Error al crear la foto con alto inválido: {e}")

    # Modificar una foto existente con un valor inválido
    try:
        foto_valida.ancho = 1200  # Esto lanzará una excepción
    except DimensionError as e:
        print(f"Error al modificar el ancho de la foto: {e}")

    try:
        foto_valida.alto = 0  # Esto lanzará una excepción
    except DimensionError as e:
        print(f"Error al modificar el alto de la foto: {e}")

if __name__ == "__main__":
    main()
