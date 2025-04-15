# 🏦 Sistema de Simulación de Colas con Prioridad

Un simulador de sistema de colas que modela la atención en estaciones de servicio con diferentes niveles de prioridad, generando métricas clave de desempeño.

## 📦 Contenido
- [Descripción](#-descripción)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Métricas](#-métricas)
- [Ejemplo](#-ejemplo)
- [Contribuciones](#-contribuciones)

## 📝 Descripción

Simulador que modela:
- Personas con prioridad alta (30%) y normal (70%)
- Múltiples estaciones de servicio configurables
- Posibilidad de estaciones exclusivas para prioridad alta
- Generación de estadísticas de desempeño

## ⚙️ Configuración

### Requisitos
```bash
Python 3.8+
numpy==2.2.4


Parámetros (config.py)
python

TIEMPO_TOTAL = 480        # 8 horas (en minutos)
LAMBDA_LLEGADAS = 1/2.0   # 1 persona cada 2 minutos
LAMBDA_SERVICIO = 1/4.0   # 4 minutos por atención
PROB_PRIORIDAD = 0.3      # 30% prioridad alta


🚀 Uso
Instalar dependencias:

bash

pip install -r requirements.txt


📊 Métricas
Métrica	Descripción
Tiempo espera promedio	Tiempo medio en cola (minutos)
Longitud máxima cola	Máximo número de personas esperando
% Ocupación	Uso de las estaciones
💻 Ejemplo de Salida

Simulación con 3 estaciones genéricas:
⏱️  Espera promedio: 12.34 min
👥  Máxima cola: 8
📈  Ocupación: 78.56%

Simulación con 1 estación exclusiva:
⏱️  Espera promedio: 9.87 min  
👥  Máxima cola: 6
📈  Ocupación: 82.34%
