from dash import Dash, html
import dash_bootstrap_components as dbc

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-gov.min.css",  # Pretendard Gov 가변
    "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css",  # Pretendard 다이나믹 서브셋
    "https://fonts.googleapis.com/earlyaccess/notosanskr.css",  # Noto Sans KR 폰트
    "https://fonts.googleapis.com/css2?family=Roboto&display=swap",  # Roboto 폰트
]

app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)

# app.title = "법령사무총조사"

app.config.suppress_callback_exceptions = True
