import pandas as pd

#Takes raw JSON API results as a parameter
#rather than fetching internally to keep data retrieval decoupled
def transform_tracks(results):
    rows = []
    for item in results['items']:
        rows.append({
            'track_name': item['track']['name'],
            'artist_name': item['track']['artists'][0]['name'],
            'played_at': item['played_at']
            })
    return pd.DataFrame(rows)
