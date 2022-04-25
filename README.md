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

