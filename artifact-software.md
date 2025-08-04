
# 🧩 Software Design & Engineering Artifact

## 📌 Artifact Description

For my CS 499 Capstone, I chose to enhance my Animal Shelter Dashboard project originally created in February 2025
for CS 340: Client-Server Development. This web application was built in a Jupyter Notebook using Python, Dash, and MongoDB.
It pulled data from a CSV file into a NoSQL database and displayed animal outcome data through an interactive dashboard.
Features included a searchable table, visual charts, and filters for outcome type, breed, color, and shelter type.
The project implemented CRUD operations to query the database for various types of analysis.

## 📎 Justification for Inclusion

I selected this artifact because it integrates everything I have learned about software engineering — from backend data handling
to frontend dashboard design — all connected via Python. The project demonstrates my ability to:

* Structure and organize code for maintainability
* Secure sensitive data
* Build a responsive and intuitive user interface

The original version functioned correctly, but lacked modular design, security practices, and clean separation of concerns,
making it a strong candidate for enhancement.

## 🔧 Enhancement Overview

Key software engineering improvements include:

* Reorganizing the codebase into a modular MVC-style structure (model, controller, and dashboard logic split into separate files)
* Replacing hardcoded credentials with secure environment variables using `python-dotenv`
* Adding application logging to support better debugging and error tracking
* Isolating Dash callback functions into a separate controller module for clarity
* Enhancing the visual presentation of charts and layout responsiveness
* Adding new filtering options for breed and color
* Implementing a `venv` virtual environment for dependency management

These changes improved the maintainability, security, and professionalism of the project.

## 💡 Code Snippets Demonstrating Enhancements

### 🧩 Snippet 1: Modular Entry Point (`app.py`)

```python
from dash import Dash
from model.view import layout
from controller import register_callbacks

app = Dash(__name__)
app.layout = layout

register_callbacks(app)

app.run(debug=True, port=8550)
```

**Enhancement Summary:**
This code demonstrates improved software design through the use of modular architecture.
The layout is loaded from a separate view file, and callbacks are managed in a separate controller module.
This structure follows the Model-View-Controller (MVC) pattern, making the application more organized, maintainable, and scalable.
Additionally, it uses the modern `app.run()` method instead of the deprecated `run_server()`, aligning with current Dash best practices.

---

### 🧩 Snippet 2: Callback Logic (`controller.py`)

```python
from dash.dependencies import Input, Output
from dash import html, dcc
import pandas as pd
import plotly.express as px
from model import get_data

# Enhancement (Software Design and Engineering): Data and logic separation using MVC
df = get_data()

# Enhancement (Software Design and Engineering): Centralized callback registration for reuse and clarity
def register_callbacks(app):

    @app.callback(
        Output('datatable-id', 'data'),
        [Input('filter-type', 'value'),
         Input('color-filter', 'value'),
         Input('breed-filter', 'value')]
    )
    def update_dashboard(filter_type, selected_colors, selected_breeds):
        filtered_df = df.copy()
        return filtered_df.to_dict('records')

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
        fig = px.pie(breed_counts, names='breed', values='count', title='Breed Distribution')
        return dcc.Graph(figure=fig)
```

**Enhancement Summary:**
This code introduces a modular structure using a `register_callbacks()` function to group all callback logic in one place.
By keeping table and chart logic cleanly separated and centralized, this approach supports maintainability and reduces duplicate logic.
The design aligns with software engineering principles like separation of concerns and modular reuse, making the application easier to scale and debug.

---

### 🧩 Snippet 3: Secure Map Callback (`controller.py`)

```python
import dash_leaflet as dl

# Map callback - handles user selection from the data table
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
```

**Enhancement Summary:**
This map callback was intentionally separated from the rest of the logic to support clarity, reuse, and single-responsibility principles.
It makes the mapping logic easier to manage independently from charts and tables, which aligns with the modular design pattern used throughout the application.
This structural decision supports flexible future enhancements, such as location clustering or advanced geospatial features.

---

## 📁 Project Folder Structure (After Enhancement)

```plaintext
CS499Capstone/
├── app.py                     # Launches the Dash application
├── controller.py              # Handles Dash callbacks and routing logic
├── .env                       # MongoDB credentials (secured)
├── requirements.txt           # Dependency list for virtual environment
├── README.md                  # Project documentation
├── .gitignore                 # Excludes venv and .env from Git
│
├── model/
│   ├── __init__.py            # Initializes the model module
│   ├── model.py               # MongoDB access and CRUD logic
│   └── view.py                # Layout and view logic for Dash app
│
├── assets/
│   ├── Dashboard.png
│   ├── DashChartGeo.png
│   ├── Grazioso Salvare Logo.png
│   └── SelectBreed.png
│
├── original_code/             # Backup of the original unenhanced project
└── venv/                      # Virtual environment for isolating dependencies
```

---

## 🧠 Reflection on Software Engineering Skills

This enhancement demonstrates my ability to:

* Apply modular design for scalability and reusability
* Follow secure coding practices
* Refactor academic code into maintainable, professional-grade applications
* Use tools like VS Code and `.env` to build software suitable for real-world deployment
* Implement the MVC pattern by separating layout, callbacks, and data logic into distinct modules
* Introduce efficient filter logic using vectorized operations in pandas
* Add user-friendly features like breed and color filtering
* Create a virtual environment using `venv` to manage dependencies cleanly
* Transition from static data files to secure, real-time database queries using MongoDB Compass
* Handle database errors gracefully and ensure connections are opened and closed properly

---

## 🎓 Course Outcomes Met

* **Outcome 3 (Software Design and Engineering):** Achieved by implementing modularity, using environment variables, and improving code structure and maintainability.
* **Outcome 4 (Algorithms and Data Structures):** Improved filtering logic and added input validation.
* **Outcome 5 (Databases):** Integrated better error handling, used MongoDB Compass, and ensured secure, closed database connections.

I updated my Module One plan after instructor feedback to include Outcome 5 due to the significant enhancements made to database design and handling.

---

## 🔗 Project Links

* 📁 [Original Code on GitHub](https://github.com/GregoriaRamirez/CS-499-Capstone/tree/main/original_code)
* 📁 [Enhanced Code (GitHub Pages)](https://gregoriaramirez.github.io/artifact-software)
* 🖼️ [Screenshot: Animal Shelter Dashboard](/assets/Animal_Shelter_Dashboard.png)

---
