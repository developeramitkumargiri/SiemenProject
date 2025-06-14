# SiemenProject - Dockerized FastAPI Producer & C# Consumer

## Overview
This project implements a **producer-consumer** model where:
- **A Python producer** generates and stores **random data** in an SQLite database.
- **A C# consumer** fetches and processes the data via an **HTTP request**.
- Both services run inside **Docker containers and are orchestrated** using Docker Compose.
  

---

## Technologies Used
- Python 3.11 , FastAPI, Uvicorn , Faker , SQLite3 , C# (.NET 8) , Docker , Docker-Compose and GitHub 


## How to Run the Application

  ### Prerequisites  
  1. Before running, ensure the following are installed:
    - **Docker & Docker Compose** → [Download here](https://www.docker.com/products/docker-desktop)
  2. Fetch code from Git and Open with VS Code Studio.
  
  ### Build and Start the Containers
  - docker-compose up -d --build  -> (Run this command inside , root folder after getting code from Github in VS code ,It will create image and create container)
  - http://localhost:5000/data?page=1&page_size=10 -> You should see JSON data
  - http://localhost:5000/ -> To see UI table with fetched data
