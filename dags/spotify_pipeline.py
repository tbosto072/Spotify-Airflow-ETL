from airflow.sdk import dag, task
from datetime import datetime
import sys 
import sqlite3


@dag(
    dag_id="spotify_pipeline", 
    start_date=datetime(2026,1,1), 
    schedule="@hourly",
    catchup=False
)
def spotify_pipeline():

    @task
    def extract():
        return 0
    
    @task 
    def transform():
        return 0
    
    @task
    def load():
        return 0
   
    extract() >> transform() >> load()

spotify_pipeline()
