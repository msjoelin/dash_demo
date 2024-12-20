from dash import Dash, html, dcc, callback, Output, Input
# import plotly.express as px
import pandas as pd
import os

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    # Uncomment the following lines if you want to use the dropdown and graph
    # dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    # dcc.Graph(id='graph-content')
])

# @callback(
#     Output('graph-content', 'figure'),
#     Input('dropdown-selection', 'value')
# )
# def update_graph(value):
#     dff = df[df.country==value]
#     return px.line(dff, x='year', y='pop')




if __name__ == '__main__':
    # port = int(os.getenv("PORT", 8050))
    app.run_server(debug=True)