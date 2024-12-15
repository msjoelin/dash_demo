import dash
from dash import html, dcc
import pandas as pd



# Create a sample DataFrame
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Grapes"],
    "Amount": [4, 1, 2, 3]
})

# Initialize the Dash app
dash_app = dash.Dash(__name__)
server=dash_app.server

# Define the layout
dash_app.layout = html.Div([
    html.H1("My Super Basic Dash App"),
    html.Div("This is a simple bar chart:"),
])

# Run the app
if __name__ == "__main__":
    dash_app.run_server(debug=True)
