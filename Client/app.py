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
                html.Div([
                    html.Div([
                        html.H3(children='Options'),
                        html.H4(children='Overall'),

                        dcc.Checklist(
                            options=[
                                {'label': 'Overall Generation', 'value': 'Overall Generation'},
                                {'label': 'Overall Usage', 'value': 'Overall Usage'},
                            ],
                            id = "overall"
                        ),

                        html.H4(children='Electricity Generators'),
                        
                        dcc.Checklist(
                            options=[
                                {'label': 'Solar', 'value': 'Solar'},
                                {'label': 'Wind', 'value': 'Wind'},
                            ],
                            id = "generators"
                        ),

                        html.H4(children='Electricity Users'),
                        
                        dcc.Checklist(
                            options=[
                                {'label': 'Business', 'value': 'Business'},
                                {'label': 'House', 'value': 'House'},
                                {'label': 'Infrastructure', 'value': 'Infrastructure'},
                                {'label': 'Vehicle', 'value': 'Vehicle'}
                            ],
                            id = "users"
                        ),
                    ], className='four columns userInput'),
                    html.Div([
                        html.H3(children='Simulation'),
                        dcc.Graph(
                            id='graph',
                        ), 
                        html.H3(children='Statistics'),
                        html.Div([
                            html.Div([
                                html.H5("Generated"),
                                html.Table([
                                    html.Tr([html.Td("Selected: "), html.Td(id='generated_selected')]),
                                    html.Tr([html.Td("Total Generated: "), html.Td(id='total_generated')]),
                                ]),
                            ],className='six columns'),
                            html.Div([
                                html.H5("Usage"),
                                html.Table([
                                    html.Tr([html.Td("Selected: "), html.Td(id='usage_selected')]),
                                    html.Tr([html.Td("Total Usage: "), html.Td(id='total_usage')]),
                                ]),
                            ],className='six columns')
                        ],className='row'),
                    ], className='eight columns'),
                ], className='row'),
            ])

@app.callback(
    Output('graph', 'figure'),
    Output("generated_selected", "children"),
    Output("usage_selected", "children"),
    Output("total_generated", "children"),
    Output("total_usage", "children"),
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
    sim_graph, selected_generated, selected_usage, total_generated, total_usage = graph.createDF(inputs)
    fig = px.line(sim_graph) 

    fig.update_layout(
        # plot_bgcolor=colors['background'],
        # paper_bgcolor=colors['background'],
        # font_color=colors['text']

        xaxis_title="Time",
        yaxis_title="Electricity (kW)",
        legend_title="Types",
        font=dict(
            size=12,
        )
    )

    return  fig, ", ".join(selected_generated), ", ".join(selected_usage), f"{int(total_generated):,}" + " kW", f"{int(total_usage):,}" + " kW"

if __name__ == '__main__':
    app.run_server(debug=True)
