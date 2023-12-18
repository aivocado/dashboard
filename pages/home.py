import dash
from dash import dcc, html

dash.register_page(__name__)

layout = html.Div([dcc.Markdown("# EDA Testing")])
