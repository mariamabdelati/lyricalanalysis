import os
#from unittest import result
#from webbrowser import get
#from matplotlib.pyplot import title
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#from bs4 import BeautifulSoup
import time
import numpy as np
import requests
from requests.exceptions import Timeout
#import sys
import logging
from pprint import pprint
import lyricsgenius


logger = logging.getLogger('scaper')
logging.basicConfig(level='INFO')

client_id = "48c55dd9e076465db2cb6a0e8b18c9e3"
client_secret = "3707f6ad41a74a6dbfff992baf8b6614"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def get_artist_uri(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        #pprint(items[0]['uri'])
        print(items[0]['uri'])
        return items[0]['uri']
    else:
        return None

def get_artist_info(uri):
    name = []
    total_followers = []
    artist_image_url = []
    genres = []
    popularity = []
    artist_data = sp.artist(uri)
    #pprint(artist_data)

    name.append(artist_data['name'])
    total_followers.append(artist_data['followers']['total'])
    artist_image_url.append(artist_data['images'][1]['url'])
    genres.append(artist_data['genres'])
    popularity.append(artist_data['popularity'])
    
    df1 = pd.DataFrame({
    'artist_name':name,
    'artist_total_followers':total_followers,
    'artist_image':artist_image_url,
    'genres':genres,
    'popularity':popularity})
    
    return df1 

def show_album_tracks(album):
    uri = []
    track = []
    duration = []
    explicit = []
    track_popularity = []
    track_number = []
    artist =[]
    results = sp.album_tracks(album['id'])
    #pprint(results['items'][1])
    df1 = pd.DataFrame(results)
    #to avoid sending too many requests to api
    sleep_min = 2
    sleep_max = 5
    start_time = time.time()
    request_count = 0
    for i, x in df1['items'].items():
        request_count+=1
        if request_count % 5 == 0:
            print(str(request_count) + " tracks completed")
            time.sleep(np.random.uniform(sleep_min, sleep_max))
            print('Loop #: {}'.format(request_count))
            print('Elapsed Time: {} seconds'.format(time.time() - start_time))
        pop = get_track_popularity(x['uri'])
        multi_artists = []
        for j in range(len(x['artists'])):
            multi_artists.append(x['artists'][j]['name'])
        artist.append(multi_artists)
        uri.append(x['uri'])
        track.append(x['name'])
        track_popularity.append(pop)
        duration.append(x['duration_ms'])
        explicit.append(x['explicit'])
        track_number.append(x['track_number'])  
    
    df2 = pd.DataFrame({
    'song_artists':artist,
    'uri':uri,
    'track_name':track,
    'duration_ms':duration,
    'explicit':explicit,
    'track_popularity': track_popularity,
    'track_number':track_number})
    
    return df2

def get_artist_albums(artist):
    all_data = pd.DataFrame()
    albums = []
    results = sp.artist_albums(artist, album_type='album')
    # pprint(results["items"][0])
    albums.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    logger.info('Total albums: %s', len(albums))
    unique = set()  # skip duplicate albums
    for album in albums:
        name = album['name'].lower()
        if name not in unique:
            logger.info('ALBUM: %s', name)
            unique.add(name)
            album_data = get_album(album['uri'])
            track_df = show_album_tracks(album)
            track_df['album_name'] = album_data['name']
            track_df['album_artist'] = album_data['artists'][0]['name']
            track_df['album_release_date'] = album_data['release_date']
            track_df['genres'] = album_data['genres'] if len(album_data['genres']) != 0 else None
            track_df['label'] = album_data['label']
            track_df['album_popularity'] = album_data['popularity']
            track_df['album_cover'] = album_data['images'][1]['url'] if len(album_data['images']) != 0 else None
            all_data = all_data.append(track_df, ignore_index=True)
    return all_data
    

def get_album(album_uri):
    results = sp.album(album_uri)
    #pprint(results)
    return results

def get_track_popularity(track_uri):
    results = sp.track(track_uri)
    #pprint(results)
    return results['popularity']

#insert output dataframe from the get_album_tracks function
def get_track_info(df):
    acousticness = []
    danceability = []
    energy = []
    instrumentalness = []
    key = []
    liveness = []
    loudness = []
    mode = []
    speechiness = []
    tempo = []
    time_signature =[]
    valence = []
    
    #to avoid sending too many requests to api
    sleep_min = 2
    sleep_max = 5
    start_time = time.time()
    request_count = 0

    for i in df['uri']:
        request_count+=1
        if request_count % 5 == 0:
            print(str(request_count) + " tracks completed")
            time.sleep(np.random.uniform(sleep_min, sleep_max))
            print('Loop #: {}'.format(request_count))
            print('Elapsed Time: {} seconds'.format(time.time() - start_time))
        for x in sp.audio_features(tracks=[i]):
            acousticness.append(x['acousticness'])
            danceability.append(x['danceability'])
            energy.append(x['energy'])
            instrumentalness.append(x['instrumentalness'])
            key.append(x['key'])
            liveness.append(x['liveness'])
            loudness.append(x['loudness'])
            mode.append(x['mode'])
            speechiness.append(x['speechiness'])
            tempo.append(x['tempo'])
            time_signature.append(x['time_signature'])
            valence.append(x['valence']) 
            
    df2 = pd.DataFrame({
    'acousticness':acousticness,
    'danceability':danceability,
    'energy':energy,
    'instrumentalness':instrumentalness,
    'key':key,
    'liveness':liveness,
    'loudness':loudness,
    'mode':mode,
    'speechiness':speechiness,
    'tempo':tempo,
    'time_signature':time_signature,
    'valence':valence})

    return df2

def merge_frames(df1, df2):
    merged_df = df1.merge(df2, left_index= True, right_index= True)
    return merged_df


CLIENT_ACCESS_TOKEN = "-bFmB_1NeOCHxvd21MGlWp0ntrM95eseLbPWnYs3SnZcXIa4wf2JmQX0lFlIby9r"
genius = lyricsgenius.Genius(CLIENT_ACCESS_TOKEN)
BASE_URL = "https://api.genius.com"

# send request and get response in json format.
def _get(path, params=None, headers=None):

    # generate request URL
    requrl = '/'.join([BASE_URL, path])
    token = "Bearer {}".format(CLIENT_ACCESS_TOKEN)
    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

    response = requests.get(url=requrl, params=params, headers=headers)
    response.raise_for_status()

    return response.json()

def genius_get_song_id(song, artist):
    find_id = _get("search", {'q': song})
    #pprint(find_id)
    song_id = None
    for hit in find_id["response"]["hits"]:
        if hit["index"].lower() == 'song' and artist.lower() in hit["result"]["primary_artist"]["name"].lower():
            song_id = hit["result"]["id"]
            break
    return song_id

def get_song_lyrics(df):
    song_lyrics = []
    lyrics_page_views = []
    featured_artists = []
    cleaned_title = []
    genius = lyricsgenius.Genius(CLIENT_ACCESS_TOKEN, skip_non_songs=True, verbose=True)
    genius.timeout = 15
    genius.sleep_time = 5  # 2
    # or: Genius(token, timeout=15, sleep_time=40)

    for i, x in df.iterrows():
        song_id = genius_get_song_id(song=x['track_name'], artist=x['album_artist'])
        if song_id != None:
            retries = 0
            while retries < 5:
                try:
                    song = genius.lyrics(song_id=song_id, remove_section_headers=True)
                    #song_lyrics.append(song)
                    song_obj = genius.song(song_id=song_id)
                    
                    #pprint(song_obj)
                    if 'pageviews' in song_obj['song']['stats']:
                        lyrics_page_views.append(song_obj['song']['stats']['pageviews']) if song_obj['song']['stats']['pageviews'] != 0 else lyrics_page_views.append(None)
                    else:
                        lyrics_page_views.append(None) 
                    
                    if 'featured_artists' in song_obj['song']:
                        featured = song_obj['song']['featured_artists']
                        if len(featured) != 0:
                            multi_artists = []
                            for j in range(len(featured)):
                                multi_artists.append(featured[j]['name'])
                            featured_artists.append(multi_artists)
                        else:
                            featured_artists.append(None)
                    else:
                        featured_artists.append(None) 
                    
                    cleaned_title.append(song_obj['song']['title'])
                
                    #song = genius.search_song(title=x['track_name'], artist=x['album_artist'])
                except Timeout as e:
                    retries += 1
                    continue
                except requests.HTTPError as h:
                    retries += 1
                    continue
                except ConnectionError as c:
                    retries += 1
                    continue
                if song is not None:
                    song_lyrics.append(song)
                else:
                    song_lyrics.append(None)
                break
        else:
            song_lyrics.append(None)
            featured_artists.append(None) 
            cleaned_title.append(None)
            lyrics_page_views.append(None) 

    df['song_lyrics'] = song_lyrics
    df['lyrics_page_views'] = lyrics_page_views
    df['cleaned_title'] = cleaned_title
    df['featured_artists'] = featured_artists
    return df

artist_names = open("1_Scraping_ArtistNames/artists.txt").read().splitlines()
#artis_names = artist_names[0:2] #testing case
for name in artist_names[21:]:
    artist_uri = get_artist_uri(name)
    #artist = get_artist_info(artist_uri)
    #print(get_artist_albums(artist_uri))
    #get_artist_albums(artist_uri).to_csv("Songs.csv", index=False)

    tracks_df = get_artist_albums(artist=artist_uri)
    track_audio_features = get_track_info(tracks_df)
    completed_df = merge_frames(tracks_df, track_audio_features)
    #completed_df = completed_df.drop_duplicates(subset=['track_name'])
    df_lyrics = get_song_lyrics(completed_df)
    output_path="Songs.csv"
    df_lyrics.to_csv(output_path, mode='a', header=not os.path.exists(output_path), index=False)
    print(f"\n\nFinished Artist: {name}\n\n")