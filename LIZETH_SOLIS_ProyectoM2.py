# Función para verificar la longitud de una palabra
def verificar_longitud_palabra(palabra):
    # Obtener la longitud de la palabra
    longitud = len(palabra)
    
    # Verificar si la longitud está entre 4 y 8 letras
    if 4 <= longitud <= 8:
        print("La palabra es correcta.")
    # Si la longitud es menor a 4 letras
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    # Si la longitud es mayor a 8 letras
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")

# Solicitar al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")

# Llamar a la función para verificar la longitud de la palabra
verificar_longitud_palabra(palabra)

# Programa para encontrar el cuadrante de un punto en el plano cartesiano

# Solicitar al usuario que ingrese las coordenadas X y Y
x = int(input("Ingrese X: "))
y = int(input("Ingrese Y: "))

# Verificar que ninguna coordenada sea 0
if x == 0 or y == 0:
    print("Las coordenadas no deben ser 0. Ingrese un numero diferente a 0")
else:
    # Determinar en qué cuadrante se encuentra el punto
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV.")