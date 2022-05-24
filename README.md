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
| | [Data Storage and Management](#data-storage)|
| | [Exploratory Data Analysis (EDA)](#eda)|
| | [Sentiment Analysis](#sentiment-analysis)|
| | [Libraries Used](#libraries)|
| | [Next Steps](#next)|

<h3>Data Gathering and Collection</h3><a id='data-collection'></a>

Track Data and Lyrics was gathered with the help of Spotipy and lyricsgenius libraries to facilitate pulling data from the Spotify and Genius APIs. To begin, the artist names for which songs were to be considered were taken from the top 1000 streaming artists on spotify using selenium webdriver. Next the artist data was pulled using spotipy and exported and can be found in [ArtistDetails.csv](./1_Data_Acquisition/2_Artist_Data_Acquisition/ArtistDetails.csv). Next the track data was pulled using spotipy and the lyrics and some related data was retrieved using lyricsgenius. Additionally, there was a direct interaction with the Genius API to retrieve song Ids to maintain accurate song retrieval. Multithreading was adopted at this stage to speed the data retrieval process and make it more efficient. The total number of records retrieved is 159,231 with 30 unique columns and 700 different artists. The data can be found in [All_Songs.csv](./1_Data_Acquisition/All_Songs.csv)

<h3>Cleaning and Obtaining Final Data</h3><a id='data-cleaning'></a>

After looking through the data collected from the Spotify and Genius APIs, it was noticed that there are several non-lyrics retrieved from the Genius API instead of song lyrics which need to be removed. Additionally, the Spotify API did not return any genres for the songs which makes the genres column insignificant to the analysis. Also, there were several duplicate track uri’s meaning that some tracks were retrieved from the Spotify API more than once, probably due to artists singing on the same track and so the track was scraped for both artists. All these errors are handled in this phase.

The following steps were followed:
- Handling duplicates for song uri -> removed
- Renaming columns for consistency and descriptiveness
- Re-organizing columns in a more logical order
- Re-formatted data types for several columns for consistency
- Handling errors:
  - spotify did not return any genres-> feature engineering
  - genius returned the wrong lyrics for a several songs 
- Cleaning up the lyrics removing line breaks for storage on the hive server

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

<h3>Data Storage and Management</h3><a id='data-storage'></a>

The modified csv file is uploaded to the Hadoop Hive server through docker in order to perform map reduce on the data. This concept allows for parallel data processing which gives benefits such as speed and efficiency. Details about set up can be found in [Docker-Setup.md](./Docker-Setup.md)

<h3>Exploratory Data Analysis (EDA)</h3><a id='eda'></a>

With the aim to gain more insight into the data collected, I analyzed some track features with help of graphs and comparisions with other songs. Some of those include:
- determining the top 15 artists, who made up almost 19% of all songs collected
- determining the top genres: pop and rock made up 51% of all data collected
- determining the top years of release: 2020 and 2021 were the top years which is around the time of the pandemic and when tiktok gained more popularity
- comparing audio features pre-2000s and post-2000s: it was found that post 2000s music has higher energy which indicates higher intensity
- comparing audio features of top songs with all other songs: it was found that top songs have higher average danceability than all songs

<h3>Sentiment Analysis</h3><a id='sentiment-analysis'></a>

For the purpose of the project, this phase is necessary in order to gain insight into the track lyrics. To begin, the data was analysed to determine the beginning point. It became apparent that the lyrical data was made up of several languages such as Spanish or German. After performing some research on multilingual sentiment analysis, it was concluded that the sentiment analysis process is exactly the same for any other language as it were for English. However, some pre-processing to classify the languages is required in order to specify the language of choice to the text processing library.

It was determined thhat analyzing each language separately would result in the least loss of data of only 2.6%. Data frames for each langauge are thus created and it was time for preprocessing. 
The steps followed included:
1. Lowercasing
2. Removing the first line from lyrics since the genius API returns the name of the song as part of the song lyrics and that is unnecessary for the analysis.
3. Removing the “Embed” word from the end of the lyrics since the Genius API returned an “embed” word at the end of every lyrics which is also unnessecary for the analysis.
4. Normalizing contractions for the English language since there are many contractions commonly used which can affect the words of the sentence if decontracted. For other languages, it is difficult to identify the common contractions as the support for the other languages is not widely available, and several contractions can have different meanings in different context. Additionally, most contractions in languages such as French or German are prepositions or pronouns which do not have a huge contribution to sentiment analysis (as opposed to English contractions which shorten verbs) as they are generally considered neutral. Hence, for the purpose of the analysis contractions for other languages will not be considered and this can be an extension to the analysis.
5. Removing special characters and numbers
6. Removing short or empty lyrics

Text Normalization then took place to normalize the data for the analysis. The following steps were taken:
1. Removing Stop Words, or words that do not have much significance to the meaning of the sentence such as pronouns or prepositions. This was done based on each language by using the passing the language of the lyrics as a parameter to the stop words function.
2. Stemming which is used to remove suffixes from the words in order to reduce words with a common root to the same form. The stemming process is not grammatically correct since it strips words based on a set of rules rather than using linguistic roots based on the part of speech.
3. Thus, lemmatization was used since it takes into consideration the part of speech for the word i.e., whether the word is a noun, verb adjective, adverb, etc. This approach is more sensible to the analysis as the words are actually part of the language’s vocabulary and it is easy to tell what the word is compared to stemming.

Afterwards, the word count for the most frequent words in the lyrics were determined. This was done by splitting the words and counting the unique ones. 

Next, the polarity score of the lyrics was calculated with the help of textblob/vader in order to gain insight on whether the lyrics collected are more positive or negative based on the words in those lyrics.

<h3>Libraries Used</h3><a id='libraries'></a>

- selenium webdriver
- pandas
- concurrent futures
- spotipy
- lyricsgenius
- time 
- numpy
- requests
- regex
- matplotlib
- swifter
- seaborn
- plotly
- langid
- nltk
- wordcloud
- textblob
- pattern

<h3>Next Steps</h3><a id='next'></a>

The next steps is to continue performing a more detailed EDA to get further insights into song data as well as understand the trends in music features patterns. Additionally, a dashboard can be used to display the figures and graphs in a more organized and clear manner and allow users to select the audio features and settings of their choice. The project can also be further extended to have a recommendation engine for suggesting similar artists. Machine Learning can also be used to train models to analyze audio features and lyrics. 
