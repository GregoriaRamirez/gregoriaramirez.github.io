## 💡 Code Snippets Supporting Software Design Enhancements
 
# 🛠️ Enhancement: Software Design and Engineering

## 🐾 Project: Animal Shelter Dashboard  
**Original Course:** CS 340 – Client-Server Development  
**Enhancement Completed In:** CS 499 – Computer Science Capstone

---

For my CS 499 Capstone, I chose to enhance my final project from CS 340: Client-Server Development. Originally created in February 2025, the artifact is a web-based dashboard for an animal shelter. The application was first developed in a Jupyter Notebook using Python, Dash, and a MongoDB database connected to a CSV data source. It displayed outcome records from the shelter in a table, supported search and filtering, and included simple charts for visual analysis.

I selected this artifact because it integrates several skills I’ve developed throughout the program: database operations, data manipulation with pandas, and interactive web development with Dash. The original version functioned, but it lacked structure, performance optimizations, and security. This made it an ideal candidate for enhancement.

To improve the software design, I reorganized the code into a more modular format using a Model-View-Controller (MVC) approach. I separated the routing logic, callback functions, and layout components into their own files. This structure improved readability, scalability, and ease of testing. I also implemented environment variables using `python-dotenv` to store sensitive information like the MongoDB connection string, enhancing security and aligning with industry best practices.

In addition to reorganizing the architecture, I introduced new filtering features, including color and breed filters, which expanded the application's usability. These enhancements improved the dashboard’s responsiveness by limiting the data processed client-side and reducing visual clutter. The filtering logic was refactored to be more efficient, using conditional logic and vectorized operations in pandas, which improved both performance and maintainability.

---

## 📈 Outcomes and Challenges

I initially focused on two outcomes:

- **Outcome 3 – Software Design and Engineering:** Met by refactoring the code into modular components, applying the MVC structure, and improving security with environment variables.  
- **Outcome 4 – Algorithms and Data Structures:** Met by enhancing the logic behind filtering features and applying structured control flows to manage data interactions.

Midway through the course, I realized I had also met:

- **Outcome 5 – Databases:** I transitioned from Mongo shell to MongoDB Compass for easier and more secure management. I improved the database handling in the code by incorporating error checking and ensuring that connections were cleanly established and closed. I also eliminated the dependency on static CSV imports and used live queries from MongoDB to drive the dashboard in real time.

One challenge I faced was refactoring the file structure. I had to carefully update import paths and test each callback function to ensure it still functioned after being separated into modules. Another challenge was setting up a virtual environment. I used `venv` to isolate dependencies and avoid version conflicts, which helped streamline the setup process for future testing and deployment.

In the end, this project reflects my growth in applying real-world development standards, organizing code for long-term maintainability, and delivering a working product that is secure, efficient, and user-friendly.

---

## 🧠 Reflection on Software Engineering Skills

This enhancement demonstrates my ability to:
- Apply modular design for scalability and reusability  
- Follow secure coding practices  
- Refactor academic code into maintainable, professional-grade applications  
- Use tools like VS Code and `.env` to build software suitable for real-world deployment  
- Implement the MVC pattern by separating layout, callbacks, and data logic into distinct modules  
- Introduce efficient filter logic using vectorized operations in pandas  
- Add user-friendly features like breed and color filtering  
- Create a virtual environment using `venv` to manage dependencies cleanly  
- Transition from static data files to secure, real-time database queries using MongoDB Compass  
- Handle database errors gracefully and ensure connections are opened and closed properly


---

````markdown
## 💡 Code Snippets Demonstrating Enhancements

### 🧩 Snippet 1: Modular Entry Point (`app.py`)

To follow software engineering best practices, I reorganized the application launch code so it only handles layout and startup. All logic and callbacks were moved to their own modules for better maintainability.

```python
from dash import Dash
from controller import register_callbacks
from view import layout

app = Dash(__name__)
app.layout = layout

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
````

This keeps `app.py` simple and clear — it initializes the app, sets the layout, and hands off all logic and callbacks to other files. That is part of implementing an MVC-style structure.

---

### 🧩 Snippet 2: Callback Logic (`controller.py`)

Instead of putting callback functions in the main file, I moved them to a controller module. This makes the logic reusable and easier to test or update.

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

This design separates app interactivity into its own space. It also lets me reuse `query_animals()` from the model without repeating code.

---

### 🧩 Snippet 3: Secure MongoDB Query (`model.py`)

To improve security and follow real-world development practices, I removed hardcoded credentials and used `.env` variables. All database logic is now in `model.py`, separate from the interface code.

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

This code securely connects to the database using `python-dotenv`. It also keeps query logic in one place, which makes it easier to maintain and debug.

---

```
---

## 📁 Project Folder Structure (After Enhancement)

```plaintext
CS499Capstone/
│
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
│
└── venv/                      # Virtual environment for isolating dependencies
````

---

## 🔗 Project Links

* 📁 [Original Code on GitHub](https://github.com/GregoriaRamirez/CS-499-Capstone/tree/main/original_code)
* 📦 [Download Full Enhanced Code (ZIP)](/assets/CS499Capstone.zip)
* 🖼️ [Screenshot: Animal Shelter Dashboard](/assets/Animal_Shelter_Dashboard.png)

```


