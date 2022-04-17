CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;

CREATE EXTERNAL TABLE IF NOT EXISTS all_tracks (
  track_uri STRING,
  track_name STRING,
  cleaned_track_name STRING,
  track_artists STRING,
  featured_artists STRING,
  track_is_explicit BOOLEAN,
  track_popularity INT,
  track_genres STRING,
  track_duration_ms BIGINT,
  track_time_signature DOUBLE,
  track_acousticness DOUBLE,
  track_danceability DOUBLE,
  track_energy DOUBLE,
  track_key_signature STRING,
  track_instrumentalness DOUBLE,
  track_key DOUBLE, 
  track_mode DOUBLE,
  track_liveness DOUBLE,
  track_loudness DOUBLE,
  track_speechiness DOUBLE, 
  track_tempo DOUBLE,
  track_valence DOUBLE,
  track_lyrics STRING,
  lyrics_page_views DOUBLE,
  track_number INT,
  album_name STRING,
  album_artist STRING,
  album_release_date STRING,
  album_popularity INT, 
  album_record_label STRING,
  album_cover STRING
)

ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
STORED AS TEXTFILE 
LOCATION 'hdfs://namenode:8020/user/hive/warehouse/testdb.db/all_tracks';
