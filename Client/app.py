## The dash code will be here

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

external_stylesheets =  [   
                            'https://codepen.io/chriddyp/pen/bWLwgP.css',
                        ]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, title='Smart City Simulation')

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
df = pd.DataFrame(dict(
    overall = [4, 6, 1, 3],
    solar = [1, 3, 2, 4],
    wind = [1, 2, 3, 4],
    houses = [2, 3, 4, 5]
))

fig = px.line(df,) 

# fig.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )

app.layout = html.Div(children=[
                html.H1(children='Smart City Simulation'),
                html.Div(id='my-output'),
                html.Div([
                    html.Div([
                        html.H3(children='Overall Electricity Generation and Usage'),

                        dcc.Checklist(
                            options=[
                                {'label': 'Overall', 'value': 'overall'},
                            ],
                            value=['overall'],
                            id = "overall"
                        ),

                        html.H3(children='Electricty Generators'),
                        
                        dcc.Checklist(
                            options=[
                                {'label': 'Solar', 'value': 'solar'},
                                {'label': 'Wind', 'value': 'wind'},
                            ],
                            value=['solar', 'wind'],
                            id = "generators"
                        ),

                        html.H3(children='Electricty Users'),
                        
                        dcc.Checklist(
                            options=[
                                {'label': 'Business', 'value': 'business'},
                                {'label': 'House', 'value': 'house'},
                                {'label': 'Infrastructure', 'value': 'infrastructure'},
                                {'label': 'Vehicle', 'value': 'vehicle'}
                            ],
                            value=['business', 'house', 'infrastructure', 'vehicle'],
                            id = "users"
                        ),
                    ], className='five columns userInput'),
                    html.Div([
                        html.H3(children='Simulation'),
                        dcc.Graph(
                            id='graph',
                            figure=fig
                        ),  
                    ], className='seven columns'),
                ], className='row'),
            ])

@app.callback(
    Output('my-output', 'children'),
    Input('overall', 'value'),
    Input('generators', 'value'),
    Input('users', 'value'),
)
def update_output_div(overall, generators, users):
    inputs = []

    inputs += overall
    inputs += generators
    inputs += users

    print(inputs)

    return

if __name__ == '__main__':
    app.run_server(debug=True)
