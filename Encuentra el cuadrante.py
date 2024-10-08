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
0
1
