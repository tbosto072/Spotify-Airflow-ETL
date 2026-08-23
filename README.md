# Spotify Airflow ETL
A personal ETL pipeline that pulls my recent Spotify listening activity from the Spotify Web API, transforms it into a clean dataframe, and loads it into a SQLite database. Eventually, this pipeline will be automated with Apache Airflow.

# Overview
This project extracts my recent listening history data from Spotify's `recently-played` endpoint, transforms the raw JSON response into a structured dataframe (track name, artist name, and timestamp), and loads it into a local SQLite database. The endpoint returns a rolling, overlapping window of 50 recent plays at a time, so the pipeline includes deduplication logic to ensure re-running the pipeline never creates duplicate records.

# Tech Stack 
* Python
* spotipy - Spotify Web API Wrapper
* pandas - data transformation
* SQLite - local storage
* Apache Airflow - orchestration and task scheduling (*planned*)


# Project Structure
```
├── .gitignore                            
├── README.md                             
├── extract.py                            # Authenticates and fetches raw data from Spotify API
├── load.py                               # Loads data into SQLite DB with dedup logic
├── main.py                               # Orchestrates full pipeline
├── test_auth.py                          # Initial exploratory test file
└── transform.py                          # Converts raw JSON to a clean dataframe
```
# Quick Start

1. Clone the repository and install dependencies:
```bash
pip install spotipy pandas python-dotenv
```
2. Register an app at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) to get a Client ID and Client Secret. Copy them down.
3. Create a `.env` file in the project root:
```bash
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
```
4. Run the pipeline:
```bash
python main.py
```

# Roadmap
* Orchestrate with Apache Airflow for scheduled, automated runs
* Add retry/error handling for API failures
   
