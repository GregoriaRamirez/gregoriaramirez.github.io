---
layout: default
title: Databases Enhancement
permalink: /artifact-databases
---

**Navigation:**  
[🏠 Home](index.md) | [📝 Self-Assessment](self-assessment.md) | [🎥 Code Review](code-review.md)| | [🛠️ Software Design](artifact-software.md) | [🧠 Algorithms](artifact-algorithms.md) | [💾 Databases](artifact-databases.md) |[📂 Projects](projects.md)  | [🏆 Awards](awards.md) | [📄 Résumé](resume.md)

# 🗄️ Databases Artifact

## 📌 Artifact Description

For my CS 499 Capstone, I selected the database integration portion of my Animal Shelter Dashboard project, originally developed in February 2025 for CS 340: Client-Server Development. In the original version, I used hardcoded MongoDB credentials and manually accessed data through the Mongo shell. While the application functioned, it lacked secure credential management, proper error handling, and modular database logic.

For the enhanced version, I refactored the MongoDB access into a reusable Python module using `pymongo` and `dotenv`. I securely connected the Dash dashboard to MongoDB using environment variables and implemented structured logging. These enhancements allowed for more professional, secure, and reliable database operations that now support real-time filtering and analytics.

## 📎 Justification for Inclusion

I selected this artifact because it demonstrates my ability to implement secure, efficient, and maintainable database access within a real-world application. Originally, the project used insecure, hardcoded credentials and lacked structure in how it connected to MongoDB. These limitations posed risks to both security and stability.

By enhancing the database layer, I showed that I can manage sensitive data responsibly using environment variables, implement structured error handling to prevent failures, and modularize code for reuse. I also improved the integrity and clarity of the data passed to the dashboard by cleaning unnecessary fields and logging database activity for better traceability.

This artifact demonstrates my ability to:

* Connect securely to a MongoDB database using Python  
* Manage sensitive credentials using environment variables  
* Modularize and reuse database access logic across the project  
* Implement logging and error handling for production readiness  
* Prevent connection leaks by closing MongoDB clients reliably  

## 🔧 Enhancement Overview

Key database improvements include:

* Connecting to MongoDB using `pymongo` with structured exception handling  
* Loading all credentials from a `.env` file using `python-dotenv`  
* Dynamically building the MongoDB URI based on development or production context  
* Wrapping the entire database operation inside a `get_data()` function for reuse  
* Logging successful connections and safely handling errors  
* Closing MongoDB clients with a `finally` block to avoid resource leaks  
* Removing the internal `_id` field to prepare data for presentation in Dash  

## 💡 Code Snippets Demonstrating Enhancements

### 🗄️ Snippet 1: Full Secure Credential Loading and Fallback Defaults (`model.py`)

```python
user = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")
host = os.getenv("MONGO_HOST", "localhost")
port = int(os.getenv("MONGO_PORT", 27017))
db_name = os.getenv("MONGO_DB")
collection_name = os.getenv("MONGO_COL")
````

**Enhancement Summary:**
This enhancement loads MongoDB connection settings from a `.env` file using environment variables, removing all hardcoded credentials. It includes fallback values for host and port to ensure the app remains operational in development environments. This is a professional security practice and makes the application deployment-ready.

---

### 🗄️ Snippet 2: MongoDB Connection Handling with Logging and Fallback (`model.py`)

```python
try:
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]

    mongo_data = list(collection.find())
    df = pd.DataFrame(mongo_data)

    logger.info("MongoDB data successfully retrieved.")
    return df

except Exception as e:
    logger.error(f"Error retrieving data: {e}")
    return pd.DataFrame()

finally:
    if client:
        client.close()
```

**Enhancement Summary:**
This complete `try-except`-`finally` block adds robust MongoDB error handling. It ensures that even if the connection fails, the application does not crash and returns a safe fallback, an empty DataFrame. Structured logging provides insight into issues, and the connection is always closed properly, preventing leaks and locking issues.

---

### 🗄️ Snippet 3: Secure Imports and dotenv Initialization (`model.py`)

```python
from dotenv import load_dotenv
from pymongo import MongoClient

# Load credentials from .env
load_dotenv()
```

**Enhancement Summary:**
This snippet imports the necessary libraries for connecting to MongoDB securely and initializes environment variable loading with `load_dotenv()`. It ensures that sensitive credentials like usernames and passwords are accessed only through a protected environment, following secure development best practices and separating secrets from source code.

---

### 🗄️ Snippet 4: Remove Internal MongoDB `_id` Field Before Display (`model.py`)

```python
if '_id' in df.columns:
    df.drop(columns=['_id'], inplace=True)
```

**Enhancement Summary:**
This enhancement removes the MongoDB internal `_id` field from the dataset before passing it to the dashboard. Dropping this field prevents it from cluttering the user interface and ensures that only relevant columns are displayed and visualized, improving user readability and data presentation.

---

## 🧠 Reflection on Database Skills

This artifact showcases my ability to build secure, maintainable database integration for a web application. I transitioned from insecure, hardcoded Mongo shell queries to a structured, production-ready MongoDB connection using Python. I added logging, exception handling, and modular design patterns that reflect real-world backend development skills. These enhancements made the system more reliable, scalable, and aligned with modern best practices.

## 🎓 Course Outcomes Met

* **Outcome 4 (Computing Tools and Practices):** Applied tools like `pymongo`, `dotenv`, and `pandas` to transform and serve real-time data from a database into an interactive dashboard. This was achieved by using pymongo to securely query MongoDB, processing and cleaning the results with pandas, and integrating the data into the Dash dashboard for live filtering and visualization.
  
* **Outcome 5 (Databases):** Developed a security mindset by implementing secure credential storage, exception handling, and proper connection cleanup for MongoDB using `Python`. This was achieved by replacing insecure, hardcoded credentials with environment variables loaded through `python-dotenv`, adding structured error handling, and ensuring the database client closes after each operation.
  

---

## 🔗 Project Links

* 📁 [Original Code – animal\_shelter.py](https://github.com/GregoriaRamirez/gregoriaramirez.github.io/blob/main/original/animal_shelter.py)
* 📁 [Original Code – ProjectTwoDashboard.ipynb](https://github.com/GregoriaRamirez/gregoriaramirez.github.io/blob/main/original/ProjectTwoDashboard%20%281%29.ipynb)
* 📁 [Enhanced Code on GitHub](https://github.com/GregoriaRamirez/CS-499-Capstone/tree/main/enhanced)
* 🖼️ [Screenshot: Animal Shelter Dashboard](/assets/Animal_Shelter_Dashboard.png)

---


---
layout: default
title: Algorithms Enhancement
permalink: /artifact-algorithms
---

**Navigation:**  
[🏠 Home](index.md) | [📝 Self-Assessment](self-assessment.md) | [🎥 Code Review](code-review.md)| | [🛠️ Software Design](artifact-software.md) | [🧠 Algorithms](artifact-algorithms.md) | [💾 Databases](artifact-databases.md) |[📂 Projects](projects.md)  | [🏆 Awards](awards.md) | [📄 Résumé](resume.md)
# 🧮 Algorithms & Data Structures Artifact

## 📌 Artifact Description

For this category, I selected my Animal Shelter Dashboard project, originally built for CS 340: Client-Server Development in February 2025. This project is a web-based dashboard built in Python using the Dash framework and connected to a MongoDB database. The dashboard allows users to explore shelter outcome data using dropdown and radio button filters, and it visualizes the results in a searchable table and interactive charts.

## 📎 Justification for Inclusion

I included this artifact in my ePortfolio because it demonstrates how I applied structured logic and efficient control flow to solve real-world filtering and visualization problems. In the original version, the `update_dashboard()` function used repetitive `if` blocks and direct filtering, which made it harder to manage.

In the enhanced version, I reorganized this function to apply layered filters that trigger only when conditions are met. I also used pandas’ vectorized operations to make filtering more efficient and added input validation to prevent the dashboard from breaking when dropdowns were empty or when filter combinations returned no records.

---
## 💡 Code Snippets Demonstrating Enhancements

## 🔄 Before and After Enhancement

**Original Code (Before Enhancement):**

```python
# Filtering data directly on original DataFrame multiple times
if filter_type == 'water':
    filtered_df = df[(df['breed'].str.contains('Labrador Retriever')) & 
                     (df['outcome_type'] == 'Euthanasia')]
````

This approach:

1. Repeatedly filters the full DataFrame
2. Overwrites previous results, making it harder to track
3. Does not handle missing or empty filter inputs properly

**Enhanced Code (After Enhancement):**
### 🧮 Snippet 1: Dashboard Table Filtering (`controller.py`)
```python
def update_dashboard(filter_type, selected_colors, selected_breeds):
    filtered_df = df.copy()
    if filter_type == 'water':
        filtered_df = filtered_df[
            (filtered_df['breed'].str.contains('Labrador Retriever', na=False)) &
            (filtered_df['outcome_type'] == 'Euthanasia') &
            (filtered_df['animal_type'] == 'Dog')
        ]
    elif filter_type == 'mount':
        filtered_df = filtered_df[
            (filtered_df['outcome_type'] == 'Transfer') &
            (filtered_df['animal_type'] == 'Cat') &
            (filtered_df['sex_upon_outcome'].str.contains('Female', na=False)) &
            (filtered_df['age_upon_outcome_in_weeks'].between(52, 260))
        ]

    if selected_colors:
        filtered_df = filtered_df[filtered_df['color'].isin(selected_colors)]
    if selected_breeds:
        filtered_df = filtered_df[filtered_df['breed'].isin(selected_breeds)]

    return filtered_df.to_dict('records')
```

---

## 🔧 Key Enhancements

1. Added layered (chained) filtering logic that applies only when needed.
2. Used `.copy()` to preserve the original dataset.
3. Applied safe filtering using `.str.contains(..., na=False)` and `.isin()`.
4. Allowed filters to work in combination without overwriting each other.
5. Returned a predictable output using `.to_dict('records')`.

These changes improved runtime efficiency, performance, and stability. For example, filtering a 3,000-row DataFrame down to just 150–300 relevant records per interaction significantly improved responsiveness during rapid user input. The dashboard now responds smoothly to user interactions and avoids crashing due to empty fields or unmatched data.

---
![Dropdown Color Selected](/assets/DropdownColorselected.png)

This screenshot applies to both Snippet 1 and Snippet 2. It shows how the table updates when a color filter is applied (Snippet 1) and how the chart updates based on that filtered data (Snippet 2).

---

### 🧮 Snippet 2: Chart Update Logic (`view.py`)

```python
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
```

This chart function was improved to show the correct graph based on the selected filter type. It now checks if the filtered data is empty and uses appropriate chart types (bar or pie) to match the context.

---

### 🧮 Snippet 3: Map Rendering with Fallbacks (`view`)

```python
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

This map code was enhanced with fallback values so the map still renders even if data is missing or no selection is made. It prevents crashes by defaulting to valid coordinates and checking for blank inputs.

---

## 🧠 Algorithms Impact

These updates improved the performance, flexibility, and stability of the application. The dashboard now handles empty filters, rare combinations like uncommon breeds or rescue types, and even missing or blank values all without crashing. The filters work together as intended, rather than overwriting or interfering with each other.

I used step-by-step filtering that only runs when needed, which made the logic easier to follow and reduced unnecessary processing. I applied pandas methods like  `.isin()` and  `.str.contains()` carefully, along with  `.copy()` to protect the original data. These decisions gave users more control and improved the overall reliability of the dashboard.

This enhancement supports Program Outcome 3 by showing how I used clear, structured logic to solve real problems while balancing performance and maintainability.

---

## 📈 Reflection

This enhancement helped me grow as a developer because I had to carefully consider how different filters interact and how to prevent them from breaking the dashboard. At first, I had difficulty getting multiple filters to work together correctly. I tested various combinations and adjusted the order in which filters were applied to make sure the results remained accurate and stable.

One of the most important lessons I learned was the need to plan for unexpected user input. Some users might leave dropdowns blank or choose rare combinations, and I had to ensure the application could handle those cases without crashing. By using na=False and safe filtering techniques, I was able to prevent errors and create a more dependable user experience.

This process improved my confidence in designing logic that is both clear and reliable. It strengthened my ability to use control flow, data structures, and pandas to manage more complex application logic in a way that remains clean, testable, and easy to maintain.

---

## 🔍 Demonstrated Skills

* Designed multi-criteria filtering algorithms
* Used pandas to manipulate structured data efficiently
* Modularized logic for clarity and reuse
* Optimized performance by using vectorized operations

---

## 🔧 Enhancement Overview

Key algorithmic improvements include:

* Replacing repetitive filtering with efficient logic using `.isin()`, `.str.contains()`, and `.between()`
* Using `.copy()` to prevent `SettingWithCopyWarning`
* Separating logic for table filtering, chart rendering, and map updates
* Organizing conditionals for multiple rescue types (`water`, `mount`, `disaster`)
* Supporting real-time updates across all dashboard components

---

## 🎓 Course Outcomes Met

* **Outcome 3 – Algorithms & Data Structures**: Applied structured filtering, condition logic, and efficient algorithms to improve application logic.
* **Outcome 4 – Tools & Practices**: Used Dash, pandas, and clean modular design to enhance interactivity and maintainability.

---

## 🔗 Project Links

* 📁 [Original Code – animal\_shelter.py](https://github.com/GregoriaRamirez/gregoriaramirez.github.io/blob/main/original/animal_shelter.py)
* 📁 [Original Notebook – ProjectTwoDashboard.ipynb](https://github.com/GregoriaRamirez/gregoriaramirez.github.io/blob/main/original/ProjectTwoDashboard%20%281%29.ipynb)
* 📁 [Enhanced Code on GitHub](https://github.com/GregoriaRamirez/CS-499-Capstone/tree/main/enhanced)
* 🖼️ [Screenshot – Animal Shelter Dashboard](/assets/Animal_Shelter_Dashboard.png)
* 🖼️ [Screenshot – Dropdown Color Selected](/assets/DropdownColorselected.png)

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



