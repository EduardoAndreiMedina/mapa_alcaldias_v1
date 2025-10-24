import pandas as pd #pandas para manejo de dataframes
import streamlit as st #streamlit para la app web

@st.cache_data #cachear la función para mejorar rendimiento
def load_data(path="df_streamlit.csv", for_stmap=False): #Función para cargar y limpiar el dataset de incidentes
    """
    Carga y limpia el dataset base de incidentes.
    
    Parámetros:
        path (str): ruta del archivo CSV.
        for_stmap (bool): si True, renombra las columnas para usar con st.map().
    
    Retorna:
        pd.DataFrame: datos listos para visualización.
    """
    try: # Manejo de errores al cargar el dataset
        # 1️⃣ Leer el CSV
        df = pd.read_csv(path)
        st.info(f"Archivo cargado: {len(df)} registros totales.") 
        
        # 2️⃣ Eliminar filas sin coordenadas válidas
        df = df.dropna(subset=["latitud", "longitud"]) # Eliminar filas con NaN en latitud/longitud
        st.success(f"Datos limpios: {len(df)} registros con coordenadas válidas.") # Mensaje de éxito

        # 3️⃣ Si se usará con st.map(), crear columnas compatibles
        if for_stmap: # Renombrar columnas para st.map()
            df = df.rename(columns={"latitud": "latitude", "longitud": "longitude"}) # Renombrar columnas
            st.caption("🗺️ Columnas renombradas a 'latitude' y 'longitude' para st.map().") # Mensaje de éxito 
        
        return df # Retornar el DataFrame limpio

    except Exception as e: # Captura cualquier error durante la carga/limpieza
        st.error(f"Error al cargar el dataset: {e}") # Mensaje de error
        return pd.DataFrame() # Retornar DataFrame vacío en caso de error
