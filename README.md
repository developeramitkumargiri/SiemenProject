# SiemenProject - Dockerized FastAPI Producer & C# Consumer

## Overview
SiemenProject is a **containerized microservice application** that integrates a **Python FastAPI Producer** and a **C# Consumer** using Docker.  
- The **Python Producer** serves randon data via an API.  
- The **C# Consumer** fetches and processes data from the Producer and list on UI.
- Both services are managed using **Docker Compose** for seamless deployment.  

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
