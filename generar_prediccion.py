import json
import random
from datetime import datetime

# Simulación de datos que obtendrías de una API real
# En la vida real, usarías: requests.get('URL_DE_TU_API')
partidos_hoy = [
    {"local": "Real Madrid", "visitante": "Barcelona", "forma_local": 0.85, "forma_visitante": 0.80},
    {"local": "Manchester City", "visitante": "Arsenal", "forma_local": 0.90, "forma_visitante": 0.88},
    {"local": "Juventus", "visitante": "Milan", "forma_local": 0.60, "forma_visitante": 0.65},
]

def analizar_partido(partido):
    # LÓGICA SIMPLE DE PREDICCIÓN (Aquí es donde va tu matemática compleja)
    # Fórmula ejemplo: Si la forma del local es 10% mayor que la del visitante -> Gana Local
    
    score_local = partido["forma_local"] * 1.10 # Ventaja de campo
    score_visitante = partido["forma_visitante"]
    
    probabilidad = 0
    prediccion = ""
    confianza = ""

    if score_local > (score_visitante + 0.1):
        prediccion = "Gana Local"
        probabilidad = score_local * 100
    elif score_visitante > (score_local + 0.1):
        prediccion = "Gana Visitante"
        probabilidad = score_visitante * 100
    else:
        prediccion = "Empate / Baja de goles"
        probabilidad = 50.0

    # Determinar nivel de confianza
    if probabilidad > 85: confianza = "ALTA"
    elif probabilidad > 60: confianza = "MEDIA"
    else: confianza = "BAJA"

    return {
        "partido": f"{partido['local']} vs {partido['visitante']}",
        "prediccion": prediccion,
        "confianza": confianza,
        "probabilidad_calculada": f"{round(probabilidad, 2)}%"
    }

# Generar lista de resultados
resultados_finales = []
for p in partidos_hoy:
    resultados_finales.append(analizar_partido(p))

# Guardar en un archivo JSON (Esto actúa como tu base de datos simple)
# Si tienes un servidor, esto se guardaría en una carpeta pública
with open('datos_apuestas.json', 'w') as f:
    json.dump(resultados_finales, f)

print("Análisis completado. Datos guardados en datos_apuestas.json")
