## The dash code will be here

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
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

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(children=[
                html.H1(children='Smart City Simulation'),
                html.Div([
                    html.Div([
                        html.H3(children='Variables'),

                        # Houses
                        html.Div(children='''
                            Houses
                        '''),

                        dcc.Dropdown(   id='dropdownHouse',
                                        style={"color": "black"},
                                        options=[
                                            { 'label': 'Item 1', 'value': 'foo' },
                                            { 'label': 'Item 2', 'value': 'bar' },
                                        ],
                        ),

                        # Houses
                        html.Div(children='''
                            Business
                        '''),

                        dcc.Dropdown(   id='dropdownBusiness',
                                        style={"color": "black"},
                                        options=[
                                            { 'label': 'Item 1', 'value': 'foo' },
                                            { 'label': 'Item 2', 'value': 'bar' },
                                        ],
                        ),

                        # Houses
                        html.Div(children='''
                            Infrastructure
                        '''),

                        dcc.Dropdown(   id='dropdownInfrastructure',
                                        style={"color": "black"},
                                        options=[
                                            { 'label': 'Item 1', 'value': 'foo' },
                                            { 'label': 'Item 2', 'value': 'bar' },
                                        ],
                        ),
                    ], className='four columns userInput'),
                    html.Div([
                        html.H3(children='Results'),
                        dcc.Graph(
                            id='graph2',
                            figure=fig
                        ),  
                    ], className='eight columns'),
                ], className='row'),
            ])

if __name__ == '__main__':
    app.run_server(debug=True)
