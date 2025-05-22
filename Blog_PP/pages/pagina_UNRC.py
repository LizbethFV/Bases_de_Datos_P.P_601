import dash
from dash import html, dcc
import pandas as pd
import plotly.graph_objs as go
from re import U
import plotly.express as px

#Registramos la página
dash.register_page(__name__, path="/", name="Inicio")

# Cargar datos limpios
Colores = ['#283C55','#5E466E', '#B56576', '#E56B6F', '#EAAC8B', '#355070', '#515575', '#9D5D7D','#CD6873', '#E88C7D', '#283C55','#5E466E', '#B56576', '#E56B6F', '#EAAC8B', '#355070', '#515575', '#9D5D7D','#CD6873', '#E88C7D']
df_Est_per = pd.read_csv('https://raw.githubusercontent.com/LizbethFV/Bases_de_Datos_P.P_601/refs/heads/main/df_Est_per.csv')
df_Est_UA = pd.read_csv('https://raw.githubusercontent.com/LizbethFV/Bases_de_Datos_P.P_601/refs/heads/main/df_Est_UA.csv')
df_ODE = pd.read_csv('https://raw.githubusercontent.com/LizbethFV/Bases_de_Datos_P.P_601/refs/heads/main/df_ODE.csv')
df_Lic_UA = pd.read_csv('https://raw.githubusercontent.com/LizbethFV/Bases_de_Datos_P.P_601/refs/heads/main/df_Lic_UA.csv')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Graficas de la Oferta-Demanda-Egresados por año
#2021
dfODE2021 = df_ODE[df_ODE['Año'] == 2021]
#2022
dfODE2022 = df_ODE[df_ODE['Año'] == 2022]
#2023
dfODE2023 = df_ODE[df_ODE['Año'] == 2023]
#2024
dfODE2024 = df_ODE[df_ODE['Año'] == 2024]

#Generamos una figura
fig_ODE = go.Figure()
etiquetas_ode=['Aspirantes que realizaron el PIRC', 'Aspirantes seleccionados', 'Egresados']
#Graficamos el embudo general 2019-2024
fig_ODE.add_trace(go.Funnel(
        y=etiquetas_ode,
        x=[df_ODE['Aspirantes PIRC'].sum(),
           df_ODE['Aspirantes seleccionados'].sum(),
           df_ODE['Egresados'].sum()],
       text=etiquetas_ode,
       textinfo = "text+value+percent initial",
       marker=dict(color=Colores),
       visible=True,
       connector=dict(visible=False)
    ))
#Graficamos 2021
fig_ODE.add_trace(go.Funnel(
    y=etiquetas_ode,
    x=[dfODE2021['Aspirantes PIRC'].sum(),
       dfODE2021['Aspirantes seleccionados'].sum(),
       dfODE2021['Egresados'].sum()],
       text=etiquetas_ode,
       textinfo = "text+value+percent initial",
       marker=dict(color=Colores),
       visible=False,
       connector=dict(visible=False)
    ))
#Graficamos 2022
fig_ODE.add_trace(go.Funnel(
    y=etiquetas_ode,
    x=[dfODE2022['Aspirantes PIRC'].sum(),
       dfODE2022['Aspirantes seleccionados'].sum(),
       dfODE2022['Egresados'].sum()],
       text=etiquetas_ode,
       textinfo = "text+value+percent initial",
       marker=dict(color=Colores),
       visible=False,
       connector=dict(visible=False)
))
#Graficamos 2023
fig_ODE.add_trace(go.Funnel(
    y=etiquetas_ode,
    x=[dfODE2023['Aspirantes PIRC'].sum(),
       dfODE2023['Aspirantes seleccionados'].sum(),
       dfODE2023['Egresados'].sum()],
       text=etiquetas_ode,
       textinfo = "text+value+percent initial",
       marker=dict(color=Colores),
       visible=False,
       connector=dict(visible=False)
))
#Graficamos 2024
fig_ODE.add_trace(go.Funnel(
    y=etiquetas_ode,
    x=[dfODE2024['Aspirantes PIRC'].sum(),
       dfODE2024['Aspirantes seleccionados'].sum(),
       dfODE2024['Egresados'].sum()],
       text=etiquetas_ode,
       textinfo = "text+value+percent initial",
       marker=dict(color=Colores),
       textposition='inside',
       visible=False,
       connector=dict(visible=False)
))
fig_ODE.update_layout(
    width=900,
    height=500,
    title='Apirantes en Proceso de Selección, Seleccionados y Egresados',
    title_font=dict(size=20, color='black'),
    font=dict(family='New Times Roman', size=15, color='black'),
    paper_bgcolor='white',
    plot_bgcolor='white',
    yaxis_showticklabels=False

)
#Creamos un Slider para poder movernos de uno a otro
Slider_ODE = []
for i, label in enumerate(['2019-2024','2021', '2022', '2023', '2024']):
    slider_ode = dict(
        method='update',
        label=label,
        args = [{"visible": [False] * len(fig_ODE.data)}]
    )
    slider_ode['args'][0]['visible'][i] = True
    Slider_ODE.append(slider_ode)

fig_ODE.update_layout(
    sliders=[dict(
        active=0,
        currentvalue={'prefix': 'Año: '},
        steps=Slider_ODE
)]
)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Graficas de las licenciaturas por año modalidad  presencial
#Creamos una figura
figLic_presencial = go.Figure()
#Seleccionamos el 2019
dfLic2019 = df_Est_per[df_Est_per['Año'] == 2019]
#Separaremos las lic a distancia y las presenciales ya que ninguna tiene las dos moodalidades
dfLic2019_presencial = dfLic2019[dfLic2019['Modalidad'] == 'Presencial']
#Graficamos a presencial
figLic_presencial.add_trace(go.Bar(name= 'Presencial',
                 y=dfLic2019_presencial['Programa Académico'],
                 x=dfLic2019_presencial['Total'],
                 marker=dict(color=Colores),
                 visible=False,
                 orientation='h'

))
#----------------------------------------------------------------------------------------------------------------------------
#Ahora con el 2020
dfLic2020 = df_Est_per[df_Est_per['Año'] == 2020]
dfLic2020_presencial = dfLic2020[dfLic2020['Modalidad'] == 'Presencial']

#Graficamos a la modalidad presencial
figLic_presencial.add_trace(go.Bar(name= 'Presencial',
                 y=dfLic2020_presencial['Programa Académico'],
                 x=dfLic2020_presencial['Total'],
                 marker=dict(color=Colores),
                 visible=False,
                 orientation='h'
))

#---------------------------------------------------------------------------------------------------------------------------
#Ahora con el año 2021
#se debe mencionar que a partir de este año ya hay algunas licenciaturas que comparten dos modalidades
dfLic2021 = df_Est_per[df_Est_per['Año'] == 2021]
dfLic2021_presencial = dfLic2021[dfLic2021['Modalidad'] == 'Presencial']

#Graficamos la modalidad presencial
figLic_presencial.add_trace(go.Bar(name= 'Presencial',
                                   y=dfLic2021_presencial['Programa Académico'],
                                   x=dfLic2021_presencial['Total'],
                                   marker=dict(color=Colores),
                                   visible=False,
                                   orientation='h'
))
#------------------------------------------------------------------------------------------------------------------------
#Año 2022
dfLic2022 = df_Est_per[df_Est_per['Año'] == 2022]
dfLic2022_presencial = dfLic2022[dfLic2022['Modalidad'] == 'Presencial']
#Graficamos la modalidad presencial
figLic_presencial.add_trace(go.Bar(name= 'Presencial',
                                   y=dfLic2022_presencial['Programa Académico'],
                                   x=dfLic2022_presencial['Total'],
                                   marker=dict(color=Colores),
                                   visible=False,
                                   orientation='h'
))
#------------------------------------------------------------------------------------------------------------------------
#Año 2023
dfLic2023 = df_Est_per[df_Est_per['Año'] == 2023]
dfLic2023_presencial = dfLic2023[dfLic2023['Modalidad'] == 'Presencial']

#Graficamos para el año 2023
figLic_presencial.add_trace(go.Bar(name='Presencial',
                                   y=dfLic2023_presencial['Programa Académico'],
                                   x=dfLic2023_presencial['Total'],
                                   marker=dict(color=Colores),
                                   visible=False,
                                   orientation='h'
))
# ------------------------------------------------------------------------------------------------------------------------
#Año 2024
dfLic2024 = df_Est_per[df_Est_per['Año'] == 2024]
dfLic2024_presencial = dfLic2024[dfLic2024['Modalidad'] == 'Presencial']

#Graficamos para el año 2024
figLic_presencial.add_trace(go.Bar(name='Presencial',
                                   y=dfLic2024_presencial['Programa Académico'],
                                   x=dfLic2024_presencial['Total'],
                                   marker=dict(color=Colores),
                                   visible=True,
                                   orientation='h'
))

figLic_presencial.update_layout(
    title='Licenciaturas en la Modalidad Presencial',
    title_font=dict(size=20, color='black'),
    font=dict(family='New Times Roman', size=15, color='black'),
    width=1000,
    height=500,
    paper_bgcolor='white',
    plot_bgcolor='white'
)

#Creamos el Slider
Slider_Lic = []
for i, label in enumerate(['2019', '2020', '2021', '2022', '2023', '2024']):
    slider_lic = dict(
        method='update',
        label=label,
        args = [{"visible": [False] * len(figLic_presencial.data)}]
        )
    slider_lic['args'][0]['visible'][i] = True
    Slider_Lic.append(slider_lic)

figLic_presencial.update_layout(
    sliders=[dict(
        active=0,
        currentvalue={'prefix': 'Año:'},
        steps=Slider_Lic
)]
)
#----------------------------------------------------------------------------------------------------------------------
#Grafica de lineas de la matricula por unidad academica y su evolución
#Graficaremos solo el 2019 pero con barras
Colores2=['#283C55','#5E466E', '#B56576', '#E56B6F', '#EAAC8B','#353670','#6D3B7D', '#B84A81', '#D74456', '#F06E5A','#F0C949','#F1391C']
UA = go.Figure()
UA.add_trace(go.Scatter(
    x=df_Est_UA['Año'],
    y=df_Est_UA['Coyoacán'],
    name='Coyoacán',
    marker=dict(color=Colores2[0])
))
UA.add_trace(go.Scatter(
    x=df_Est_UA['Año'],
    y=df_Est_UA['Azcapotzalco'],
    name='Azcapotzalco',
    marker=dict(color=Colores2[1])
))
UA.add_trace(go.Scatter(
    x=df_Est_UA['Año'],
    y=df_Est_UA['Gustavo A. Madero'],
    name='Gustavo A. Madero',
    marker=dict(color=Colores2[2])
))
UA.add_trace(go.Scatter(
    x=df_Est_UA['Año'],
    y=df_Est_UA['Justo Sierra'],
    name='Justo Sierra',
    marker=dict(color=Colores2[3])
))
UA.add_trace(go.Scatter(
    x=df_Est_UA['Año'],
    y=df_Est_UA['La Magdalena Contreras'],
    name='Magdalena Contreras',
    marker=dict(color=Colores2[4])
))
UA.add_trace(go.Scatter(
    x=df_Est_UA['Año'],
    y=df_Est_UA['Milpa Alta'],
    name='Milpa Alta',
    marker=dict(color=Colores2[5])
))
UA.add_trace(go.Scatter(
    x=df_Est_UA['Año'],
    y=df_Est_UA['Casco Santo Tomás'],
    name='Casco de Santo Tomas',
    marker=dict(color=Colores2[6])
))
UA.add_trace(go.Scatter(
    x=df_Est_UA['Año'],
    y=df_Est_UA['Euzkadi'],
    name='Sub. Euzkadi',
    marker=dict(color=Colores2[7])
))
UA.add_trace(go.Scatter(
    x=df_Est_UA['Año'],
    y=df_Est_UA['Oceania'],
    name='Sub. Oceania',
    marker=dict(color=Colores2[8])
))
UA.add_trace(go.Scatter(
    x=df_Est_UA['Año'],
    y=df_Est_UA['Familia Juárez Maza'],
    name='Sub. Familia Juarez Maza',
    marker=dict(color=Colores2[9])
))
UA.add_trace(go.Scatter(
    x=df_Est_UA['Año'],
    y=df_Est_UA['Herrerías'],
    name='Sub. Herrerías',
    marker=dict(color=Colores2[10])
))
UA.add_trace(go.Scatter(
    x=df_Est_UA['Año'],
    y=df_Est_UA['Olímpica'],
    name='Sub. Olimpica. C.C',
    marker=dict(color=Colores2[11])
))
UA.update_layout(
    title='Matricula por Unidad Académica',
    title_font=dict(size=20, color='black'),
    font=dict(family='New Times Roman', size=15, color='black'),
    width=1000,
    height=500,
    paper_bgcolor='white',
    plot_bgcolor='white'
)
#--------------------------------------------------------------------------------------------------------------

#Grafica de las licencituras mas demandadas por unidad académica, selección de datos
#Seleccionamos a ls unidades academicas por separado
UA_LUA_Coy = df_Lic_UA[['Año','Programa Académico','Coyoacán']]
UA_LUA_Azc = df_Lic_UA[['Año','Programa Académico','Azcapotzalco']]
UA_LUA_Mad = df_Lic_UA[['Año','Programa Académico','Gustavo A. Madero']]
UA_LUA_Jas = df_Lic_UA[['Año','Programa Académico' ,'Justo Sierra']]
UA_LUA_Mag = df_Lic_UA[['Año','Programa Académico','Magdalena Contreras']]
UA_LUA_Cas = df_Lic_UA[['Año','Programa Académico','Casco de Santo Tomás']]
UA_LUA_Euz = df_Lic_UA[['Año','Programa Académico','Sub. Euzkadi']]
UA_LUA_Oce = df_Lic_UA[['Año','Programa Académico','Sub Oceania']]
UA_LUA_Fam = df_Lic_UA[['Año','Programa Académico','Sub. Familia Maza Juaréz']]
UA_LUA_Her = df_Lic_UA[['Año','Programa Académico','Sub. Herrerías']]
UA_LUA_Oli = df_Lic_UA[['Año','Programa Académico','Sub. Olimpica. C.C']]
#---------------------------------------------------------------------------------------------------------------------------
#Seleecionamos las 5 licenciaturas mas demandadas por año
UA_C5 = UA_LUA_Coy.groupby('Año').apply(lambda x: x.nlargest(5, 'Coyoacán')).reset_index(drop=True)
UA_A5 = UA_LUA_Azc.groupby('Año').apply(lambda x: x.nlargest(5, 'Azcapotzalco')).reset_index(drop=True)
UA_M5 = UA_LUA_Mad.groupby('Año').apply(lambda x: x.nlargest(5, 'Gustavo A. Madero')).reset_index(drop=True)
UA_J5 = UA_LUA_Jas.groupby('Año').apply(lambda x: x.nlargest(5, 'Justo Sierra')).reset_index(drop=True)
UA_Ma5 = UA_LUA_Mag.groupby('Año').apply(lambda x: x.nlargest(5, 'Magdalena Contreras')).reset_index(drop=True)
UA_CS5 = UA_LUA_Cas.groupby('Año').apply(lambda x: x.nlargest(5, 'Casco de Santo Tomás')).reset_index(drop=True)
UA_E5 = UA_LUA_Euz.groupby('Año').apply(lambda x: x.nlargest(5, 'Sub. Euzkadi')).reset_index(drop=True)
UA_O5 = UA_LUA_Oce.groupby('Año').apply(lambda x: x.nlargest(5, 'Sub Oceania')).reset_index(drop=True)
UA_FM5 = UA_LUA_Fam.groupby('Año').apply(lambda x: x.nlargest(5, 'Sub. Familia Maza Juaréz')).reset_index(drop=True)
UA_H5 = UA_LUA_Her.groupby('Año').apply(lambda x: x.nlargest(5, 'Sub. Herrerías')).reset_index(drop=True)
UA_Ol5 = UA_LUA_Oli.groupby('Año').apply(lambda x: x.nlargest(5, 'Sub. Olimpica. C.C')).reset_index(drop=True)

#---------------------------------------------------------------------------------------------------------------------------------
#Borramos el año 2023 por que no hay datos
UA_C5 = UA_C5[UA_C5['Año'] != 2023]
UA_A5 = UA_A5[UA_A5['Año'] != 2023]
UA_M5 = UA_M5[UA_M5['Año'] != 2023]
UA_J5 = UA_J5[UA_J5['Año'] != 2023]
UA_Ma5 = UA_Ma5[UA_Ma5['Año'] != 2023]
UA_CS5 = UA_CS5[UA_CS5['Año'] != 2023]
UA_E5 = UA_E5[UA_E5['Año'] != 2023]
UA_O5 = UA_O5[UA_O5['Año'] != 2023]
UA_FM5 = UA_FM5[UA_FM5['Año'] != 2023]
UA_H5 = UA_H5[UA_H5['Año'] != 2023]
UA_Ol5 = UA_Ol5[UA_Ol5['Año'] != 2023]
#---------------------------------------------------------------------------------------------------------------------------------
#Graficas de lineas
#Graficamos con grafica de lineas
fig_C5 = px.line(UA_C5,
              x='Año',
              y='Coyoacán',
              color='Programa Académico',
              labels={'Coyoacán': 'Número de Solicitudes', 'Año': 'Año', 'Programa Académico': 'Licenciatura'},
              markers=True)
#--------------------------------------------------------------------------------------------------------------------------------------
#Graficamos a la unidad de azcapotzalco
fig_A5 = px.line(UA_A5,
              x='Año',
              y='Azcapotzalco',
              color='Programa Académico',
              labels={'Azcapotzalco': 'Número de Solicitudes', 'Año': 'Año', 'Programa Académico': 'Licenciatura'},
              markers=True)
#-------------------------------------------------------------------------------------------------------------------------------------
#Graficamos la unidad de Gustavo A. Madero
fig_M5 = px.line(UA_M5,
              x='Año',
              y='Gustavo A. Madero',
              color='Programa Académico',
              labels={'Gustavo A. Madero': 'Número de Solicitudes', 'Año': 'Año', 'Programa Académico': 'Licenciatura'},
              markers=True)
#---------------------------------------------------------------------------------------------------------------------------------------
#Graficamos a justo sierra
fig_J5 = px.line(UA_J5,
              x='Año',
              y='Justo Sierra',
              color='Programa Académico',
              labels={'Justo Sierra': 'Número de Solicitudes', 'Año': 'Año', 'Programa Académico': 'Licenciatura'},
              markers=True)
#---------------------------------------------------------------------------------------------------------------------------------------
#Graficamos a Magdalena contreras
fig_Ma5 = px.line(UA_Ma5,
              x='Año',
              y='Magdalena Contreras',
              color='Programa Académico',
              labels={'Magdalena Contreras': 'Número de Solicitudes', 'Año': 'Año', 'Programa Académico': 'Licenciatura'},
              markers=True)
#---------------------------------------------------------------------------------------------------------------------------------------
#Graficamos a casco de santo tomas
fig_CS5 = px.line(UA_CS5,
              x='Año',
              y='Casco de Santo Tomás',
              color='Programa Académico',
              labels={'Casco de Santo Tomás': 'Número de Solicitudes', 'Año': 'Año', 'Programa Académico': 'Licenciatura'},
              markers=True)
#---------------------------------------------------------------------------------------------------------------------------------------
#Graficamos Euzcadi
fig_E5 = px.line(UA_E5,
              x='Año',
              y='Sub. Euzkadi',
              color='Programa Académico',
              labels={'Sub. Euzkadi': 'Número de Solicitudes', 'Año': 'Año', 'Programa Académico': 'Licenciatura'},
              markers=True)
#---------------------------------------------------------------------------------------------------------------------------------------
#Graficamos a Oceania
fig_O5 = px.line(UA_O5,
              x='Año',
              y='Sub Oceania',
              color='Programa Académico',
              labels={'Sub Oceania': 'Número de Solicitudes', 'Año': 'Año', 'Programa Académico': 'Licenciatura'},
              markers=True)
#----------------------------------------------------------------------------------------------------------------------------------------
#Graficamos juarez maza
fig_FM5 = px.line(UA_FM5,
              x='Año',
              y='Sub. Familia Maza Juaréz',
              color='Programa Académico',
              labels={'Sub. Familia Maza Juaréz': 'Número de Solicitudes', 'Año': 'Año', 'Programa Académico': 'Licenciatura'},
              markers=True)
#---------------------------------------------------------------------------------------------------------------------------------------------
#Graficamos a las herrerias
fig_H5 = px.line(UA_H5,
              x='Año',
              y='Sub. Herrerías',
              color='Programa Académico',
              labels={'Sub. Herrerías': 'Número de Solicitudes', 'Año': 'Año', 'Programa Académico': 'Licenciatura'},
              markers=True)
#---------------------------------------------------------------------------------------------------------------------------------------------
#Graficamos olimpica
fig_Ol5 = px.line(UA_Ol5,
              x='Año',
              y='Sub. Olimpica. C.C',
              color='Programa Académico',
              labels={'Sub. Olimpica. C.C': 'Número de Solicitudes', 'Año': 'Año', 'Programa Académico': 'Licenciatura'},
              markers=True)
#Dropdown
#Hacemos el Dropdown
fig_top5 = go.Figure()

Lista_Top5 = [fig_A5, fig_C5, fig_M5, fig_J5, fig_Ma5, fig_CS5, fig_E5, fig_O5, fig_FM5, fig_H5, fig_Ol5]
labels_top5 = ['Azcapotzalco', 'Coyoacán', 'Gustavo A. Madero', 'Justo Sierra', 'Magdalena Contreras',
               'Casco de Santo Tomás', 'Sub. Euzkadi', 'Sub Oceania', 'Sub. Familia Maza Juaréz',
               'Sub. Herrerías', 'Sub. Olimpica. C.C']

color_index = 0
for i, Fig_5 in enumerate(Lista_Top5):
    for trace in Fig_5.data:
        trace.visible = True if i == 0 else False
        if hasattr(trace, 'line'):
            trace.line.color = Colores[color_index % len(Colores)]
        if hasattr(trace, 'marker'):
            trace.marker.color = Colores[color_index % len(Colores)]
        fig_top5.add_trace(trace)
        color_index += 1

n_traces = [len(Fig_5.data) for Fig_5 in Lista_Top5]
n_total_traces = sum(n_traces)

# Creamos los botones del dropdown
boton_top5 = []
start = 0
for i, label in enumerate(labels_top5):
    visible = [False] * n_total_traces
    for j in range(n_traces[i]):
        visible[start + j] = True
    button = dict(
        label=label,
        method="update",
        args=[{"visible": visible},
              {"title": f"5 Licenciaturas mas Demandadas en la Unidad Académica de {label}"}]
    )
    boton_top5.append(button)
    start += n_traces[i]

# Añadimos el menu
fig_top5.update_layout(
    updatemenus=[
        dict(
            buttons=boton_top5,
            direction="down",
            showactive=True,
            x=0.5,
            xanchor="center",
            y=1.1,
            yanchor="top"
        )
    ],#Le Damos formato a las graficas
    title="5 Licenciaturas mas Demandadas por Año y Unidad Académica",
    title_x=0.5,
    width=900,
    height=600,
    paper_bgcolor='white',
    plot_bgcolor='white',
    font=dict(family='New Times Roman', size=15, color='black'),
    xaxis = dict(title='Año'),
    yaxis = dict(title='Demanda')
)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

layout = html.Div([
    html.H1("Información General de la UNRC", className="text-center my-4"),
    html.P("La Universidad Rosario Castellanos (UNRC) es una institución pública que busca ampliar el acceso a la educación superior en la Ciudad de México."),
    dcc.Graph(figure=fig_ODE),
    
    html.H2("Asiprantes PIRC, Seleccionados"),
    dcc.Graph(figure=figLic_presencial),
    
    html.H2("UA"),
    dcc.Graph(figure=UA),
    
    html.H2("Top 5"),
    dcc.Graph(figure=fig_top5)
])