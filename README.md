# 🌌 ExoMiner Explorer

**Aplicación educativa para explorar exoplanetas usando datos de NASA Kepler**

Desarrollado para el NASA Space Apps Challenge 2025 - Reto: *A World Away: Hunting for Exoplanets with AI*

---

## 📋 Descripción

ExoMiner Explorer es una aplicación interactiva construida con Streamlit que hace accesible el análisis de exoplanetas a usuarios sin conocimientos técnicos previos. Utiliza datos reales del telescopio espacial Kepler de NASA y proporciona herramientas intuitivas para:

- 🔍 Explorar y filtrar datos de más de 1000 exoplanetas candidatos
- 📊 Visualizar curvas de luz y tránsitos planetarios
- 🤖 Aplicar modelos de Machine Learning para clasificación
- 🌍 Analizar habitabilidad potencial
- 📚 Aprender sobre métodos de detección de exoplanetas

---

## 🚀 Instalación Rápida

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
```bash
cd exominer_nasa
```

2. **Crear entorno virtual (recomendado)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## 📁 Estructura del Proyecto

```
exominer_nasa/
│
├── app.py                  # Aplicación principal Streamlit
├── config.py              # Configuración y constantes
├── data_handler.py        # Manejo de datos y API de NASA
├── model_handler.py       # Lógica del modelo ExoMiner
├── utils.py               # Funciones de visualización
├── requirements.txt       # Dependencias del proyecto
└── README.md             # Este archivo
```

### Descripción de Archivos

- **app.py**: Interfaz principal con navegación entre páginas
- **config.py**: URLs, constantes y contenido educativo
- **data_handler.py**: Consultas a NASA Exoplanet Archive y preprocesamiento
- **model_handler.py**: Implementación simplificada del modelo ExoMiner
- **utils.py**: Funciones para gráficos y visualizaciones interactivas

---

## 🎯 Características Principales

### 1. 🏠 Página de Inicio
- Métricas generales del dataset
- Estadísticas de clasificación
- Top exoplanetas descubiertos
- Mapa de distribución en el cielo

### 2. 📊 Explorador de Datos
- Filtrado por disposición y score de confianza
- Tabla interactiva con columnas personalizables
- Distribuciones de características físicas
- Análisis de correlaciones entre variables
- Exportación de datos a CSV

### 3. 🔍 Análisis Detallado
- Información completa de cada exoplaneta
- Curva de luz simulada del tránsito
- Clasificación por tipo (terrestre, super-tierra, etc.)
- Análisis de habitabilidad
- Comparación con la Tierra

### 4. 🤖 Modelo ExoMiner
- Predicción de probabilidad de ser exoplaneta
- Importancia de características (feature importance)
- Simulación de entrenamiento
- Métricas de rendimiento

### 5. 📚 Sección Educativa
- Explicación del método del tránsito
- Tutorial sobre curvas de luz
- Calculadora de zona habitable
- Historia de la misión Kepler

---

## 🔬 Fuentes de Datos

Los datos provienen del **NASA Exoplanet Archive**:
- URL: https://exoplanetarchive.ipac.caltech.edu/
- API: TAP (Table Access Protocol)
- Tabla: `cumulative` (Kepler Objects of Interest)



## 🤖 Sobre el Modelo ExoMiner

**ExoMiner Real**: Desarrollado por NASA, utiliza redes neuronales profundas (Deep Learning) entrenadas con millones de curvas de luz del telescopio Kepler.

**Esta Implementación**: Versión educativa simplificada que usa Random Forest para demostrar los principios de clasificación. Incluye:

- Preprocesamiento de datos (normalización, manejo de valores faltantes)
- Feature engineering basado en conocimiento físico
- Sistema de scoring heurístico para habitabilidad
- Visualización de importancia de características

---

## 📊 Tecnologías Utilizadas

- **Streamlit** - Framework web para aplicaciones de datos
- **Pandas** - Manipulación de datos
- **NumPy** - Operaciones numéricas
- **Plotly** - Visualizaciones interactivas
- **Matplotlib/Seaborn** - Gráficos estáticos
- **Scikit-learn** - Machine Learning
- **Astropy** - Computaciones astronómicas
- **Astroquery** - Consultas a archivos astronómicos

---

## 🎓 Uso Educativo

Esta aplicación es ideal para:

- 👨‍🎓 **Estudiantes**: Aprender sobre exoplanetas de forma interactiva
- 👨‍🏫 **Educadores**: Herramienta para enseñar astronomía y ciencia de datos
- 🔬 **Aficionados**: Explorar datos reales de NASA sin programación
- 🚀 **Divulgadores**: Demostrar conceptos de forma visual


## 🐛 Solución de Problemas

### Error: Módulo no encontrado
```bash
pip install -r requirements.txt --upgrade
```

### La aplicación no carga datos
- Verifica tu conexión a internet (necesita acceso a NASA API)
- La aplicación usará datos de ejemplo si falla la conexión

### Gráficos no se muestran
- Actualiza tu navegador
- Limpia la caché de Streamlit: `streamlit cache clear`

### Error de memoria
- Reduce el límite de datos en `config.py`
- Cierra otras aplicaciones que consuman RAM

---

## 🔮 Mejoras Futuras

- [ ] Implementar ExoMiner real con TensorFlow/PyTorch
- [ ] Añadir datos de TESS (Transiting Exoplanet Survey Satellite)
- [ ] Integración con base de datos James Webb
- [ ] Sistema de autenticación para guardar análisis
- [ ] Modo offline con datos precargados
- [ ] API REST para consultas programáticas
- [ ] Versión multiidioma
- [ ] Integración con realidad virtual (visualización 3D)

---

## 🤝 Contribuciones

Este proyecto fue desarrollado para el **NASA Space Apps Challenge 2025**. Las contribuciones son bienvenidas:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📚 Referencias

- **NASA Exoplanet Archive**: https://exoplanetarchive.ipac.caltech.edu/
- **Kepler Mission**: https://www.nasa.gov/mission_pages/kepler/
- **ExoMiner Paper**: https://arxiv.org/abs/2108.04869
- **Astropy Documentation**: https://docs.astropy.org/
- **Streamlit Docs**: https://docs.streamlit.io/

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT para fines educativos.

---

## 👥 Autores

Desarrollado con ❤️ para el NASA Space Apps Challenge 2025

**Contacto**: [Tu información de contacto]

---

## 🌟 Agradecimientos

- NASA por proporcionar datos abiertos
- Equipo de Kepler por el increíble trabajo científico
- Comunidad de Streamlit por el framework
- Space Apps Challenge por la inspiración

---

## 📞 Soporte

¿Tienes preguntas o sugerencias?

- 🐛 **Issues**: Reporta bugs en GitHub Issues
- 💬 **Discusiones**: Únete a GitHub Discussions
- 📧 **Email**: [Tu email]
- 🌐 **Web**: [Tu sitio web]

---

**¡Explora el universo de exoplanetas! 🚀🌌**# NasaAppsChallengeCasiopea
