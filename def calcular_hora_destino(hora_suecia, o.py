def calcular_hora_destino(hora_suecia, opcion_pais):
    diferencias_horarias = {
        1: (6, "Singapur"),
        2: (-10, "Canadá Oeste"),
        3: (3.5, "India")
    }

    if opcion_pais in diferencias_horarias:
        diferencia_horaria, pais_destino = diferencias_horarias[opcion_pais]
        hora_destino = hora_suecia + diferencia_horaria

        if hora_destino >= 24:
            hora_destino -= 24
            print(f"La hora en {pais_destino} es {hora_destino:.2f} del día siguiente.")
        elif hora_destino < 0:
            hora_destino += 24
            print(f"La hora en {pais_destino} es {hora_destino:.2f} del día anterior.")
        else:
            print(f"La hora en {pais_destino} es {hora_destino:.2f}.")
    else:
        print("Opción no válida.")

# Solicitar datos al usuario
hora_suecia = float(input("Ingrese la hora actual en Suecia (formato 24 horas): "))
print("Seleccione el país que visitará:")
print("1. Singapur (+6 horas)")
print("2. Canadá Oeste (-10 horas)")
print("3. India (+3.5 horas)")
opcion_pais = int(input("Ingrese el número correspondiente al país: "))

calcular_hora_destino(hora_suecia, opcion_pais)