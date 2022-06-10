from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate



############################################################### FRONT END ###################################################################################################




app = Dash(__name__)
server = app.server

app.layout = html.Div("HW")


if __name__ == '__main__':
  app.run_server(debug = False)
