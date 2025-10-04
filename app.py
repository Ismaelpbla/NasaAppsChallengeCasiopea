"""
ExoMiner Explorer - Aplicación Streamlit
Versión autocontenida con datos JSON hardcodeados
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

# =========================
# CONFIGURACIÓN BÁSICA
# =========================
APP_TITLE = "ExoMiner Explorer"
APP_DESCRIPTION = """
Explora y analiza exoplanetas detectados por el telescopio **Kepler** de la NASA.  
Esta es una versión demostrativa con datos simulados.
"""

EDUCATIONAL_CONTENT = {
    "transit_method": "El método del tránsito mide la disminución del brillo estelar cuando un planeta pasa frente a su estrella.",
    "light_curve": "Las curvas de luz son gráficas que muestran el brillo de una estrella a lo largo del tiempo.",
    "habitable_zone": "La zona habitable es la región alrededor de una estrella donde el agua líquida puede existir en la superficie de un planeta."
}

DISPOSITION_TYPES = ["CONFIRMED", "CANDIDATE", "FALSE POSITIVE"]

# =========================
# CONFIGURACIÓN DE PÁGINA
# =========================
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# ESTILO CSS
# =========================
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(120deg, #1e3c72, #2a5298, #7e22ce);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# DATOS HARDCODEADOS
# =========================
@st.cache_data
def load_data():
    """Carga datos simulados de exoplanetas"""
    data = [
        {
            "name": "Kepler-22b",
            "disposition": "CONFIRMED",
            "score": 0.98,
            "period_days": 289.9,
            "radius_re": 2.4,
            "teq": 295,
            "host_star_temp": 5518,
            "prediction": "planet_confirmed"
        },
        {
            "name": "Kepler-452b",
            "disposition": "CONFIRMED",
            "score": 0.95,
            "period_days": 385.0,
            "radius_re": 1.6,
            "teq": 265,
            "host_star_temp": 5757,
            "prediction": "planet_confirmed"
        },
        {
            "name": "KOI-3010.01",
            "disposition": "CANDIDATE",
            "score": 0.81,
            "period_days": 60.9,
            "radius_re": 1.1,
            "teq": 320,
            "host_star_temp": 4932,
            "prediction": "planet_candidate"
        },
        {
            "name": "KOI-871.02",
            "disposition": "FALSE POSITIVE",
            "score": 0.45,
            "period_days": 13.2,
            "radius_re": 4.5,
            "teq": 700,
            "host_star_temp": 6100,
            "prediction": "false_positive"
        }
    ]
    return pd.DataFrame(data)

# =========================
# PÁGINAS
# =========================
def home_page(df):
    st.markdown(f'<h1 class="main-header">{APP_TITLE}</h1>', unsafe_allow_html=True)
    st.markdown(APP_DESCRIPTION)

    # === Inputs simulando una consulta al backend ===
    st.markdown("### 🧪 Analiza un nuevo objetivo con ExoMiner")
    col1, col2, col3 = st.columns([1, 1, 1.5])

    with col1:
        tic_id = st.text_input("🔭 TIC ID", placeholder="Ejemplo: TIC 123456789")
    with col2:
        sector_run = st.text_input("🛰️ Sector / Run", placeholder="Ejemplo: Sector 14")
    with col3:
        simulate = st.button("🚀 Analizar con ExoMiner")

    if simulate:
        if tic_id and sector_run:
            with st.spinner("Procesando con ExoMiner... 🔬"):
                st.toast(f"Consultando modelo ExoMiner para {tic_id} (Sector {sector_run})...", icon="🔄")
                time.sleep(2.5)

            st.success(f"✅ Resultados obtenidos para **{tic_id}** en **{sector_run}**")

            # Simular filtrado de resultados del "backend"
            # (aquí puedes definir tu lógica personalizada)
            np.random.seed(len(tic_id) + len(sector_run))
            selected_rows = df.sample(n=1).copy()
            selected_rows["tic_id"] = tic_id
            selected_rows["sector_run"] = sector_run

            st.markdown("---")
            st.subheader("📊 Resultados del Análisis Simulado")

            col1, col2, col3, col4 = st.columns(4)
            row = selected_rows.iloc[0]

            with col1:
                st.metric("Exoplaneta", row["name"])
            with col2:
                st.metric("Disposición", row["disposition"])
            with col3:
                st.metric("Score ExoMiner", f"{row['score']:.2f}")
            with col4:
                st.metric("Período Orbital (días)", f"{row['period_days']:.1f}")

            st.markdown("---")
            st.subheader("🌟 Catálogo Filtrado (Simulación ExoMiner)")
            st.dataframe(selected_rows, use_container_width=True)

        else:
            st.warning("Por favor, introduce un **TIC ID** y un **Sector/Run** válidos antes de analizar.")
            return

    else:
        st.info("Introduce un **TIC ID** y un **Sector/Run**, luego pulsa *Analizar con ExoMiner* para ver resultados simulados.")



def explore_data_page(df):
    st.header("📊 Exploración de Datos")

    disposition_filter = st.sidebar.multiselect(
        "Filtrar por disposición:",
        options=DISPOSITION_TYPES,
        default=DISPOSITION_TYPES
    )

    df_filtered = df[df["disposition"].isin(disposition_filter)]

    st.info(f"Mostrando {len(df_filtered)} de {len(df)} exoplanetas")

    st.dataframe(df_filtered, use_container_width=True)

    st.markdown("---")
    st.subheader("📈 Distribución de Scores")
    st.bar_chart(df_filtered["score"])


def learn_page():
    st.header("📚 Aprende sobre Exoplanetas")

    tab1, tab2, tab3 = st.tabs([
        "🔭 Método del Tránsito",
        "📉 Curvas de Luz",
        "🌍 Zona Habitable"
    ])

    with tab1:
        st.markdown(EDUCATIONAL_CONTENT["transit_method"])

    with tab2:
        st.markdown(EDUCATIONAL_CONTENT["light_curve"])

    with tab3:
        st.markdown(EDUCATIONAL_CONTENT["habitable_zone"])
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/ExoplanetHabitability.svg/800px-ExoplanetHabitability.svg.png",
            caption="Zona habitable en diferentes tipos de estrellas",
            use_container_width=True
        )


# =========================
# FUNCIÓN PRINCIPAL
# =========================
def main():
    df = load_data()

    st.sidebar.title("🚀 Navegación")
    page = st.sidebar.radio(
        "Selecciona una sección:",
        ["🏠 Inicio", "📊 Explorar Datos", "📚 Aprende"]
    )

    if page == "🏠 Inicio":
        home_page(df)
    elif page == "📊 Explorar Datos":
        explore_data_page(df)
    elif page == "📚 Aprende":
        learn_page()

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Demo educativa del modelo ExoMiner (NASA)**")


# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    main()
