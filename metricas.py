def calcular_ocupacion(estaciones, tiempo_total):
    # Suma el tiempo total que cada estación estuvo ocupada
    suma = sum(e.total_tiempo_ocupada for e in estaciones)

    # Calcula y retorna el porcentaje de ocupación
    return (suma / (tiempo_total * len(estaciones))) * 100