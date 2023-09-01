import pandas as pd
from code.youtube_api import download_channels_videos

# Read channels.csv (adjust the file path if needed)
channels = pd.read_csv('channels.csv')

# Assuming 'slug' is a column in your channels data that provides a unique identifier for each channel
channels['slug'] = channels['title'].str.lower().replace(' ', '-')

# Call the function with the channels data
download_channels_videos(channels)
