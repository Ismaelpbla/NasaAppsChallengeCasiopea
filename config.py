# config.py

# Título y descripción de la aplicación
APP_TITLE = "ExoMiner Dashboard"
APP_DESCRIPTION = """
Explora los resultados del modelo **ExoMiner**, una red neuronal que clasifica candidatos a exoplanetas
usando datos del satélite TESS.  
Selecciona un TIC ID para ver sus características estelares, el resultado de la inferencia y la curva de luz correspondiente.
"""

# Tipos de disposición o clasificación
DISPOSITION_TYPES = {
    "planet_candidate": "🪐 Candidato a planeta",
    "false_positive": "🚫 Falso positivo",
    "confirmed_planet": "✅ Planeta confirmado",
    "unknown": "❓ Desconocido"
}

# Contenido educativo para mostrar en la interfaz
EDUCATIONAL_CONTENT = {
    "overview": """
### ¿Qué es ExoMiner?
ExoMiner es una red neuronal profunda desarrollada por NASA para analizar señales de tránsito detectadas por el satélite TESS.
Evalúa la probabilidad de que un evento sea un exoplaneta verdadero o un falso positivo.

### ¿Qué datos utiliza?
- Curvas de luz de TESS (2-min o FFI)
- Parámetros estelares de TIC-8 y Gaia
- Resultados de TESS SPOC (DV reports)

### ¿Qué produce?
Un puntaje de confianza (`score`) y una clasificación (`disposition`) que indican si el objeto
es un **planeta candidato**, un **planeta confirmado**, o un **falso positivo**.
""",
    "model_details": """
### Modelos disponibles
- **exominer++_single** → Modelo base de ExoMiner.
- **exominer++_cviter-mean-ensemble** → Promedio de modelos cross-validated.
- **exominer++_cv-super-mean-ensemble** → Modelo ensamble de alto rendimiento.

Puedes seleccionar el modelo a utilizar en la ejecución para comparar resultados.
"""
}
