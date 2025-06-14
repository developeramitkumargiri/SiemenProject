# SiemenProject - Dockerized FastAPI Producer & C# Consumer

## Overview
This project implements a **producer-consumer** model where:
- **A Python producer** generates and stores **random data (Id, Username and Value)** in an SQLite database.
- **A C# consumer** fetches and processes the data via an **HTTP request**.
- Both services run inside **Docker containers and are orchestrated** using Docker Compose.
  
## Technologies Used
- Python 3.11 , FastAPI, Uvicorn , Faker , SQLite3 , C# (.NET 8) , Docker , Docker-Compose and GitHub 

## How to Run the Application

### Prerequisites

1. Ensure the following steps are completed:

   - Installed **Docker & Docker Desktop** → [Download here](https://www.docker.com/products/docker-desktop)

   - Login into Docker Desktop to start Docker Engine.

   - Make sure Docker is running  
     *(To confirm, open Docker-Desktop and check the status)*.
     
  2. Open Source code with VS Code.
  
  ### Build ,Start the Containers and see the Output

##### 1. To build Images and Run Containers:
      - docker-compose up -d --build
#### 2. Most Used Commands to monitor Docker and Containers
      - docker ps → Lists running containers.
      - docker ps -a → Lists all containers, including stopped ones.
      - docker exec -it <container-name> <command> → Runs a command inside a running container.
      - docker logs <container-name> → Shows the logs of a running container.
      - docker-compose down → Stops and removes all services in the docker-compose.yml file
      
##### 2. To See UI Table & API response , run below commands in browser
       - http://localhost:5000    -> See table list , using next and previous button
       - http://localhost:5000/data?page=1&page_size=10   -> To fetch dynamic data , change page and page_size
       - http://localhost:5000/next   -> To insert 10 new data into SQLite
     
##### 3. To see the fetched result from SQLite by C# Consumer , run below commands in cmd
       - docker exec -it csharp-client dotnet run   -> To run Api and fetch first 10 data
       - docker exec -it csharp-client curl "http://fastapi-service:5000/data?page=1&page_size=10"  -> To fetch dynamic data , change page and page_size
       - docker exec -it csharp-client curl "http://fastapi-service:5000/next   -> To insert 10 new data into SQLite
    
  
  ### For any clarification , contact on below
    developeramitkumargiri@gmail.com
