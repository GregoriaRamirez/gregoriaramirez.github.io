````markdown
# Code Review: Enhancing the Animal Shelter Dashboard Project from CS 340 to CS 499

## Artifact Overview

This code review focuses on the Animal Shelter Dashboard project originally developed during CS 340: Client-Server Development.
The project is a web-based application started in Jupyter Notebook and MongoDB shell, that utilizes Python, Dash, and MongoDB
to display and filter animal outcome data. The dashboard featured searchable tables and charts based on animal type, breed, color, and outcome category.

## Purpose of the Review

The purpose of this review is to evaluate the original implementation for technical weaknesses and opportunities for enhancement. The focus areas are:

- Software Design and Engineering
- Algorithms and Data Structures
- Databases

The findings informed a structured enhancement plan implemented during CS 499: Computer Science Capstone.

## Identified Weaknesses

### 1. Software Design and Engineering

- The application was contained in a single monolithic script (`app.py`)
- No modular file organization (e.g., no MVC pattern)
- Sensitive credentials (MongoDB URI) were hardcoded
- No implementation of logging or error tracking
- Dash callbacks were tightly coupled with layout code

### 2. Algorithms and Data Structures

- Filtering logic was duplicated and not reusable
- Hardcoded conditions for specific rescue types
- No input validation or dynamic query handling
- Missed opportunities for vectorized operations with pandas

### 3. Database Handling

- Static CSV file used on every app run instead of querying MongoDB live
- MongoDB connections were not managed securely or efficiently
- No use of `try-except-finally` blocks for error handling
- No separation of CRUD logic into reusable functions

## Example of Original Filtering Code (Before Enhancement)

```python
if filter == 'disaster':
    df = df[df['animal_type'] == 'Dog']
    df = df[df['age_upon_outcome_in_weeks'] > 52]
    df = df[df['sex_upon_outcome'].str.contains('Male')]
    df = df[df['outcome_type'].isin(['Adoption', 'Transfer'])]
````

### Issues

* Logic is hardcoded and repeated across filters
* Not abstracted into a function or reusable structure
* No validation or dynamic input handling

## Enhancement Plan

### Software Design and Engineering

* Separated code into modular components: `app.py`, `controller.py`, `model.py`, `view.py`
* Adopted a basic MVC (Model-View-Controller) structure
* Moved sensitive data to a `.env` file using `python-dotenv`
* Added a `logging` module for error tracking
* Improved readability and separation of layout and logic

### Algorithms and Data Structures

* Refactored filtering logic into centralized, reusable functions
* Introduced input validation for breed and color filters
* Applied vectorized operations in pandas for efficiency
* Reduced data handling complexity in callbacks

### Databases

* Replaced static CSV loads with real-time MongoDB queries
* Structured CRUD operations in a separate model module
* Used MongoDB Compass for secure, visual database interaction
* Ensured proper use of `try-except-finally` for connections

## Outcomes Met Through Review

* **Outcome 3 (Software Design and Engineering):** Implemented modular design and secure coding practices
* **Outcome 4 (Algorithms and Data Structures):** Improved filter logic and implemented input validation
* **Outcome 5 (Databases):** Optimized database interaction and ensured secure handling

## Capstone Walkthrough Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/NTrtEVuawBM" title="Capstone Walkthrough" frameborder="0" allowfullscreen></iframe>
```

---
