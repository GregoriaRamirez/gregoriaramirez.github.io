# Written by: Gregoria Ramirez
# Course: CS-499 Computer Science Capstone
# Description: Defines the layout of the Dash web interface.

# Enhancements (Software Design and Engineering):
# - Moved the layout into its own file to follow the MVC design pattern and make the app more organized.
# - Automatically generated dropdown options using values from the live dataset to avoid hardcoding.
# - Structured the interface using flexible layout features so the UI looks cleaner and is easier to update.
# Original version written in Feb 2025 and updated by me for the final capstone.

from dash import html, dcc, dash_table
import base64
from model import get_data

df = get_data()

# Encode the logo image from the assets folder
image_filename = 'assets/Grazioso Salvare Logo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode()

# Define the layout
layout = html.Div([

    # Title centered
    html.Center(html.B(html.H1('SNHU CS-340 Gregoria Ramirez'))),

    # Centered logo
    html.Div(
        children=html.Img(
            src='data:image/png;base64,{}'.format(encoded_image),
            style={'width': '200px', 'display': 'block', 'margin': '0 auto'}
        )
    ),

    html.Hr(),

    # Controls row: Radio buttons (left) and filters (right)
    html.Div(style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '20px'}, children=[

        # Left side: Radio buttons stacked
        html.Div([
            dcc.RadioItems(
                id='filter-type',
                options=[
                    {'label': 'Water Rescue', 'value': 'water'},
                    {'label': 'Mountain or Wilderness Rescue', 'value': 'mount'},
                    {'label': 'Disaster or Individual Tracking', 'value': 'disaster'},
                    {'label': 'Reset', 'value': 'reset'}
                ],
                value='reset',
                labelStyle={'display': 'block'}
            )
        ], style={'width': '40%'}),
        
        # Enhancement (Software Design and Engineering):
        # The dropdown options for color and breed are pulled from the actual dataset.
        # This keeps the UI up to date with the data and makes maintenance easier.

        # Right side: Filters stacked and shifted left slightly
        html.Div([
            dcc.Dropdown(
                id='color-filter',
                options=[{'label': color, 'value': color} for color in df['color'].unique()],
                multi=True,
                placeholder="Select colors",
                style={'width': '220px', 'marginBottom': '10px'}
            ),
            dcc.Dropdown(
                id='breed-filter',
                options=[{'label': breed, 'value': breed} for breed in df['breed'].unique()],
                multi=True,
                placeholder="Select breeds",
                style={'width': '220px'}
            )
        ], style={
            'width': '40%',
            'marginLeft': '40px'
        })
    ]),

    # DataTable
    dash_table.DataTable(
        id='datatable-id',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        row_selectable='single',
        filter_action='native',
        sort_action='native',
        page_size=15,
        style_table={'overflowX': 'auto'}
    ),

    # Row for charts and map
    html.Div(className='row', style={'display': 'flex'}, children=[
        html.Div(id='chart-id', className='col s12 m6'),
        html.Div(id='map-id', className='col s12 m6'),
    ])
])
