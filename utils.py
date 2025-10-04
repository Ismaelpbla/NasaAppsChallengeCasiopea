"""
Funciones auxiliares para visualización y análisis
"""

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
import streamlit as st
from config import PLOT_COLORS

def plot_light_curve(time, flux, title="Curva de Luz"):
    """
    Visualiza una curva de luz con tránsitos planetarios
    
    Args:
        time: Array de tiempos
        flux: Array de flujos normalizados
        title: Título del gráfico
    """
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=time,
        y=flux,
        mode='lines',
        name='Flujo',
        line=dict(color=PLOT_COLORS['primary'], width=1)
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title="Tiempo (días)",
        yaxis_title="Flujo Normalizado",
        hovermode='x unified',
        template='plotly_white',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

def plot_feature_distribution(df, feature, title=None):
    """
    Crea un histograma de la distribución de una característica
    
    Args:
        df: DataFrame con los datos
        feature: Nombre de la columna
        title: Título del gráfico
    """
    if title is None:
        title = f"Distribución de {feature}"
    
    fig = px.histogram(
        df,
        x=feature,
        color='koi_disposition' if 'koi_disposition' in df.columns else None,
        title=title,
        marginal='box',
        opacity=0.7,
        nbins=50
    )
    
    fig.update_layout(
        template='plotly_white',
        height=400,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

def plot_scatter_comparison(df, x_feature, y_feature, color_by='koi_disposition'):
    """
    Crea un scatter plot comparando dos características
    
    Args:
        df: DataFrame con los datos
        x_feature: Feature para eje X
        y_feature: Feature para eje Y
        color_by: Columna para colorear puntos
    """
    fig = px.scatter(
        df,
        x=x_feature,
        y=y_feature,
        color=color_by if color_by in df.columns else None,
        hover_data=['kepoi_name'] if 'kepoi_name' in df.columns else None,
        title=f"{y_feature} vs {x_feature}",
        opacity=0.6
    )
    
    fig.update_layout(
        template='plotly_white',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

def plot_feature_importance(importance_df, top_n=10):
    """
    Visualiza la importancia de las características del modelo
    
    Args:
        importance_df: DataFrame con features e importancias
        top_n: Número de features principales a mostrar
    """
    top_features = importance_df.head(top_n)
    
    fig = px.bar(
        top_features,
        x='Importance',
        y='Feature',
        orientation='h',
        title=f'Top {top_n} Características Más Importantes',
        color='Importance',
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        template='plotly_white',
        height=400,
        yaxis={'categoryorder': 'total ascending'}
    )
    
    st.plotly_chart(fig, use_container_width=True)

def plot_exoplanet_statistics(df):
    """
    Crea visualizaciones estadísticas de los exoplanetas
    
    Args:
        df: DataFrame con datos de exoplanetas
    """
    col1, col2 = st.columns(2)
    
    with col1:
        # Distribución por disposición
        if 'koi_disposition' in df.columns:
            disposition_counts = df['koi_disposition'].value_counts()
            fig = px.pie(
                values=disposition_counts.values,
                names=disposition_counts.index,
                title='Distribución por Clasificación',
                hole=0.4
            )
            fig.update_layout(template='plotly_white')
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Distribución de scores
        if 'koi_score' in df.columns:
            fig = px.box(
                df,
                y='koi_score',
                color='koi_disposition' if 'koi_disposition' in df.columns else None,
                title='Distribución de Scores de Confianza',
                points='all'
            )
            fig.update_layout(template='plotly_white')
            st.plotly_chart(fig, use_container_width=True)

def create_sky_map(df):
    """
    Crea un mapa del cielo con las posiciones de los KOIs
    
    Args:
        df: DataFrame con coordenadas RA y DEC
    """
    if 'ra' not in df.columns or 'dec' not in df.columns:
        st.warning("No hay datos de coordenadas disponibles")
        return
    
    fig = go.Figure()
    
    for disposition in df['koi_disposition'].unique():
        subset = df[df['koi_disposition'] == disposition]
        fig.add_trace(go.Scattergl(
            x=subset['ra'],
            y=subset['dec'],
            mode='markers',
            name=disposition,
            marker=dict(size=5, opacity=0.6),
            text=subset['kepoi_name'] if 'kepoi_name' in subset.columns else None,
            hovertemplate='<b>%{text}</b><br>RA: %{x:.2f}°<br>DEC: %{y:.2f}°'
        ))
    
    fig.update_layout(
        title='Mapa del Cielo - Distribución de KOIs',
        xaxis_title='Ascensión Recta (°)',
        yaxis_title='Declinación (°)',
        template='plotly_dark',
        height=500,
        hovermode='closest'
    )
    
    st.plotly_chart(fig, use_container_width=True)

def format_scientific(value, decimals=2):
    """
    Formatea un número en notación científica si es apropiado
    
    Args:
        value: Número a formatear
        decimals: Decimales a mostrar
        
    Returns:
        String formateado
    """
    if pd.isna(value):
        return "N/A"
    
    if abs(value) >= 1000 or abs(value) < 0.01:
        return f"{value:.{decimals}e}"
    else:
        return f"{value:.{decimals}f}"

def create_comparison_table(planet_data):
    """
    Crea una tabla comparativa con datos del planeta
    
    Args:
        planet_data: Series con datos del planeta
        
    Returns:
        DataFrame formateado para visualización
    """
    comparisons = []
    
    if 'koi_prad' in planet_data and not pd.isna(planet_data['koi_prad']):
        comparisons.append({
            'Propiedad': 'Radio',
            'Valor': f"{planet_data['koi_prad']:.2f} R⊕",
            'Comparación': f"{planet_data['koi_prad'] / 1:.2f}x Tierra"
        })
    
    if 'koi_period' in planet_data and not pd.isna(planet_data['koi_period']):
        earth_years = planet_data['koi_period'] / 365.25
        comparisons.append({
            'Propiedad': 'Período Orbital',
            'Valor': f"{planet_data['koi_period']:.2f} días",
            'Comparación': f"{earth_years:.3f} años terrestres"
        })
    
    if 'koi_teq' in planet_data and not pd.isna(planet_data['koi_teq']):
        comparisons.append({
            'Propiedad': 'Temperatura',
            'Valor': f"{planet_data['koi_teq']:.0f} K",
            'Comparación': f"{planet_data['koi_teq'] - 273.15:.0f}°C"
        })
    
    if 'koi_steff' in planet_data and not pd.isna(planet_data['koi_steff']):
        sun_ratio = planet_data['koi_steff'] / 5778
        comparisons.append({
            'Propiedad': 'Temperatura Estelar',
            'Valor': f"{planet_data['koi_steff']:.0f} K",
            'Comparación': f"{sun_ratio:.2f}x Sol"
        })
    
    return pd.DataFrame(comparisons)