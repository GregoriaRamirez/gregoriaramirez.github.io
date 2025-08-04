# 🧮 Algorithms & Data Structures Artifact

## 💡 Code Snippets Demonstrating Enhancements

### Snippet 1: Efficient Multi-Criteria Filtering in Dashboard Table (controller.py)

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
```

**🔧 Enhancement Summary:**
This function was enhanced to support dynamic, multi-criteria filtering by combining vectorized pandas operations such as `.isin()`, `.str.contains()`, and `.between()`. These techniques replaced slower, more manual filtering approaches, improving runtime and maintainability. The use of `.copy()` prevents `SettingWithCopyWarning`, ensuring safe DataFrame manipulation.

---

### Snippet 2: Chart Update Logic Using Filtered Data (controller.py)

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

**🔧 Enhancement Summary:**
This enhancement separates chart logic from filtering logic, improving modularity. The function dynamically builds visualizations based on the active filter and uses `value_counts()` for fast frequency aggregation. The separation of chart display from the data logic follows clean design principles.

---

### Snippet 3: Map Update Callback Handling User Selection (controller.py)

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

**🔧 Enhancement Summary:**
This update refines the Dash Leaflet map callback to respond to user selections. By extracting coordinates and animal info from the selected row, it renders contextual tooltips and popups. The use of `.get()` ensures graceful fallback defaults, improving fault tolerance.

---

## 📌 Artifact Description

This artifact is part of my Animal Shelter Dashboard project, where I process and filter large datasets from MongoDB using Python and pandas.
It demonstrates how I manipulate data efficiently to create an interactive dashboard that supports filtering by multiple criteria such as breed, color, age, and outcome type.

## 📎 Justification for Inclusion

I selected this artifact because it highlights my ability to implement efficient data filtering algorithms and structured conditional logic.
The use of vectorized pandas operations and modular design improves performance and usability in a real-world application.

## 🔧 Enhancement Overview

Key improvements include:

* Using `.isin()`, `.str.contains()`, and `.between()` for fast, readable, and flexible data filtering
* Applying `.copy()` to avoid pandas `SettingWithCopy` warnings
* Structuring rescue-type filters (`water`, `mount`, `disaster`) with clear conditional logic
* Separating logic for table filtering, chart updating, and map display into modular callbacks

## 🧠 Reflection on Algorithms Skills

This artifact showcases my ability to apply efficient data filtering and transformation techniques using pandas.
By replacing nested loops and manual filtering with vectorized methods, I improved performance and readability.
Additionally, the structured conditional logic for rescue types enhances maintainability and scalability of the dashboard.

## 🎓 Course Outcomes Met

* **Outcome 3:** Designed and evaluated computing solutions using algorithmic principles and sound software practices
* **Outcome 4:** Demonstrated innovative use of data structures and tools like pandas for practical problem-solving

## 🔗 Project Links

* 📁 [Original Code on GitHub](https://github.com/GregoriaRamirez/CS-499-Capstone/blob/main/original/ProjectTwoDashboard%20(1).ipynb)
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

---
