from collections import deque

def simular(personas, estaciones, tiempo_total, exclusiva=False):
    cola_prioridad = deque()  # Cola para personas con prioridad alta
    cola_normal = deque()  # Cola para personas con prioridad baja
    tiempo = 0.0
    indice_persona = 0
    max_cola = 0
    espera_total = 0.0
    personas_atendidas = 0

    while tiempo < tiempo_total or any(e.ocupada for e in estaciones):
        while indice_persona < len(personas) and personas[indice_persona].tiempo_llegada <= tiempo:
            p = personas[indice_persona]
            if p.prioridad == 0:
                cola_prioridad.append(p)
            else:
                cola_normal.append(p)
            indice_persona += 1

        max_cola = max(max_cola, len(cola_prioridad) + len(cola_normal))

        for est in estaciones:
            if not est.ocupada or tiempo >= est.tiempo_disponible:
                est.ocupada = False

            if not est.ocupada:
                persona_a_atender = None
                if est.exclusiva_prioridad:
                    if cola_prioridad:
                        persona_a_atender = cola_prioridad.popleft()
                    elif cola_normal:
                        persona_a_atender = cola_normal.popleft()
                else:
                    if cola_prioridad:
                        persona_a_atender = cola_prioridad.popleft()
                    elif cola_normal:
                        persona_a_atender = cola_normal.popleft()

                if persona_a_atender:
                    persona_a_atender.tiempo_inicio_servicio = tiempo
                    espera_total += tiempo - persona_a_atender.tiempo_llegada
                    est.tiempo_disponible = tiempo + persona_a_atender.tiempo_servicio
                    est.total_tiempo_ocupada += persona_a_atender.tiempo_servicio
                    est.ocupada = True
                    est.persona_actual = persona_a_atender
                    personas_atendidas += 1

        tiempo += 1.0

    return espera_total / personas_atendidas, max_cola, estaciones, personas_atendidas