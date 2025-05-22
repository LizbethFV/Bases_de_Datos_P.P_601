import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div([
    html.H1("Blog educativo UNRC", style={'textAlign': 'center'}),
    
    # Menú de navegación
    html.Div([
        dcc.Link("Inicio", href="/", style={'marginRight': '20px'}),
        dcc.Link("CECATI", href="/CECATI", style={'marginRight': '20px'}),
        dcc.Link("Otra página", href="/otra", style={'marginRight': '20px'}),
    ], style={'textAlign': 'center'}),
    
    html.Hr(),

    dash.page_container  # Aquí se cargan las páginas registradas
])

if __name__ == "__main__":
    app.run(debug=True)

dbc.Button("Ir a CECATI", href="/CECATI", color="primary", className="me-2")
