from dash import Dash, html, dcc, page_container
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.H3("법령사무총조사", className="home-logo"),
        html.Hr(),
        html.P("2023.12.28.", className="home-explanation"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/home", active="exact"),
                dbc.NavLink("모델예측", href="/prediction", active="exact"),
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            title="데이터",
                            children=[
                                dbc.NavLink(
                                    "데이터원본",
                                    href="/data_source/dataframe",
                                    active="exact",
                                ),
                                dbc.NavLink(
                                    "데이터설명서",
                                    href="/data_source/codebook",
                                    active="exact",
                                ),
                                dbc.NavLink(
                                    "데이터사전",
                                    href="/data_source/dictionary",
                                    active="exact",
                                ),
                                dbc.NavLink(
                                    "EDA",
                                    href="/data_source/eda",
                                    active="exact",
                                ),
                                dbc.NavLink(
                                    "설정",
                                    href="/data_source/setting",
                                    active="exact",
                                ),
                            ],
                        ),
                    ]
                ),
            ],
            className="navigator",
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar sidebar-visible",
    id="sidebar",
)

header = html.Div(
    [
        html.Button(
            html.Img(src="/assets/menu-button.png", height="20px"), id="sidebar-toggle"
        )
    ],
    className="header",
)

main = html.Div([dbc.Row(header), dbc.Row(page_container)], className="main", id="main")


def create_layout(app: Dash) -> html.Div:
    return html.Div([dbc.Container([dbc.Col(sidebar), dbc.Col(main)])])
