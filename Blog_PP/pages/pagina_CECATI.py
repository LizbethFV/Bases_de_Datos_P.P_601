import dash
from dash import html, dcc
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

#Registrar la segunda pagina
dash.register_page(__name__, path="/CECATI", name="CECATI")

df_CECATI_OA = pd.read_csv('https://raw.githubusercontent.com/LizbethFV/Bases_de_Datos_P.P_601/refs/heads/main/CECATI%20-%20Numeralia%20inscritos-acreditados%20.csv')
df_CECATI_CE = pd.read_csv('https://raw.githubusercontent.com/LizbethFV/Bases_de_Datos_P.P_601/refs/heads/main/CECATI%20-%20Especialidades.csv')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# @title Grafica de matricula del CECATI por año
#Seleccionamos el año 2019
df_CECATI_OA2019 = df_CECATI_OA[df_CECATI_OA['Periodo'] == 2019]
#2020
df_CECATI_OA2020 = df_CECATI_OA[df_CECATI_OA['Periodo'] == 2020]
#2021
df_CECATI_OA2021 = df_CECATI_OA[df_CECATI_OA['Periodo'] == 2021]
#2022
df_CECATI_OA2022 = df_CECATI_OA[df_CECATI_OA['Periodo'] == 2022]
#2023
df_CECATI_OA2023 = df_CECATI_OA[df_CECATI_OA['Periodo'] == 2023]
#2024
df_CECATI_OA2024 = df_CECATI_OA[df_CECATI_OA['Periodo'] == 2024]

#Generamos una sola figura
fig_CECATI_M = go.Figure()

#Graficamo el historico
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA['Inscritos'].sum(), df_CECATI_OA['Acreditados'].sum()],
    text = ["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#283C55', '#5E466E']),
    visible=True,
    connector=dict(visible=False)
))
#Graficamos 2019
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA2019['Inscritos'].sum(), df_CECATI_OA2019['Acreditados'].sum()],
    text = ["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#283C55', '#5E466E']),
    visible=False,
    connector=dict(visible=False)
))
#Graficamos 2020
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA2020['Inscritos'].sum(), df_CECATI_OA2020['Acreditados'].sum()],
    text = ["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#283C55', '#5E466E']),
    visible=False,
    connector=dict(visible=False)
))
#Graficamos 2021
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA2021['Inscritos'].sum(), df_CECATI_OA2021['Acreditados'].sum()],
    text = ["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#283C55', '#5E466E']),
    visible=False,
    connector=dict(visible=False)
))
#Graficamos 2022
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA2022['Inscritos'].sum(), df_CECATI_OA2022['Acreditados'].sum()],
    text=["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#283C55', '#5E466E']),
    visible=False,
    connector=dict(visible=False)
))
#graficamos 2023
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA2023['Inscritos'].sum(), df_CECATI_OA2023['Acreditados'].sum()],
    text=["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#283C55', '#5E466E']),
    visible=False,
    connector=dict(visible=False)
))
#graficamos 2024
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA2024['Inscritos'].sum(), df_CECATI_OA2024['Acreditados'].sum()],
    text=["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#283C55', '#5E466E']),
    visible=False,
    connector=dict(visible=False)
))

#damos fromato
fig_CECATI_M.update_layout(
    title='Inscritos y Acreditados Historico y por Año del CECATI',
    title_font=dict(size=20, color='black'),
    font=dict(family='New Times Roman', size=15, color='black'),
    width=900,
    height=500,
    paper_bgcolor='white',
    plot_bgcolor='white',
    yaxis_showticklabels=False
)
#Creamos el Slider
Slider_CECATI_M = []
for i, label in enumerate(['2019-2024','2019','2020', '2021', '2022', '2023', '2024']):
    slider_CECATI_M = dict(
        method='update',
        label=label,
        args = [{"visible": [False] * len(fig_CECATI_M.data)}]
    )
    slider_CECATI_M['args'][0]['visible'][i] = True
    Slider_CECATI_M.append(slider_CECATI_M)

fig_CECATI_M.update_layout(
    sliders=[dict(
        active=0,
        currentvalue={'prefix': 'Año: '},
        steps=Slider_CECATI_M
)]
)
#---------------------------------------------------------------------------------------------------
#Especialidades por unidad academica
# en este caso haremos una tabla por unidad del CECATI
#Hacemos una lista de cecati
CECATI = df_CECATI_CE['CECATI'].unique()

#Creamos una figura
tab_CECATI = go.Figure()

for cecati in CECATI:
  CEATI_F = df_CECATI_CE[df_CECATI_CE['CECATI'] == cecati]

  #Creamos la tabla
  tab_CECATI.add_trace(
      go.Table(
          header=dict(
              values=['Especialidad', 'Clave', 'Modalidad'],
              fill_color=['#283C55'],
              font=dict(color='white', family='New Times Roman'),
              align='center',
              line=dict(color='#5E466E', width=0)
          ),
          cells=dict(
              values=[CEATI_F['Especialidad'], CEATI_F['Clave'], CEATI_F['Modalidad']],
              fill_color='white',
              align='left',
              line=dict(color='#5E466E', width=0),
          ),
          visible=False
      )
      )
#Mostramos la primera tabla para que no se vea vacio
tab_CECATI.data[0].visible = True

#Creamos un dropdown
Boton= [
    dict(
        label=f"CECATI {cecati}",
        method="update",
        args=[{"visible": [k == j for k in range(len(CECATI))]}, {"title": f"Especialidades del CECATI {cecati}"}]
    )
    for j, cecati in enumerate(CECATI)
]
tab_CECATI.update_layout(
    width=900,
    height=500,
    paper_bgcolor='white',
    plot_bgcolor='white',
    font=dict(family='New Times Roman', size=15, color='black'),
    updatemenus = [
        dict(
            buttons=Boton,
            direction="down",
            showactive=True,
            x=0.5,
            xanchor="center",
            y=1.15,
            yanchor="top"
        )
    ],
    title="Especialidades del CECATI"
)
#---------------------------------------------------------------------------------------------------------

layout = html.Div([
    html.H1("Información del CECATI"),
    html.P("En este apartado se presenta información general del CECATI."),
    html.Br(),
    dcc.Graph(figure=fig_CECATI_M),
    
    html.H2("Especialidades por Unidad"),
    html.P("Selecciona una unidad para consultar sus especialidades."),
    dcc.Graph(figure=tab_CECATI)
])