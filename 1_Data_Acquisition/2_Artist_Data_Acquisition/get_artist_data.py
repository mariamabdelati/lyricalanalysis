# importing sys
import sys
  
# adding folder to the system path
sys.path.append('3_Track_Data_Acquistion')
 
# importing the get_artist_uri and get_artist_info functions
from mulithreaded_scraper import get_artist_uri, get_artist_info

artist_names = open("1_Scraping_ArtistNames/artists.txt").read().splitlines()

for name in artist_names:
    artist_uri = get_artist_uri(name)
    artist = get_artist_info(artist_uri)
    output_path="ArtistDetails.csv"
    artist.to_csv(output_path, mode='a', header=not os.path.exists(output_path), index=False)
    
    print(f"\n\nFinished Artist: {name}\n\n")