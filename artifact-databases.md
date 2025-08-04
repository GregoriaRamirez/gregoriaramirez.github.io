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
This complete try-except-finally block adds robust MongoDB error handling. It ensures that even if the connection fails, the application does not crash and returns a safe fallback — an empty DataFrame. Structured logging provides insight into issues, and the connection is always closed properly, preventing leaks and locking issues.

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

* **Outcome 5 (Databases):** Developed a security mindset by implementing secure credential storage, exception handling, and proper connection cleanup for MongoDB using Python.
* **Outcome 4 (Computing Tools and Practices):** Applied tools like `pymongo`, `dotenv`, and `pandas` to transform and serve real-time data from a database into an interactive dashboard.

---

## 🔗 Project Links

* 📁 [Original Code – animal\_shelter.py](https://github.com/GregoriaRamirez/gregoriaramirez.github.io/blob/main/original/animal_shelter.py)
* 📁 [Original Code – ProjectTwoDashboard.ipynb](https://github.com/GregoriaRamirez/gregoriaramirez.github.io/blob/main/original/ProjectTwoDashboard%20%281%29.ipynb)
* 📁 [Enhanced Code (GitHub Pages)](https://gregoriaramirez.github.io/artifact-databases)
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





