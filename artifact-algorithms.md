---
layout: default
title: Algorithms Enhancement
permalink: /artifact-algorithms
---

**Navigation:**  
[🏠 Home](index.md) | [📝 Self-Assessment](self-assessment.md) | [🙋‍♀️ About Me](about.md) | [📂 Projects](projects.md) | [🛠️ Software Design](artifact-software.md) | [🧠 Algorithms](artifact-algorithms.md) | [💾 Databases](artifact-databases.md) | [🏆 Awards](awards.md) | [📄 Résumé](resume.md)

# 🧮 Algorithms & Data Structures Artifact

## 📌 Artifact Description

For this category, I selected my Animal Shelter Dashboard project, originally built for CS 340: Client-Server Development in February 2025. This project is a web-based dashboard built in Python using the Dash framework and connected to a MongoDB database. The dashboard allows users to explore shelter outcome data using dropdown and radio button filters, and it visualizes the results in a searchable table and interactive charts.

## 📎 Justification for Inclusion

I included this artifact in my ePortfolio because it demonstrates how I applied structured logic and efficient control flow to solve real-world filtering and visualization problems. In the original version, the `update_dashboard()` function used repetitive `if` blocks and direct filtering, which made it harder to manage.

In the enhanced version, I reorganized this function to apply layered filters that trigger only when conditions are met. I also used pandas’ vectorized operations to make filtering more efficient and added input validation to prevent the dashboard from breaking when dropdowns were empty or when filter combinations returned no records.

---

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

These changes improved both performance and stability. The dashboard now responds smoothly to user interactions and avoids crashing due to empty fields or unmatched data.

---

## 🧠 Algorithms Impact

While improving filtering logic and performance, I also focused on error handling. I added checks for empty dropdowns and rare selections to prevent the app from crashing. This strengthened the reliability of the application. Although not a security feature, input validation makes the application more stable and professional.

This enhancement aligns with **Program Outcome 3**: *Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while managing the trade-offs involved in design choices.*

---

## 📈 Reflection

Enhancing this artifact helped me understand how to organize logic for both readability and performance. A key challenge was ensuring that multiple filters worked together without breaking the application. I tested several combinations and implemented fallback handling for missing or null values using `na=False`.

This experience improved my confidence in using control flow, data structures, and pandas to manage complex application logic in a maintainable way.

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

## 💡 Code Snippets

### 🧮 Snippet 1: Dashboard Table Filtering

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

---

### 🧮 Snippet 2: Chart Update Logic

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

---

### 🧮 Snippet 3: Map Rendering with Fallbacks

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

---

## 🎓 Course Outcomes Met

* **Outcome 3 – Algorithms & Data Structures**: Applied structured filtering, condition logic, and efficient algorithms to improve application logic.
* **Outcome 4 – Tools & Practices**: Used Dash, pandas, and clean modular design to enhance interactivity and maintainability.

---

## 🔗 Project Links

* 📁 [Original Code – animal\_shelter.py](https://github.com/GregoriaRamirez/gregoriaramirez.github.io/blob/main/original/animal_shelter.py)
* 📁 [Original Notebook – ProjectTwoDashboard.ipynb](https://github.com/GregoriaRamirez/gregoriaramirez.github.io/blob/main/original/ProjectTwoDashboard%20%281%29.ipynb)
* 📁 [Enhanced Artifact – GitHub Pages](https://gregoriaramirez.github.io/artifact-algorithms)
* 🖼️ [Screenshot – Animal Shelter Dashboard](/assets/Animal_Shelter_Dashboard.png)

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
