from app import app

from dash import html, dcc, callback, Output, Input, State
from src.components.layout import create_layout

app.layout = create_layout(app)


@app.callback(
    [
        Output("sidebar", "className"),
        Output("main", "className"),
    ],
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className"), State("main", "className")],
)
def toggle_sidebar(n_clicks, sidebar_class, main_class):
    if n_clicks:
        if "sidebar-visible" in sidebar_class:
            return "sidebar sidebar-hidden", "main-expanded"
        else:
            return "sidebar sidebar-visible", "main"
    else:
        return sidebar_class, main_class


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
