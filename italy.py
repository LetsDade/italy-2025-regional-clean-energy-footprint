import streamlit as st
import plotly.express as px
import pandas as pd

# 2025 Regional Data (Estimates based on Terna and GSE year-end reports)
# Share of renewables in gross final energy consumption (%)
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

# Official GeoJSON URL for Italian regional boundaries (ISTAT/OpenPolis)
geojson_url = "https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_IT_regions.geojson"

# Creating the English Regional Choropleth Map
fig = px.choropleth(df,
                    geojson=geojson_url,
                    locations='Region',
                    featureidkey='properties.reg_name',
                    color='Renewables_2025',
                    color_continuous_scale='Blues',
                    range_color=[10, 100],
                    labels={'Renewables_2025':'Renewables Share (%)'})

# Geographical optimization for Italy
fig.update_geos(fitbounds="locations", visible=False)

fig.update_layout(
    title=dict(
        text="<b>Italy 2025: Regional Clean Energy Footprint</b><br>Share of renewable energy in gross final consumption by Region",
        x=0.48 # Regola il titolo per allinearlo visivamente allo stivale
    ),
    margin=dict(l=0, r=0, t=80, b=0),
    font=dict(size=14, color='black'),
    coloraxis_colorbar=dict(
        title="Share %", # Ripristinato il titolo predefinito
        x=0.7, # Sposta la colorbar più a sinistra per avvicinarla al grafico
        y=0.55,
        yanchor='middle',
        len=0.9 # Rende la colorbar più corta
    )
)

# Rimossa l'annotazione separata per il titolo della colorbar

fig.show()
