# Lyrical Analysis

*Big Data Programming Project -- University Junior Year*
##### Mariam Abdelati

<h3>Problem Description<a id='problem-description'></a></h3>

Being a music fan myself, I am constantly discovering new music and compiling playlists to match different moods and tastes on spotify. Thus, I became curious to explore how different aspects of a song such as its genre, key signature, and lyrics can affect it's popularity. I also wanted to explore the textual content of the lyrics and discover the sentiment of the songs present nowadays.

#### Project Table of Contents
| Navigation | Description |
| ----- | ----- |
| Python Files ||
|  | **[Data Acquistion](./1_Data_Acquisition)**|
|  | &emsp;  [Retieving Artist Names](./1_Data_Acquisition/1_Scraping_ArtistNames/get_artists_names.py)|
|  | &emsp;  [Retieving Artist Data from Spotify](./1_Data_Acquisition/2_Artist_Data_Acquisition/get_artist_data.py)|
|  | &emsp; *[Retieving Track Details from Spotify and Genius](./1_Data_Acquisition/3_Track_Data_Acquistion)*|
|  | &emsp; &emsp; [Single-Threaded Scraper](./1_Data_Acquisition/3_Track_Data_Acquistion/track_scaper.py)|
|  | &emsp; &emsp; [Multi-Threaded Scraper](1_Data_Acquisition/3_Track_Data_Acquistion/mulithreaded_scraper.py)|
| Notebooks ||
|  | [Data Cleanup](./2_Data_Cleaning/data_clean_up.ipynb)|
|  | [EDA](./4_EDA/Track_Features_EDA.ipynb)|
|  | [Sentiment Analysis](./5_Sentiment_Analysis/track_lyrics_sentiment_analysis.ipynb)|
|ReadMe  | |
| | [Problem Description](#problem-description)|
| | [Data Gathering and Collection](#data-collection)|
| | [Cleaning and Obtaining Final Data](#data-cleaning)|
| | [Final Data Columns Dictionary](#data-dictionary)|
| | [Exploratory Data Analysis (EDA)](#eda)|
| | [Sentiment Analysis](#sentiment-analysis)|
| | [Conclusion](#conclusion)|
| | [Libraries Used](#libraries)|
| | [Next Steps](#next)|

<h3>Data Gathering and Collection</h3><a id='data-collection'></a>

Track Data and Lyrics was gathered with the help of Spotipy and lyricsgenius libraries to facilitate pulling data from the Spotify and Genius APIs. To begin, the artist names for which songs were to be considered were taken from the top 1000 streaming artists on spotify using selenium webdriver. Next the artist data was pulled using spotipy and exported and can be found in [ArtistDetails.csv](./1_Data_Acquisition/2_Artist_Data_Acquisition/ArtistDetails.csv). Next the track data was pulled using spotipy and the lyrics and some related data was retrieved using lyricsgenius. Additionally, there was a direct interaction with the Genius API to retrieve song Ids to maintain accurate song retrieval. Multithreading was adopted at this stage to speed the data retrieval process and make it more efficient. The data can be found in [All_Songs.csv](./1_Data_Acquisition/All_Songs.csv)

<h3>Cleaning and Obtaining Final Data</h3><a id='data-cleaning'></a>


<h3>Final Data Columns Dictionary</h3><a id='data-dictionary'></a>
##### Track Table
|Column Name|Description|
|---|---|
|track_uri|The Spotify Unique Identifier (ID) for each track.|
|track_name|Name of Track including Featured Artists.|
|cleaned_track_name|Name of the Track without Featured Artists.|
|track_artists|Name of all Artists on the Track including Featured Artists.|
|featured_artists|Names of Featured Artists on the Track excluding main artist.|
|track_is_explicit|Boolean indicating whether the song contains explicit content.|
|track_popularity| The Popularity of the Track as calculated by the Spotify Algorithm using the recent number of plays.|
|track_genres|The genres of the track as derived from the Artists' Genres performing on the track.|
|track_duration_ms|The track length in milliseconds|
|track_time_signature|The time signature of the song which specifies how many beats are in each bar; ranges from 3 to 7 indicating time signatures of "3/4", to "7/4".|
|track_acousticness|Confidence measure indicating whether a track is acoustic.|
|track_danceability|Indicates how suitable a track is for dancing based on several musical elements.|
|track_energy|Indicates the intensity and activity of a song based on several music elements. Typically high energy is characterized by being fast, loud, and noisy.|
|track_key_signature|The key signature of the song calculated using the key and mode values|
|track_instrumentalness|Predicts whether or not a track has no vocals. "Ooh" and "Aah" sounds are treated as instrumental. Values above 0.5 are intended to be intrumental.|
|track_key|The key the track is in represented using integers mapping to pitch class notation|
|track_mode|Indicates 1 for major scale and 0 for minor scale|
|track_liveness|Detects the presence of an audience in the recording. Values above 0.8 indicate strong liklihood the track is live|
|track_loudness|The overall loudness of a track in decibel (dB). Ranges from -60 and 0 dB.|
|track_speechiness|Detects the presence of spoken words in the track. Values above 0.66 indicate song is mode of spoken words, 0.33-0.66 indicate containing both music and speed in sections of layers. Below 0.33 most likely represents music and other non-speech tracks.|
|track_tempo|The beats per minute (BPM) in the song or the spead and pace of the track.|
|track_valence|Describes the track's musical positiveness; whether or not the track sounds positive.|
|track_lyrics|The Track Lyrics|
|lyrics_page_views|The number of views for the lyrics on Genius|
|track_number|The number of the track on the album|
|album_name|Name of Album where the Track Appears.|
|album_artist|The Main Artist of the Album where the Track Appears.|
|album_release_date|The date the album containing the track was released|
|album_popularity|The Popularity of the Album as calculated by the Spotify Algorithm using the popularity of the songs|
|album_record_label|The Record Label under which the Album was released|
|album_cover|The URL of the album cover|