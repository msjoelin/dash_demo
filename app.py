import dash
from dash import dcc, html
import plotly.express as px
import requests
import pandas as pd

# Create Dash app
app = dash.Dash(__name__)

# Fetch data from an API
response = requests.get('https://randomuser.me/api/?results=10')
data = response.json()

# Convert the fetched data into a pandas DataFrame
users = pd.json_normalize(data['results'])
users['age'] = users['dob.age']

# Create a simple plot
fig = px.bar(users, x='name.first', y='age', title="Users' Age Distribution")

# Define the app layout
app.layout = html.Div([
    html.H1("Random User Data", id='title'),
    
    # Radio Button for dynamic title change
    dcc.RadioItems(
        id='title-selector',
        options=[
            {'label': 'Age Distribution', 'value': 'Age Distribution'},
            {'label': 'User Information', 'value': 'User Info'}
        ],
        value='Age Distribution',
        labelStyle={'display': 'inline-block'}
    ),
    
    # Graph
    dcc.Graph(
        id='user-plot',
        figure=fig
    )
])

# Define the callback to change the title
@app.callback(
    dash.dependencies.Output('title', 'children'),
    [dash.dependencies.Input('title-selector', 'value')]
)
def update_title(selected_value):
    return f"Random User Data - {selected_value}"

if __name__ == '__main__':
    app.run_server(debug=True)
