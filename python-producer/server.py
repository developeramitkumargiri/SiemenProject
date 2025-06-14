import os
import sqlite3
import random
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from faker import Faker

app = FastAPI()
faker = Faker()


def initialize_db():
    conn = sqlite3.connect("data.db", check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS data")  
    cursor.execute("CREATE TABLE data (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)")

    for _ in range(10):  
        cursor.execute("INSERT INTO data (name, value) VALUES (?, ?)", (faker.name(), random.randint(100, 1000)))

    conn.commit()
    conn.close()

initialize_db() 

@app.get("/data")
def get_data(page: int = 1, page_size: int = 10):
    conn = sqlite3.connect("data.db", check_same_thread=False)
    cursor = conn.cursor()

    offset = (page - 1) * page_size
    cursor.execute("SELECT * FROM data ORDER BY id DESC LIMIT ? OFFSET ?", (page_size, offset))
    
    rows = cursor.fetchall()
    conn.close()
    
    # return {"data": rows, "page": page, "page_size": page_size}

    formatted_data = [{"id": row[0], "name": row[1], "value": row[2]} for row in rows]

    return {"data": formatted_data}

    # return {"data": rows}

@app.get("/next")
def insert_new_data():
    conn = sqlite3.connect("data.db", check_same_thread=False)
    cursor = conn.cursor()

    for _ in range(10): 
        cursor.execute("INSERT INTO data (name, value) VALUES (?, ?)", (faker.name(), random.randint(100, 1000)))

    conn.commit()
    conn.close()

    return {"message": "10 new records added!"}

app.mount("/static", StaticFiles(directory="templates"), name="static")

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    file_path = os.path.join("templates", "index.html")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return HTMLResponse(content=file.read())
    return HTMLResponse("<h1>Page Not Found</h1>", status_code=404)