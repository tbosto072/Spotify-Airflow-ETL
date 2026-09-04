from airflow.sdk import dag, task
from datetime import datetime
import sys 
import sqlite3
import pandas as pd
from io import StringIO

sys.path.insert(0, '/opt/airflow/include')

from extract import get_recent_tracks
from transform import transform_tracks
from load import create_table, load_tracks


@dag(
    dag_id="spotify_pipeline", 
    start_date=datetime(2026,1,1), 
    schedule="@hourly",
    catchup=False
)
def spotify_pipeline():

    @task
    def extract():
        return get_recent_tracks()
    
    @task 
    def transform(results):
        df = transform_tracks(results)
        return df.to_json()

    @task
    def load(df):
        conn = sqlite3.connect("/opt/airflow/database/spotify_recently_played.db")
        df = pd.read_json(StringIO(df), convert_dates=False)
        create_table(conn)
        load_tracks(df,conn)

    results = extract()
    df = transform(results)
    load(df)


spotify_pipeline()
