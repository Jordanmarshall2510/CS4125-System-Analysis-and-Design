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
from client.grapher import Grapher

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
                        html.H6(children='Overall'),

                        dcc.Checklist(
                            options=[
                                {'label': 'Overall Generation', 'value': 'Overall Generation'},
                                {'label': 'Overall Usage', 'value': 'Overall Usage'},
                            ],
                            id = "overall"
                        ),

                        html.H6(children='Electricity Generators'),
                        
                        dcc.Checklist(
                            options=[
                                {'label': 'Solar', 'value': 'Solar'},
                                {'label': 'Wind', 'value': 'Wind'},
                            ],
                            id = "generators"
                        ),

                        html.H6(children='Electricity Users'),
                        
                        dcc.Checklist(
                            options=[
                                {'label': 'Business', 'value': 'Business'},
                                {'label': 'House', 'value': 'House'},
                                {'label': 'Infrastructure', 'value': 'Infrastructure'},
                                {'label': 'Vehicle', 'value': 'Vehicle'}
                            ],
                            id = "users"
                        ),

                        html.H3(children='Session Information'),
                        html.Table([
                                    html.Tr([html.Td("Business: "), html.Td(id='business')]),
                                    html.Tr([html.Td("House: "), html.Td(id='house')]),
                                    html.Tr([html.Td("Infrastructure: "), html.Td(id='infrastructure')]),
                                    html.Tr([html.Td("Vehicles: "), html.Td(id='vehicles')]),
                                    html.Tr([html.Td("Solar: "), html.Td(id='solar')]),
                                    html.Tr([html.Td("Wind: "), html.Td(id='wind')]),
                                    html.Tr([html.Td("Time: "), html.Td(id='time')]),                   
                        ]),

                    ], className='three columns userInput'),
                    html.Div([
                        html.H3(children='Simulation'),
                        dcc.Graph(
                            id='graph',
                        ), 
                        html.H3(children='Statistics'),
                        html.Div([
                            html.Div([
                                html.H6("Generated"),
                                html.Table([
                                    html.Tr([html.Td("Selected: "), html.Td(id='generated_selected')]),
                                    html.Tr([html.Td("Total Generated: "), html.Td(id='total_generated')]),
                                ]),
                            ],className='six columns'),
                            html.Div([
                                html.H6("Usage"),
                                html.Table([
                                    html.Tr([html.Td("Selected: "), html.Td(id='usage_selected')]),
                                    html.Tr([html.Td("Total Usage: "), html.Td(id='total_usage')]),
                                ]),
                            ],className='six columns')
                        ],className='row'),
                    ], className='nine columns'),
                ], className='row'),
            ])

@app.callback(
    Output('graph', 'figure'),
    Output("generated_selected", "children"),
    Output("usage_selected", "children"),
    Output("total_generated", "children"),
    Output("total_usage", "children"),
    Output("business", "children"),
    Output("house", "children"),
    Output("infrastructure", "children"),
    Output("vehicles", "children"),
    Output("solar", "children"),
    Output("wind", "children"),
    Output("time", "children"),
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

    sim_graph, selected_generated, selected_usage, total_generated, total_usage = graph.create_df(inputs)
    fig = px.line(sim_graph) 

    business, house, infrastructure, vehicles, solar, wind, time = graph.get_session_data()

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

    return  fig, ", ".join(selected_generated), ", ".join(selected_usage), f"{int(total_generated):,}" + " kW", f"{int(total_usage):,}" + " kW", business, house, infrastructure, vehicles, solar, wind, time

if __name__ == '__main__':
    app.run_server(debug=True)
