---
layout: default
title: Algorithms Enhancement
permalink: /artifact-algorithms
---
**Navigation:**  
[🏠 Home](index.md) | [📝 Self-Assessment](self-assessment.md) | [🙋‍♀️ About Me](about.md) | [📂 Projects](projects.md) | [🛠️ Software Design](artifact-software.md) | [🧠 Algorithms](artifact-algorithms.md) | [💾 Databases](artifact-databases.md) | [🏆 Awards](awards.md) | [📄 Résumé](resume.md)


# 🧮 Algorithms & Data Structures Artifact

## 📌 Artifact Description

For this category, I selected my Animal Shelter Dashboard project originally built for CS 340: Client-Server Development in February 2025. This project 
is a web-based dashboard built in Python using the Dash framework and connected to a MongoDB database. The dashboard allows users to explore shelter outcome
data using dropdown and radio button filters and visualizes the results in a searchable table and interactive charts.

## 📎 Justification for Inclusion

I included this artifact in my ePortfolio because it demonstrates how I applied structured logic and efficient control flow to solve real-world filtering and visualization problems. In the original version, the update\_dashboard() function used repetitive if blocks and direct filtering that made it harder to manage. 
In the enhanced version, I reorganized this function to apply layered filters that only trigger when conditions are met. I also used pandas’ vectorized operations to make filtering more efficient and added input validation so the dashboard would not break when dropdowns were empty or when combinations did not match any records.

## Examples Before and After Enhancements:
Original Code (Before Enhancement):

```python
# Filtering data directly on original DataFrame multiple times
if filter_type == 'water':
    filtered_df = df[(df['breed'].str.contains('Labrador Retriever')) & 
                     (df['outcome_type'] == 'Euthanasia')]
```

This approach:

1. Repeatedly filters the full DataFrame
2. Overwrites previous filter results without preserving the original data
3. Does not handle empty or missing filter inputs properly

## Enhanced Code (After Enhancement):

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

    # Additional filters that apply safely and independently
    if selected_colors:
        filtered_df = filtered_df[filtered_df['color'].isin(selected_colors)]
    if selected_breeds:
        filtered_df = filtered_df[filtered_df['breed'].isin(selected_breeds)]

    # Return a clean, predictable structure for use in the dashboard
    return filtered_df.to_dict('records')
```

## Key Enhancements:

1. Added layered (chained) filter conditions that apply sequentially and only when relevant, improving clarity and control flow.
2. Used df.copy() to create a separate working dataset, preserving the original data and preventing unintended side effects.
3. Implemented safer filtering methods such as .str.contains(..., na=False) and .isin() to avoid runtime errors caused by missing or null data.
4. Handled multiple filter combinations properly so that filters work together instead of conflicting or overwriting each other.
5. Returned a clean, consistent data structure with .to\_dict('records') that the dashboard can reliably use.

These changes improved both performance and user experience. The dashboard now reacts more smoothly to filter changes and is more resilient to unusual inputs 
or empty selections.

Although I focused on improving the filtering logic and performance, I also added input checks to prevent the dashboard from crashing when users leave filters empty, select options with no matching data, such as a rare breed or rescue type or when the data has missing/blank values. This helps avoid errors that could make the app unstable or stop it from working. By safely handling missing or empty data, I made the app more reliable and less likely to fail in ways that could cause problems. While this is not the same as security features like login or encryption, it does help keep the app running smoothly and prevents issues that could cause it to break.

This enhancement aligns with Program Outcome 3: Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while managing the trade-offs involved in design choices. By using layered filtering logic and efficient data-handling methods, I improved both performance and stability while managing complexity in how filters interact.

Enhancing this artifact helped me better understand the importance of organizing logic for readability and performance. One challenge I faced was making sure multiple filters could work together without interfering with one another’s results. I had to test various combinations and inputs to ensure the application responded as expected in all cases. I also was careful with handling missing values or null fields, which required using na=False to prevent errors when filtering string fields. This process improved my confidence in using control flow and data structures to solve real problems. It also taught me how clear, well-planned logic can lead to more stable and professional applications.


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

* 📁 [Original Code – animal\_shelter.py](https://github.com/GregoriaRamirez/gregoriaramirez.github.io/blob/main/original/animal_shelter.py)
* 📁 [Original Code – ProjectTwoDashboard.ipynb](https://github.com/GregoriaRamirez/gregoriaramirez.github.io/blob/main/original/ProjectTwoDashboard%20%281%29.ipynb)
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
