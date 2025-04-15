from generador import generar_personas
from sistema_colas import simular
from metricas import calcular_ocupacion
from modelos import Estacion
from config import *


def correr_simulacion(estaciones_config):
    # Genera las personas para la simulación
    personas = generar_personas(TIEMPO_TOTAL, LAMBDA_LLEGADAS, PROB_PRIORIDAD, LAMBDA_SERVICIO)

    # Crea las estaciones según la configuración
    estaciones = [Estacion(**cfg) for cfg in estaciones_config]

    # Determina si hay alguna estación exclusiva para prioridad
    hay_exclusiva = any(cfg.get("exclusiva_prioridad", False) for cfg in estaciones_config)

    # Corre la simulación
    espera_promedio, max_cola, estaciones_finales, atendidos = simular(personas, estaciones, TIEMPO_TOTAL,
                                                                       hay_exclusiva)

    # Calcula la ocupación
    ocupacion = calcular_ocupacion(estaciones_finales, TIEMPO_TOTAL)

    return espera_promedio, max_cola, ocupacion


def main():
    # Primera simulación: todas las estaciones son genéricas
    print("Simulación con estaciones genéricas:")
    estaciones_gen = [{"exclusiva_prioridad": False} for _ in range(3)]
    espera, cola, ocupacion = correr_simulacion(estaciones_gen)
    print(f"Tiempo espera promedio: {espera:.2f} min, Longitud máxima cola: {cola}, Ocupación: {ocupacion:.2f}%\n")
    # Segunda simulación: 1 estación exclusiva para prioridad
    print("Simulación con 1 estación exclusiva para prioridad:")
    estaciones_mix = [{"exclusiva_prioridad": True}] + [{"exclusiva_prioridad": False} for _ in range(2)]
    espera, cola, ocupacion = correr_simulacion(estaciones_mix)
    print(f"Tiempo espera promedio: {espera:.2f} min, Longitud máxima cola: {cola}, Ocupación: {ocupacion:.2f}%")


if __name__ == "__main__":
    main()