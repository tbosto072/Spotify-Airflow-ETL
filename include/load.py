import sqlite3
import pandas as pd

conn = sqlite3.connect("spotify_recently_played.db")

#Set up plays table if it doesn't exist yet
def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS plays (
            track_name TEXT,
            artist_name TEXT,
            played_at TEXT
        )
    """)
    conn.commit()

#Takes passed dataframe and DB connection and filters out existing rows
#by comparing 'played_at' values so no duplicates are appended when pipeline is rerun
def load_tracks(df, conn):
    existing = pd.read_sql("SELECT played_at FROM plays", conn)
    new_rows =  df[~df['played_at'].isin(existing['played_at'])]
    new_rows.to_sql("plays", conn, if_exists="append", index=False)
    print("New songs fetched: " + str(len(new_rows))) #Logs amount of songs fetched every call
