# Written by: Gregoria Ramirez
# Course: CS-499 Computer Science Capstone
# Description: Sets up all app callbacks for table, chart, and map interactivity.

# Enhancements (Software Design and Engineering):
# - Moved all callback logic into a separate controller file to support MVC structure.
# - Wrapped all callbacks inside register_callbacks(app) to keep things modular and reusable.
# - Kept each section (table, chart, map) in its own callback for clean layout and easier updates.
# - Used clear variable names and organized logic for better readability and debugging.
# Original version written in Feb 2025 and enhanced for the final capstone.

from dash.dependencies import Input, Output
from dash import html, dcc
import pandas as pd
import dash_leaflet as dl
import plotly.express as px
from model import get_data

# Enhancement (Software Design and Engineering): Keep data retrieval separate from UI logic
df = get_data()

# Enhancement (Software Design and Engineering): All callbacks organized into one function for structure and reuse
def register_callbacks(app):
    
    # Enhancement (Software Design and Engineering): Handles all data table filtering logic in one callback
    @app.callback(
        Output('datatable-id', 'data'),
        [Input('filter-type', 'value'),
         Input('color-filter', 'value'),
         Input('breed-filter', 'value')]
    )
    def update_dashboard(filter_type, selected_colors, selected_breeds):
        filtered_df = df.copy()

        # Structured conditional logic to filter based on rescue type
        if filter_type == 'water':
            filtered_df = filtered_df[(filtered_df['breed'].str.contains('Labrador Retriever', na=False)) &
                                      (filtered_df['outcome_type'] == 'Euthanasia') &
                                      (filtered_df['animal_type'] == 'Dog')]
        elif filter_type == 'mount':
            filtered_df = filtered_df[(filtered_df['outcome_type'] == 'Transfer') &
                                      (filtered_df['animal_type'] == 'Cat') &
                                      (filtered_df['sex_upon_outcome'].str.contains('Female', na=False)) &
                                      (filtered_df['age_upon_outcome_in_weeks'].between(52, 260))]
        elif filter_type == 'disaster':
            filtered_df = filtered_df[(filtered_df['animal_type'] == 'Dog') &
                                      (filtered_df['age_upon_outcome_in_weeks'].between(52, 260)) &
                                      (filtered_df['sex_upon_outcome'].str.contains('Male', na=False)) &
                                      (filtered_df['outcome_type'].isin(['Adoption', 'Transfer']))]
        
        # Enhancement (Algorithms and Data Structures): Additional filters added for breed and color
        if selected_colors:
            filtered_df = filtered_df[filtered_df['color'].isin(selected_colors)]
        if selected_breeds:
            filtered_df = filtered_df[filtered_df['breed'].isin(selected_breeds)]

        return filtered_df.to_dict('records')

    # Enhancement (Software Design and Engineering): Handles chart creation separately for modular updates
    @app.callback(
        Output('chart-id', 'children'),
        [Input('datatable-id', 'data'), Input('filter-type', 'value')]
    )
    def update_chart(data, filter_type):
        dff = pd.DataFrame(data)
        if dff.empty:
            return html.Div("No data available for chart.")

        breed_counts = dff['breed'].value_counts().reset_index()
        breed_counts.columns = ['breed', 'count']

        if filter_type == 'mount':
            fig = px.pie(breed_counts, names='breed', values='count', title='Mountain Rescue')
        elif filter_type == 'disaster':
            fig = px.bar(breed_counts, x='breed', y='count', title='Disaster Rescue')
        elif filter_type == 'reset':
            fig = px.bar(breed_counts, x='breed', y='count', title='Unfiltered View')
        else:
            fig = px.pie(breed_counts, names='breed', values='count', title='Water Rescue')

        return dcc.Graph(figure=fig)

    # Enhancement (Software Design and Engineering): Keeps map logic separated for clarity and reuse
    @app.callback(
        Output('map-id', "children"),
        [Input('datatable-id', "derived_virtual_data"),
         Input('datatable-id', "derived_virtual_selected_rows")]
    )
    def update_map(viewData, index):
        if viewData is None or not index:
            return []

        dff = pd.DataFrame(viewData)
        row = index[0]

        lat = dff.iloc[row].get("location_lat", 30.75)
        lon = dff.iloc[row].get("location_long", -97.48)
        animal_name = dff.iloc[row].get("name", "Unknown")
        breed = dff.iloc[row].get("breed", "Unknown")

        return [
            dl.Map(style={'width': '1000px', 'height': '500px'},
                   center=[lat, lon], zoom=10, children=[
                       dl.TileLayer(id="base-layer-id"),
                       dl.Marker(position=[lat, lon],
                                 children=[
                                     dl.Tooltip(breed),
                                     dl.Popup([html.H1("Animal Name"), html.P(animal_name)])
                                 ])
                   ])
        ]
