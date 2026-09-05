# Spotify Airflow ETL Pipeline
An end-to-end ETL pipeline that extracts my recent Spotify listening activity from the Spotify Web API, transforms it into a clean dataframe, and loads it into a SQLite database with deduplication logic. The whole process is orchestrated with Apache Airflow running in Docker.

# Overview
This project extracts my recent listening history data from Spotify's `recently-played` endpoint, transforms the raw JSON response into a structured dataframe (track name, artist name, and timestamp), and loads it into a local SQLite database. The endpoint returns a rolling, overlapping window of 50 recent plays at a time, so the pipeline is designed to safely handle overlapping data across repeated runs. The entire pipeline is orchestrated with Apache Airflow, containerized with Docker, and scheduled to run on an hourly basis.

# Tech Stack 
* Python
* spotipy - Spotify Web API Wrapper
* pandas - data transformation
* SQLite - local storage
* Apache Airflow - orchestration and task scheduling
* Docker / Docker Compose - containerized environment


# Project Structure
```
├── dags/
|   └── spotify_pipeline.py               # Airflow DAG: wires extract > transform > load as tasks
├── database/
|   └── spotify_recently_played.db        # NOT COMMITTED - SQLite database                       
├── include/
|   ├── extract.py                        # Authenticates and fetches raw data from Spotify API
|   ├── load.py                           # Creates database table and handles dedup logic
|   ├── transform.py                      # Converts raw JSON into a structured dataframe
|   └── .cache                            # NOT COMMITTED - Spotify OAuth refresh token
├── .env                                  # NOT COMMITTED - Spotify and Airflow credentials
├── .gitignore
├── Dockerfile                            # Extends official Airflow image with project dependencies 
├── README.md                             
├── docker-compose.yaml                   # Official Airflow docker-compose setup 
├── main.py                               # Main entry point for running pipeline outside Airflow
└── requirements.txt                      # spotipy, pandas, python-dotenv
```
# Setup

1. Clone the repository.
   
2. Register an app at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) to get a Client ID and Client Secret. Copy them down.
   
3. Create a `.env` file in the project root and add your credentials:
```bash
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
```

4. Build and start Airflow.
```bash
docker compose up --build -d
```

5. Visit `localhost:8080` (default login: `airflow` / `airflow`) and unpause the `spotify_pipeline` DAG

6. **First-time authorization**: run `main.py` locally once to complete Spotify's browser-based OAuth flow. This generates a cached refresh token inside `include/` which the containerized pipeline reuses afterward without needing browser access.

# Notes
This pipeline runs locally via Docker Desktop, so scheduled runs only occur while the host machine is awake and Docker is running. 
