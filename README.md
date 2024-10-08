Abrir archivo LIZETH_SOLIS_ProyectoM2.py 
En el archivo LIZETH_SOLIS_ProyectoM2.py se encuetran dos programas:
## Programa 1: Verificar Longitud de Palabra

### Descripción
Este programa verifica la longitud de una palabra ingresada por el usuario y determina si es correcta según los siguientes criterios:
- La palabra debe tener entre 4 y 8 letras.
- Si tiene menos de 4 letras, se indica cuántas letras faltan.
- Si tiene más de 8 letras, se indica cuántas letras sobran.

## Programa 2: Encuentra el Cuadrante
Descripción
Este programa determina en cuál de los cuatro cuadrantes del plano cartesiano se encuentra un punto basado en sus coordenadas (X, Y). El programa verifica que ninguna coordenada sea 0.
### Instrucciones
1. Ejecutar el programa.
2. Ingresa una palabra cuando se te solicite.
3. El programa te dirá si la palabra es correcta o te indicará si faltan o sobran letras.
4. Ingresa las coordenadas X y Y cuando se te solicite.
5. El programa te dirá en cuál cuadrante se encuentra el punto.


### Codigo Python:

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
