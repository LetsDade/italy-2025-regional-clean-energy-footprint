import streamlit as st
import plotly.express as px
import pandas as pd

# Configurazione pagina
st.set_page_config(page_title="Italy 2025 Energy Map", layout="centered")

# 1. Titolo ottimizzato (Dimensioni ridotte e break manuale bilanciato)
st.markdown("""
    <style>
    .main-title {
        font-size: 28px !important;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    <div class="main-title">
        🇮🇹 Italy 2025: Regional Clean Energy Footprint<br>
        <span style="font-size: 18px; font-weight: normal; color: #555;">
            Renewable energy share in gross final consumption by Region
        </span>
    </div>
    """, unsafe_allow_html=True)

# 2. Dataset
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

# 3. GeoJSON
geojson_url = "https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_IT_regions.geojson"

# 4. Creazione Mappa
fig = px.choropleth(df,
                    geojson=geojson_url,
                    locations='Region',
                    featureidkey='properties.reg_name',
                    color='Renewables_2025',
                    color_continuous_scale='Blues',
                    range_color=[10, 100],
                    hover_name='Region',
                    hover_data={'Region': False, 'Renewables_2025': ':.1f'},
                    labels={'Renewables_2025': 'Share (%)'})

fig.update_geos(fitbounds="locations", visible=False)

# 5. Layout Professionale (Focus su Colorbar e Proporzioni)
fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0), # Rimosso margine superiore per dare spazio al div HTML
    height=750, # Altezza aumentata per bilanciare il titolo
    coloraxis_colorbar=dict(
        title="Share %",
        thicknessmode="pixels", thickness=15,
        lenmode="fraction", len=0.85, # Lunghezza che copre quasi tutta l'Italia
        yanchor="middle", y=0.5,      # Centrata verticalmente
        xanchor="left", x=0.85,       # Avvicinata allo stivale
        ticks="outside"
    )
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
    <p style='text-align: center; color: gray; font-size: 12px;'>
        Data: 2025 Estimates (Terna/GSE) | Interactive Portfolio Task 10
    </p>
    """, unsafe_allow_html=True)
