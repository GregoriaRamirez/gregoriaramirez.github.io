---
layout: default
title: Software Design Enhancement
permalink: /artifact-software
---

# 🧮 Algorithms & Data Structures Artifact

## 📌 Artifact Description

For my CS 499 Capstone, I selected my Animal Shelter Dashboard project, originally developed in February 2025 for CS 340: Client-Server Development. This application connects to a MongoDB database and uses Dash to render an interactive interface that allows users to filter and visualize animal outcome data. The original version lacked efficient filtering and used basic conditional logic that limited the dashboard’s responsiveness and flexibility.

In this enhanced version, I focused on improving the data handling logic by using vectorized pandas operations for filtering, transforming, and displaying the data. The updates ensure that the dashboard efficiently processes multi-criteria inputs, responds quickly to user interactions, and displays accurate visualizations. These improvements directly support the application's core functionality by enabling real-time, meaningful insights from large datasets.

## 📎 Justification for Inclusion

I selected this artifact because it demonstrates my ability to work with real-world datasets using effective algorithms and data structures. The enhancements I implemented go beyond basic filtering by introducing logical structures that handle multiple user inputs in a scalable way. I optimized the data transformation process using pandas methods like `.isin()`, `.str.contains()`, and `.between()`, which allow for fast and readable operations on large datasets.

This artifact showcases my ability to:

* Design and apply multi-criteria filtering algorithms
* Use pandas to manipulate structured data efficiently
* Separate logic into modular functions for reuse and clarity
* Optimize performance by avoiding loops and using vectorized operations

## 🔧 Enhancement Overview

Key algorithmic improvements include:

* Replacing manual and repetitive filters with flexible logic using `.isin()` and `.str.contains()`
* Filtering by age using `.between()` for clearer range conditions
* Using `.copy()` to avoid `SettingWithCopyWarning` errors in pandas
* Separating logic for table filtering, chart rendering, and map updates
* Organizing conditional logic for rescue types (`water`, `mount`, `disaster`) to allow complex combinations of breed, age, outcome, and sex
* Improving user experience by supporting live updates across all visual components

## 💡 Code Snippets Demonstrating Enhancements

### 🧮 Snippet 1: Efficient Multi-Criteria Filtering in Dashboard Table (`controller.py`)

```python
def update_dashboard(filter_type, selected_colors, selected_breeds):
    filtered_df = df.copy()

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

    if selected_colors:
        filtered_df = filtered_df[filtered_df['color'].isin(selected_colors)]
    if selected_breeds:
        filtered_df = filtered_df[filtered_df['breed'].isin(selected_breeds)]

    return filtered_df.to_dict('records')
````

**Enhancement Summary:**
This function was enhanced to support dynamic, multi-criteria filtering by combining vectorized pandas operations such as `.isin()`, `.str.contains()`, and `.between()`. These techniques replaced slower, more manual filtering approaches, improving runtime and maintainability. The use of `.copy()` prevents `SettingWithCopyWarning`, ensuring safe DataFrame manipulation.

---

### 🧮 Snippet 2: Chart Update Logic Using Filtered Data (`controller.py`)

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

**Enhancement Summary:**
This enhancement separates chart logic from filtering logic, improving modularity. The function dynamically builds visualizations based on the active filter and uses `value_counts()` for fast frequency aggregation. The separation of chart display from the data logic follows clean design principles.

---

### 🧮 Snippet 3: Map Update Callback Handling User Selection (`controller.py`)

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

**Enhancement Summary:**
This update refines the Dash Leaflet map callback to respond to user selections. By extracting coordinates and animal info from the selected row, it renders contextual tooltips and popups. The use of `.get()` ensures graceful fallback defaults, improving fault tolerance.

---

## 🧠 Reflection on Algorithms Skills

This artifact highlights my ability to work with structured data efficiently using pandas and Python. I applied best practices for filtering large datasets using optimized methods, improved data transformation logic, and reduced potential bugs from chained indexing. By building modular functions to support multi-criteria filters and separate data logic from UI updates, I demonstrated clean coding principles and scalable algorithm design. These enhancements helped the application remain responsive and intuitive even with complex data combinations.

## 🎓 Course Outcomes Met

* **Outcome 3 (Algorithms and Data Structures):** Designed and evaluated computing solutions using algorithmic principles and computer science practices. Demonstrated this by optimizing filter logic and restructuring callback functions.
* **Outcome 4 (Computing Tools and Practices):** Used data transformation tools like pandas and Dash to develop interactive components based on efficient logic and data handling practices.

---

## 🔗 Project Links

* 📁 [Original Code on GitHub](https://github.com/GregoriaRamirez/CS-499-Capstone/tree/main/original_code)
* 📁 [Enhanced Code (GitHub Pages)](https://gregoriaramirez.github.io/artifact-algorithms)
* 🖼️ [Screenshot: Animal Shelter Dashboard](/assets/Animal_Shelter_Dashboard.png)

---

<div style="text-align: center; margin-top: 3em;">
  <a href="/" style="
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
```
