---
layout: default
title: Algorithms & Data Structures Enhancement
permalink: /artifact-algorithms
---

**Navigation:**  
[🏠 Home](index.md) | [📝 Self-Assessment](self-assessment.md) | [🎥 Code Review](code-review.md)| [🛠️ Software Design](artifact-software.md) | [🧠 Algorithms](artifact-algorithms.md) | [💾 Databases](artifact-databases.md) | [📂 Projects](projects.md)  | [🏆 Awards](awards.md) | [📄 Résumé](resume.md)

## 🧠 Algorithms & Data Structures Artifact

### 📌 Artifact Description

For my CS 499 Capstone, I selected the filtering and dashboard update logic from my Animal Shelter Dashboard project. In the original CS 340 version, I handled data filtering with long, repetitive blocks of `if/else` statements inside a single function. This made the code harder to maintain and limited performance when working with large datasets.  

For the enhanced version, I refactored the filtering process using `pandas` DataFrame operations and modularized the update logic. I also added two new dropdown filters for **breed** and **color**. This enhancement improved both readability and efficiency while giving users more control over the dashboard.

---

## 🔁 Before → After (Key Changes)

### 1) Filtering Logic
**Before – ProjectTwoDashboard.ipynb (original):**
```python
if outcome_type == "Adoption":
    df = df[df["outcome_type"] == "Adoption"]
elif outcome_type == "Transfer":
    df = df[df["outcome_type"] == "Transfer"]
elif outcome_type == "Return to Owner":
    df = df[df["outcome_type"] == "Return to Owner"]
else:
    df = df
````

**After – controller.py (enhanced):**

```python
filters = {}
if outcome_type:
    filters["outcome_type"] = outcome_type
if breed:
    filters["breed"] = breed
if color:
    filters["color"] = color

if filters:
    df = df[df[list(filters)].isin(filters.values()).all(axis=1)]
```

➡️ I replaced multiple `if/else` statements with a layered dictionary filter. This allows the dashboard to handle multiple conditions at once (like adoption + breed + color) in a clean, scalable way.
Picture below shows drop down with breed slected and the outcome.

![Color Filtered](/assets/ColorFiltered.png)

### 2) Chart Updates

**Before – ProjectTwoDashboard.ipynb (original):**

```python
fig = px.histogram(df, x="outcome_type")
fig.show()
```

**After – view\.py (enhanced):**

```python
def make_outcome_chart(df):
    if df.empty:
        return go.Figure()
    return px.histogram(df, x="outcome_type", color="sex_upon_outcome",
                        title="Animal Outcomes by Type")
```

➡️ I moved chart creation into its own function. This separates visualization from filtering and makes it reusable across the dashboard.
The chart below shows the pie chart filtered by breed

![Filtered Chart](/assets/FilteredChart.png)


### 3) Map Updates

**Before – ProjectTwoDashboard.ipynb (original):**

```python
px.scatter_mapbox(df, lat="location_lat", lon="location_long")
```

**After – view\.py (enhanced):**

```python
def make_map(df):
    if df.empty:
        return go.Figure()
    return px.scatter_mapbox(
        df, lat="location_lat", lon="location_long",
        color="outcome_type", zoom=10,
        title="Animal Outcomes by Location"
    )
```
---
➡️ I modularized the map logic into a helper function. This keeps the main callback simple and allows better customization of the map display.
The chart below shows the Location on the map

![Map – Breed & Location](/assets/LabBreedLocation.png)

## 🧠 Reflection on Algorithms & Data Structures Skills

This enhancement shows how I refactored repetitive code into layered, efficient filtering logic using `pandas`. By separating charts and maps into their own functions, I made the dashboard easier to read, update, and expand. I also added dropdown filters for **breed** and **color**, giving users more powerful ways to analyze the data.

---

## 🎓 Course Outcomes Met

* **Outcome 3 (Algorithms & Data Structures):** Refactored filtering logic into efficient, layered dictionary operations using pandas.
* **Outcome 4 (Software Development):** Modularized update functions for charts and maps, making the system easier to maintain and extend.

---

## 🔗 Project Links

* 📁 [Original Notebook – ProjectTwoDashboard.ipynb](https://github.com/GregoriaRamirez/gregoriaramirez.github.io/blob/main/original/ProjectTwoDashboard%20%281%29.ipynb)
* 📁 [Enhanced Code – controller.py & view.py](https://github.com/GregoriaRamirez/CS-499-Capstone/tree/main/enhanced)
* 🖼️ [Screenshot: Dashboard with Breed & Color Filters](/assets/DropdownColorselected.png)

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


