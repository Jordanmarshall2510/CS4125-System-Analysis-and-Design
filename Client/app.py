## The dash code will be here

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash.dcc.Graph import Graph
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from grapher import Grapher

graph = Grapher()

external_stylesheets =  [   
                            'https://codepen.io/chriddyp/pen/bWLwgP.css',
                        ]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, title='Smart City Simulation')

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
                html.H1(children='Smart City Simulation'),
                html.Div(id='my-output'),
                html.Div([
                    html.Div([
                        html.H3(children='Overall Electricity Generation and Usage'),

                        dcc.Checklist(
                            options=[
                                {'label': 'Overall', 'value': 'Overall'},
                            ],
                            id = "overall"
                        ),

                        html.H3(children='Electricty Generators'),
                        
                        dcc.Checklist(
                            options=[
                                {'label': 'Solar', 'value': 'Solar'},
                                {'label': 'Wind', 'value': 'Wind'},
                            ],
                            id = "generators"
                        ),

                        html.H3(children='Electricty Users'),
                        
                        dcc.Checklist(
                            options=[
                                {'label': 'Business', 'value': 'Business'},
                                {'label': 'House', 'value': 'House'},
                                {'label': 'Infrastructure', 'value': 'Infrastructure'},
                                {'label': 'Vehicle', 'value': 'Vehicle'}
                            ],
                            id = "users"
                        ),
                    ], className='five columns userInput'),
                    html.Div([
                        html.H3(children='Simulation'),
                        dcc.Graph(
                            id='graph',
                        ),  
                    ], className='seven columns'),
                ], className='row'),
            ])

@app.callback(
    Output('graph', 'figure'),
    Input('overall', 'value'),
    Input('generators', 'value'),
    Input('users', 'value'),
)
def update_output_div(overall, generators, users):
    inputs = []

    if overall:
        inputs += overall
    if generators:
        inputs += generators
    if users:
        inputs += users

    print(inputs)
    
    fig = px.line(graph.createDF(inputs)) 

    fig.update_layout(
        # plot_bgcolor=colors['background'],
        # paper_bgcolor=colors['background'],
        # font_color=colors['text']

        xaxis_title="Time",
        yaxis_title="Electricity (kW)",
        legend_title="Types",
        font=dict(
            size=16,
        )
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
