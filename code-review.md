---
layout: default
title: Code Review Walkthrough
permalink: /code-review
---
**Navigation:**  
[🏠 Home](index.md) | [📝 Self-Assessment](self-assessment.md) | [🎥 Code Review](code-review.md) | [🛠️ Software Design](artifact-software.md) | [🧠 Algorithms](artifact-algorithms.md) | [💾 Databases](artifact-databases.md) |[📂 Projects](projects.md)  | [🏆 Awards](awards.md) | [📄 Résumé](resume.md)


# Code Review: Enhancing the Animal Shelter Dashboard Project from CS 340 to CS 499
## 🎥 Code Review – CS 499 Capstone

<p>
  This video walks through the original project and explains the enhancements I made in design, logic, and data handling. It includes commentary on software design, database operations, and algorithm updates.
</p>

<iframe width="560" height="315" src="https://www.youtube.com/embed/DXgBW47WSRQ" title="Capstone Code Review Walkthrough" frameborder="0" allowfullscreen></iframe>


## Artifact Overview

This code review focuses on the Animal Shelter Dashboard project originally developed during CS 340: Client-Server Development. The project is a web-based application that began in Jupyter Notebook with MongoDB shell integration, and utilizes Python, Dash, and MongoDB to display and filter animal outcome data. The dashboard featured searchable tables and charts based on animal type, breed, color, and outcome category, demonstrating my ability to design interactive, data-driven applications.

## Purpose of the Review

The purpose of this review is to evaluate the original implementation for technical weaknesses and opportunities for enhancement.
The focus areas are:

- Software Design and Engineering
- Algorithms and Data Structures
- Databases

The findings informed a structured enhancement plan implemented during CS 499: Computer Science Capstone.

## Identified Weaknesses

### 1. Software Design and Engineering

* The application was contained in a single monolithic script (`app.py`)
* No modular file organization (e.g., no MVC pattern)
* Sensitive credentials (MongoDB URI) were hardcoded
* No implementation of logging or error tracking
* Dash callbacks were tightly coupled with layout code

#### Example of Original Constructor Code (Before Enhancement)

```python
def __init__(self):
    USER = 'aacuser'
    PASS = 'SNHU1234'
    HOST = 'nv-desktop-services.apporto.com'
    PORT = 32440
    DB = 'AAC'
    COL = 'animals'
    self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
    self.database = self.client[DB]
    self.collection = self.database[COL]
```

#### Issues with the constructor code:

* Hardcoded credentials (username, password, host, port)
* No use of environment variables for secure configuration
* No error handling for failed database connection
* No logging to indicate success or failure of connection
* Poor separation of concerns (configuration logic mixed in constructor)
* Not modular or reusable – config values are not centralized
* Sensitive credentials are exposed, violating security best practices

**Enhancement Plan – Software Design and Engineering:** I will replace hardcoded credentials with environment variables using
the `dotenv` package for better security. I will also modularize the configuration into a separate file or helper method, and
replace print statements with structured logging. This aligns with secure design practices and improves the maintainability and
readability of the code.

### 2. Algorithms and Data Structures

* Filtering logic was duplicated and not reusable
* Hardcoded conditions for specific rescue types
* No input validation or dynamic query handling
* Missed opportunities for vectorized operations with pandas
* Repeatedly filters the entire original DataFrame

#### Example of Original Filtering Code (Before Enhancement)

```python
if filter_type == 'water':
    filtered_df = df[(df['breed'].str.contains('Labrador Retriever')) &
                     (df['outcome_type'] == 'Euthanasia')]
```

#### Issues:

* Repeatedly filters the entire original DataFrame
* Overwrites previously filtered data
* Not reusable – specific to one filter case
* Lacks input validation for `filter_type`
* Does not handle empty or missing values
* Filtering logic is hardcoded and not dynamic

**Enhancement Plan – Algorithms and Data Structures:** I will refactor this into a reusable filtering function that accepts
dynamic inputs. This will eliminate repeated code, improve scalability, and make it easier to add or adjust filters without
rewriting logic.

### 3. Database Handling

* Static CSV file used on every app run instead of querying MongoDB live
* MongoDB connections were not managed securely or efficiently
* No use of `try-except-finally` blocks for error handling
* No separation of CRUD logic into reusable functions

#### Example of Original Filtering Code (Before Enhancement)

```python
if filter == 'disaster':
    df = df[df['animal_type'] == 'Dog']
    df = df[df['age_upon_outcome_in_weeks'] > 52]
    df = df[df['sex_upon_outcome'].str.contains('Male')]
    df = df[df['outcome_type'].isin(['Adoption', 'Transfer'])]
```

#### Issues:

* Logic is hardcoded and repeated across filters
* Not abstracted into a function or reusable structure
* No validation or dynamic input handling

**Enhancement Plan – Databases:** I will improve exception handling, validate inputs for all CRUD methods, and move these methods
into a dedicated module. I will also connect to MongoDB live using secure credentials stored in a `.env` file and manage connections
using proper `try-except-finally` blocks.

## Outcomes Met Through Review

* **Outcome 3 (Software Design and Engineering):** Implemented modular design and secure coding practices
* **Outcome 4 (Algorithms and Data Structures):** Improved filter logic and implemented input validation
* **Outcome 5 (Databases):** Optimized database interaction and ensured secure handling


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


