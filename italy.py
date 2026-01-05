import streamlit as st
import plotly.express as px
import pandas as pd

# Configurazione pagina per Streamlit
st.set_page_config(page_title="Italy 2025 Energy Map", layout="centered")

st.title("🇮🇹 Italy 2025: Regional Clean Energy Footprint")
st.markdown("Interactive visualization of renewable energy share in gross final consumption. *Hover over regions for details.*")

# 1. Dataset (I tuoi dati verificati 2025)
data = {
    'Region': [
        'Abruzzo', 'Basilicata', 'Calabria', 'Campania', 'Emilia-Romagna',
        'Friuli-Venezia Giulia', 'Lazio', 'Liguria', 'Lombardia', 'Marche',
        'Molise', 'Piemonte', 'Puglia', 'Sardegna', 'Sicilia', 'Toscana',
        'Trentino-Alto Adige', 'Umbria', "Valle d'Aosta", 'Veneto'
    ],
    'Renewables_2025': [
        42.5, 88.0, 72.3, 31.0, 21.5,
        24.0, 18.5, 12.0, 28.5, 29.0,
        65.5, 41.0, 78.5, 62.0, 48.5, 36.0,
        95.0, 34.5, 99.5, 26.0
    ]
}

df = pd.DataFrame(data)

# 2. GeoJSON per i confini regionali
geojson_url = "https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_IT_regions.geojson"

# 3. Creazione Mappa Interattiva
fig = px.choropleth(df,
                    geojson=geojson_url,
                    locations='Region',
                    featureidkey='properties.reg_name',
                    color='Renewables_2025',
                    color_continuous_scale='Blues',
                    range_color=[10, 100],
                    hover_name='Region', # Mostra il nome in grassetto nell'hover
                    hover_data={'Region': False, 'Renewables_2025': ':.1f'}, # Formattazione pulita
                    labels={'Renewables_2025': 'Renewables Share (%)'})

fig.update_geos(fitbounds="locations", visible=False)

fig.update_layout(
    margin=dict(l=0, r=0, t=20, b=0),
    height=600,
    coloraxis_colorbar=dict(
        title="Share %",
        x=0.8,
        y=0.5,
        len=0.75
    )
)

# Visualizzazione su Streamlit
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.caption("Source: Estimates based on Terna and GSE 2025 reports. Built with Plotly & Streamlit.")
