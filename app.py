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
users['gender'] = users['gender']

# Create a simple bar plot for age
fig_age = px.bar(users, x='name.first', y='age', title="Users' Age Distribution NEW TITLE")

# Create a simple pie plot for gender
fig_gender = px.pie(users, names='gender', title="Users' Gender Distribution")


# Define the app layout
app.layout = html.Div([
    html.H1("Random User Data", id='title'),
    
    # Radio Button for dynamic title and plot change
    dcc.RadioItems(
        id='title-selector',
        options=[
            {'label': 'Age Distribution', 'value': 'Age Distribution'},
            {'label': 'Gender Distribution', 'value': 'Gender Distribution'}
        ],
        value='Age Distribution',
        labelStyle={'display': 'inline-block'}
    ),
    
    # Graph
    dcc.Graph(
        id='user-plot',
        figure=fig_age  # default figure
    )
])

# Define the callback to change both the title and the plot
@app.callback(
    [dash.dependencies.Output('title', 'children'),
     dash.dependencies.Output('user-plot', 'figure')],
    [dash.dependencies.Input('title-selector', 'value')]
)
def update_content(selected_value):
    if selected_value == 'Age Distribution':
        return "Random User Data - Age Distribution", fig_age
    else:
        return "Random User Data - Gender Distribution", fig_gender

if __name__ == '__main__':
    app.run_server(debug=True)