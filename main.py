from include.extract import get_recent_tracks
from include.load import create_table, load_tracks
from include.transform import transform_tracks
import sqlite3

#Run extract, transform, and load in sequence
def run_pipeline():
    conn = sqlite3.connect("spotify_recently_played.db")
    results = get_recent_tracks()

    #Prevents transform_tracks() from being called if extract API call failed
    if results is None:
        print("Pipeline stopped: failed to fetch data from Spotify.")
        return 
    
    df = transform_tracks(results)
    create_table(conn)
    load_tracks(df,conn)

#Only execute the pipeline when this file is run directly (for future Airflow DAG implementation)
if __name__ == "__main__":
    run_pipeline()
