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
from controller import register_callbacks
from view import layout

app = Dash(__name__)
app.layout = layout

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
```

This snippet shows how the main application logic was simplified. By isolating callbacks and layout into other files, 
`app.py` becomes cleaner and easier to manage.

### 🧩 Snippet 2: Callback Logic (`controller.py`)

```python
from dash import Input, Output
from model import query_animals

def register_callbacks(app):
    @app.callback(
        Output('table', 'data'),
        Input('breed-dropdown', 'value'),
        Input('color-dropdown', 'value')
    )
    def update_table(selected_breed, selected_color):
        return query_animals(breed=selected_breed, color=selected_color)
```

Callback logic was moved into `controller.py`. This improves readability, keeps business logic organized, and makes testing easier.

### 🧩 Snippet 3: Secure MongoDB Query (`model.py`)

```python
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client['AAC']

def query_animals(breed=None, color=None):
    query = {}
    if breed:
        query['breed'] = breed
    if color:
        query['color'] = color
    return list(db.animals.find(query))
```

This code replaces hardcoded database credentials with environment variables stored in a `.env` file. All data interaction 
is handled within this model file.

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

## 🎓 Course Outcomes Met

* **Outcome 3 (Software Design and Engineering):** Achieved by implementing modularity, using environment variables, and improving code structure and maintainability.
* **Outcome 4 (Algorithms and Data Structures):** Improved filtering logic and added input validation.
* **Outcome 5 (Databases):** Integrated better error handling, used MongoDB Compass, and ensured secure, closed database connections.

I updated my Module One plan after instructor feedback to include Outcome 5 due to the significant enhancements made to database design and handling.

## 🔗 Project Links

* 📁 [Original Code on GitHub](https://github.com/GregoriaRamirez/CS-499-Capstone/tree/main/original_code)
* 📁 [Enhanced Code (GitHub Pages)](https://gregoriaramirez.github.io/artifact-software)
* 🖼️ [Screenshot: Animal Shelter Dashboard](/assets/Animal_Shelter_Dashboard.png)
