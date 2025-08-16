---
layout: default
title: Software Design Enhancement
permalink: /artifact-software
---

**Navigation:**  
[🏠 Home](index.md) | [📝 Self-Assessment](self-assessment.md) | [🎥 Code Review](code-review.md) | [🛠️ Software Design](artifact-software.md) | [🧠 Algorithms](artifact-algorithms.md) | [💾 Databases](artifact-databases.md) | [📂 Projects](projects.md) | [🏆 Awards](awards.md) | [📄 Résumé](resume.md)

## 🧹 Software Design & Engineering Artifact

### 📌 Artifact Description

For my CS 499 Capstone, I chose to enhance my final project from CS 340: Client-Server Development. Originally created in February 2025, the artifact is a web-based dashboard for an animal shelter. The application was first developed in a Jupyter Notebook using Python, Dash, and a MongoDB database connected to a CSV data source. It displayed outcome records from the shelter in a table, supported search and filtering, and included simple charts for visual analysis.

I selected this artifact because it integrates several skills I have developed throughout the program: database operations, data manipulation with pandas, and interactive web development with Dash. The original version functioned, but it lacked structure, performance optimizations, and security. This made it an ideal candidate for enhancement. 

To improve the software design, I reorganized the code into a more modular format using a Model-View-Controller (MVC) approach. I separated the routing logic, callback functions, and layout components into their own files. This structure improved readability, scalability, and ease of testing. I also implemented environment variables using python-dotenv to store sensitive information like the MongoDB connection string, enhancing security and aligning with industry best practices.

In addition to reorganizing the architecture, I introduced new filtering features, including color and breed filters, which expanded the application's usability. These enhancements improved the dashboard’s responsiveness by limiting the data processed client-side and reducing visual clutter. The filtering logic was refactored to be more efficient, using conditional logic and vectorized operations in pandas, which improved both performance and maintainability.

### 📷 Final Dashboard Screenshot

<img src="/assets/Animal_Shelter_Dashboard.png" alt="Animal Shelter Dashboard Screenshot" style="max-width: 100%; border: 1px solid #ddd; border-radius: 8px; margin-top: 20px;" />

---

### 🔁 Before → After (Key Changes)

#### 1) App Startup  
**Before – `animal_shelter.py` (original):**
```python
app = Dash(__name__)
# layout, callbacks, and database all here...
app.run_server(debug=True)
````

**After – `app.py` (enhanced):**

```python
app = Dash(__name__)
app.layout = layout
register_callbacks(app)
app.run(debug=True, port=8550)
```

➡️ I moved the layout and callbacks into their own files and switched to `app.run()`. This makes the code shorter, easier to read, and ready to expand later.&#x20;

---

#### 2) Layout

**Before – `animal_shelter.py` (original):**

```python
app.layout = html.Div([
    html.H1("Animal Shelter Dashboard"),
    dash_table.DataTable(...),
    dcc.Graph(...)
])
```

**After – `view.py` (enhanced):**

```python
layout = html.Div([
    html.H1('SNHU CS-340 Gregoria Ramirez'),
    dcc.RadioItems(id='filter-type', options=[...]),
    dcc.Dropdown(id='color-filter', options=[...]),
    dcc.Dropdown(id='breed-filter', options=[...]),
    dash_table.DataTable(id='datatable-id', ...),
    html.Div(id='chart-id'),
    html.Div(id='map-id')
])
```

➡️ The layout is now in its own file. The dropdowns are built from real data instead of being hardcoded, which keeps the app current without me having to edit options manually.&#x20;

---

#### 3) Callbacks

**Before – `animal_shelter.py` (original):**

```python
@app.callback(Output('datatable-id','data'),
              [Input('filter-type','value')])
def update_dashboard(filter_type): ...
```

**After – `controller.py` (enhanced):**

```python
def register_callbacks(app):
    @app.callback(Output('datatable-id','data'),
                  [Input('filter-type','value'),
                   Input('color-filter','value'),
                   Input('breed-filter','value')])
    def update_dashboard(...): ...
```

➡️ All callbacks are grouped together in one controller file. This makes the logic easier to manage and test.&#x20;

---
#### 4) Project Structure (Monolith → Modular)

**Before – single file (original):**

```
animal_shelter.py
```

**After – modular folders (enhanced):**

```
CS499Capstone/
├── app.py
├── controller.py
├── model/
│   ├── __init__.py
│   ├── model.py
│   └── view.py
├── assets/
│   └── ...
└── venv/
```
➡️ Splitting the code into clear modules (app, controller, model, view) follows the MVC pattern, improves readability, and makes testing and future changes easier.

---

### 📎 Justification for Inclusion

This enhancement shows how I improved the structure and security of my code. I modularized the project into separate files and separated layout and callbacks to follow MVC principles. These changes make the app more professional, secure, and maintainable.

One challenge I faced was reorganizing the file structure without breaking imports. I had to carefully adjust paths and test each piece until everything connected properly. I also set up a virtual environment with `venv` to keep dependencies isolated, which made testing and deployment smoother.

---

### 🧠 Reflection on Software Engineering Skills

This enhancement demonstrates my ability to:

* Apply modular design for scalability and reusability
* Follow secure coding practices
* Refactor academic code into maintainable, professional-grade applications
* Use tools like VS Code and `.env` to prepare for real-world deployment
* Separate layout, callbacks, and data logic into distinct modules
* Add new user features (color and breed filters)
* Manage dependencies with a virtual environment

---

### 🎓 Course Outcomes Met

* **Outcome 3 (Software Design and Engineering):** Achieved by implementing modularity, using environment variables, and improving structure.

---

### 🔗 Project Links

* 📁 [Original Code on GitHub](https://github.com/GregoriaRamirez/CS-499-Capstone/tree/main/original_code)
* 📁 [Enhanced Code on GitHub](https://github.com/GregoriaRamirez/CS-499-Capstone/tree/main/enhanced)
* 🖼️ [Screenshot: Animal Shelter Dashboard](/assets/Animal_Shelter_Dashboard.png)

---

<div style="text-align: center; margin-top: 3em;">
  <a href="https://gregoriaramirez.github.io/index" style="
    display: inline-block;
    padding: 10px 20px;
    background-color: #007acc;
    color: white;
    border-radius: 6px;
    text-decoration: none;
    font-weight: bold;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  ">Back to Home</a>
</div>
