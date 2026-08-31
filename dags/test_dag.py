from airflow.sdk import dag, task
from datetime import datetime
import spotipy

@dag(start_date=datetime(2026,1,1), schedule="@daily")
def test_dag():

    @task
    def say_hello():
        print("Hello from task 1")

    @task
    def say_goodbye():
        print("Goodbye from task 2")

    @task
    def test_spotipy():
        print(spotipy.Spotify)

    say_hello() >> say_goodbye() >> test_spotipy()

test_dag()