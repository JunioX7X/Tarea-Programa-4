class Persona:
    """
    Representa a una persona/cliente en el sistema de colas.
    """
    def __init__(self, tiempo_llegada, prioridad, tiempo_servicio):
        self.tiempo_llegada = tiempo_llegada
        self.prioridad = prioridad  # 0 = alta prioridad, 1 = baja prioridad
        self.tiempo_servicio = tiempo_servicio
        self.tiempo_inicio_servicio = None  # Se establece cuando comienza a ser atendido

class Estacion:
    """
    Representa una estación de servicio en el sistema.
    """
    def __init__(self, exclusiva_prioridad=False):
        self.exclusiva_prioridad = exclusiva_prioridad  # Si es True, es exclusiva para personas con prioridad
        self.ocupada = False  # Estado actual de la estación
        self.persona_actual = None  # Persona siendo atendida actualmente
        self.tiempo_disponible = 0.0  # Tiempo en que la estación estará disponible nuevamente
        self.total_tiempo_ocupada = 0.0  # Tiempo total que la estación ha estado ocupada