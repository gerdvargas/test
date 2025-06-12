# Definir constantes
VELOCIDAD_MAXIMA = 100
NUM_VEHICULOS = 8000

# Variables para estadísticas
velocidad_mas_alta = 0
velocidad_mas_baja = float('inf')
contador_excesos = 0
lista_excesos = []

# Procesar cada vehículo
for i in range(1, NUM_VEHICULOS + 1):
    tiempo = float(input(f"Ingrese el tiempo en minutos que tomó el vehículo {i} en recorrer 500 metros: "))

    if tiempo > 0:
        velocidad = 30 / tiempo  # Calcular velocidad

        # Actualizar velocidad más alta y más baja
        if velocidad > velocidad_mas_alta:
            velocidad_mas_alta = velocidad
        if velocidad < velocidad_mas_baja:
            velocidad_mas_baja = velocidad

        # Verificar exceso de velocidad
        if velocidad > VELOCIDAD_MAXIMA:
            print(f"ALERTA: El vehículo {i} ha excedido el límite de velocidad con {velocidad:.2f} km/hr.")
            lista_excesos.append((i, velocidad))
            contador_excesos += 1

        # Mostrar velocidad del vehículo
        print(f"Vehículo {i}: {velocidad:.2f} km/hr")
    else:
        print("Tiempo no válido, ingrese un número mayor a 0.")

# Mostrar estadísticas finales
print(f"\nCantidad de vehículos que excedieron la velocidad permitida: {contador_excesos}")
print(f"Velocidad más alta registrada: {velocidad_mas_alta:.2f} km/hr")
print(f"Velocidad más baja registrada: {velocidad_mas_baja:.2f} km/hr")

# Mostrar lista de vehículos con exceso de velocidad
if contador_excesos > 0:
    print("\nLista de vehículos que excedieron la velocidad máxima:")
    for vehiculo in lista_excesos:
        print(f"Vehículo {vehiculo[0]}: {vehiculo[1]:.2f} km/hr")


        #Comment Test