---
layout: default
title: Databases Enhancement
permalink: /artifact-databases
---

**Navigation:**  
[🏠 Home](index.md) | [📝 Self-Assessment](self-assessment.md) | [🎥 Code Review](code-review.md)| [🛠️ Software Design](artifact-software.md) | [🧠 Algorithms](artifact-algorithms.md) | [💾 Databases](artifact-databases.md) | [📂 Projects](projects.md)  | [🏆 Awards](awards.md) | [📄 Résumé](resume.md)

## 🗄️ Databases Artifact

### 📌 Artifact Description

For my CS 499 Capstone, I selected the database integration portion of my Animal Shelter Dashboard project, originally developed in February 2025 for CS 340: Client-Server Development. In the original version, I used hardcoded MongoDB credentials and manually accessed data through the Mongo shell. While the application functioned, it lacked secure credential management, proper error handling, and modular database logic.

For the enhanced version, I refactored the MongoDB access into a reusable Python module using `pymongo` and `dotenv`. I securely connected the Dash dashboard to MongoDB using environment variables and implemented structured logging. These enhancements allowed for more professional, secure, and reliable database operations that now support real-time filtering and analytics.

---

## 🔁 Before → After (Key Changes)

### 1) Secure Credential Management
**Before – animal_shelter.py (original):**
```python
USER = 'aacuser'
PASS = 'SNHU1234'
HOST = 'localhost'
PORT = 27017
DB = 'AAC'
COL = 'animals'
````

**After – model.py (enhanced):**

```python
from dotenv import load_dotenv
load_dotenv()

user = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")
host = os.getenv("MONGO_HOST", "localhost")
port = int(os.getenv("MONGO_PORT", 27017))
db_name = os.getenv("MONGO_DB")
collection_name = os.getenv("MONGO_COL")
```

➡️ I replaced all hardcoded credentials with environment variables loaded from a `.env` file. This prevents exposing passwords in the code and makes the project deployment-ready.

---

### 2) MongoDB Connection Handling

**Before – animal\_shelter.py (original):**

```python
client = MongoClient('mongodb://localhost:27017')
db = client['AAC']
collection = db['animals']
data = list(collection.find({}))
```

**After – model.py (enhanced):**

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

➡️ I wrapped the connection in a `try-except-finally` block with logging. Even if errors occur, the program returns a safe fallback and always closes the database connection.

---

### 3) Dropping Internal MongoDB Fields

**Before – animal\_shelter.py (original):**

```python
df = pd.DataFrame(mongo_data)
# _id field included in output
```

**After – model.py (enhanced):**

```python
if '_id' in df.columns:
    df.drop(columns=['_id'], inplace=True)
```

➡️ I removed the internal `_id` field before sending the data to the dashboard. This keeps the user interface clean and shows only meaningful fields.

---

## 🧠 Reflection on Database Skills

This artifact shows how I moved from insecure, hardcoded MongoDB shell commands to a secure, production-ready database connection in Python. By adding environment variables, error handling, logging, and cleanup, I demonstrated real-world database integration skills. The enhanced version is more secure, easier to maintain, and supports reliable data analysis.

---

## 🎓 Course Outcomes Met

* **Outcome 4 (Computing Tools and Practices):** Applied `pymongo`, `dotenv`, and `pandas` to securely connect, transform, and serve MongoDB data to the dashboard.
* **Outcome 5 (Databases):** Implemented secure credential management, exception handling, and connection cleanup. Replaced insecure hardcoding with environment variables and structured error handling.

---

## 🔗 Project Links

* 📁 [Original Code – animal\_shelter.py](https://github.com/GregoriaRamirez/gregoriaramirez.github.io/blob/main/original/animal_shelter.py)
* 📁 [Original Code – ProjectTwoDashboard.ipynb](https://github.com/GregoriaRamirez/gregoriaramirez.github.io/blob/main/original/ProjectTwoDashboard%20%281%29.ipynb)
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


