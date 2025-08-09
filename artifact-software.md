---
layout: default
title: Software Design Enhancement
permalink: /artifact-software
---
**Navigation:**  
[🏠 Home](index.md) | [📝 Self-Assessment](self-assessment.md) | [🎥 Code Review](code-review.md)| [📂 Projects](projects.md) | [🛠️ Software Design](artifact-software.md) | [🧠 Algorithms](artifact-algorithms.md) | [💾 Databases](artifact-databases.md) |[📂 Projects](projects.md)  | [🏆 Awards](awards.md) | [📄 Résumé](resume.md)

# 🧹 Software Design & Engineering Artifact

## 📌 Artifact Description

For my CS 499 Capstone, I chose to enhance my final project from CS 340: Client-Server Development. Originally created in February 2025, the artifact 
is a web-based dashboard for an animal shelter. The application was first developed in a Jupyter Notebook using Python, Dash, and a MongoDB database 
connected to a CSV data source. It displayed outcome records from the shelter in a table, supported search and filtering, and included simple charts 
for visual analysis.

I selected this artifact because it integrates several skills I have developed throughout the program: database operations, data manipulation with pandas, 
and interactive web development with Dash. The original version functioned, but it lacked structure, performance optimizations,
and security. This made it an ideal candidate for enhancement. 

To improve the software design, I reorganized the code into a more modular format using a Model-View-Controller (MVC) approach. I separated the routing
logic, callback functions, and layout components into their own files. This structure improved readability, scalability, and ease of testing. I also
implemented environment variables using python-dotenv to store sensitive information like the MongoDB connection string, enhancing security and aligning 
with industry best practices.

In addition to reorganizing the architecture, I introduced new filtering features, including color and breed filters, which expanded the application's
usability. These enhancements improved the dashboard’s responsiveness by limiting the data processed client-side and reducing visual clutter. The filtering 
logic was refactored to be more efficient, using conditional logic and vectorized operations in pandas, which improved both performance and maintainability.

## 📷 Final Dashboard Screenshot

<img src="/assets/Animal_Shelter_Dashboard.png" alt="Animal Shelter Dashboard Screenshot" style="max-width: 100%; border: 1px solid #ddd; border-radius: 8px; margin-top: 20px;" />

## 📎 Justification for Inclusion

To improve the software design, I reorganized the code into a more modular format using a Model-View-Controller (MVC) structure. I separated the routing logic, callback functions, and layout components into separate files. This made the codebase easier to read, scale, and test. I also used `python-dotenv` to manage environment variables and securely store sensitive information like the MongoDB connection string—an improvement aligned with industry standards.

Beyond restructuring the architecture, I added new filtering features for animal color and breed. These expanded the dashboard’s usability and helped reduce clutter by narrowing down results. I also refactored the filtering logic using conditional checks and vectorized operations in pandas, which made the app faster and more efficient.

At the start of the enhancement, I focused on two outcomes:

* **Outcome 3 – Software Design and Engineering:** Met by refactoring the codebase into modular components, applying the MVC pattern, and improving security practices.
* **Outcome 4 – Algorithms and Data Structures:** Met by improving filtering logic and implementing efficient data-handling techniques.

As the project progressed, I realized I had also met:

* **Outcome 5 – Databases:** I transitioned from using the Mongo shell to MongoDB Compass, which gave me a more secure and user-friendly way to manage the database. I also added error handling, replaced static CSV imports with live MongoDB queries, and ensured proper connection management in the code.

One challenge I faced was reorganizing the file structure without breaking the app. I had to carefully adjust import paths and retest each callback to confirm it worked. Another challenge was setting up a virtual environment with `venv` to isolate dependencies and avoid version conflicts. That step helped streamline future testing and deployment.

Overall, this project reflects how far I have come in applying real-world development standards, organizing code for long-term maintainability, and building a working product that is secure, efficient, and user-friendly.

## 💡 Code Snippets Demonstrating Enhancements

### 🧹 Snippet 1: Modular Entry Point (`app.py`)

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
This code demonstrates improved software design through the use of modular architecture. The layout is loaded from a separate view file, and callbacks are managed in a separate controller module. This structure follows the Model-View-Controller (MVC) pattern, making the application more organized, maintainable, and scalable. Additionally, it uses the modern `app.run()` method instead of the deprecated `run_server()`, aligning with current Dash best practices.

---

### 🧹 Snippet 2: Callback Logic (`controller.py`)

```python
from dash.dependencies import Input, Output
from dash import html, dcc
import pandas as pd
import plotly.express as px
from model import get_data

df = get_data()

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
This code introduces a modular structure using a `register_callbacks()` function to group all callback logic in one place. By keeping table and chart logic cleanly separated and centralized, this approach supports maintainability and reduces duplicate logic. The design aligns with software engineering principles like separation of concerns and modular reuse, making the application easier to scale and debug.

---

### 🧹 Snippet 3: Secure Map Callback (`controller.py`)

```python
import dash_leaflet as dl

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
This map callback was intentionally separated from the rest of the logic to support clarity, reuse, and single-responsibility principles. It makes the mapping logic easier to manage independently from charts and tables, which aligns with the modular design pattern used throughout the application. This structural decision supports flexible future enhancements, such as location clustering or advanced geospatial features.

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

---

## 🔗 Project Links

* 📁 [Original Code on GitHub](https://github.com/GregoriaRamirez/CS-499-Capstone/tree/main/original_code)
* 📁 [Enhanced Code (GitHub Pages)](https://gregoriaramirez.github.io/artifact-software)
* 🖼️ [Screenshot: Animal Shelter Dashboard](/assets/Animal_Shelter_Dashboard.png)

---

<div style="text-align: center; margin-top: 3em;">
  <a href="index.md" style="
    display: inline-block;
    padding: 10px 20px;
    background-color: #007acc;
    color: white;
    border-radius: 6px;
    text-decoration: none;
    font-weight: bold;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  ">⬅ Back to Home</a>
</div>

