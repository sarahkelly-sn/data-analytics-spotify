<div align="center">
  <a href="https://github.com/spotify">
    <img src="https://avatars.githubusercontent.com/u/251374?s=200&v=4" alt="Logo" width="120" height="120">
  </a>

  <h1 align="center">Spotify Data Analysis</h1>

  <p align="center">
    <h3>Portfolio Project for Learning</h3>
  </p>
</div>


## About The Project

This project aims to analyze Spotify data, providing insights into listening habits and musical preferences. The primary goal is to collect and visualize various metrics for analysis in a Business Intelligence (BI) context.

The project collects data such as the most listened songs, artists, playlists, audio features, and historical listening data. The analysis will be conducted using Power BI.

### Data Collection

- The data includes:
  - Most listened tracks and artists
  - Recently played tracks
  - User playlists and their characteristics
  - Audio features for each track
  - Insights into genres and listening times
    
## Links to Project Files

Check out the code and visualizations that power the project. 
Click the links below to access the files.

-  [Python Code](https://github.com/sarahkelly-sn/data-analytics-spotify/blob/main/index.py)
-  [Power BI Report](seu-link-aqui)


  
## Built With

In this section, the main tools and libraries used in the development of this project are listed.

<div align="Center">
  
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Spotipy](https://img.shields.io/badge/Spotipy-1DB954?style=for-the-badge&logo=spotify&logoColor=white)](https://spotipy.readthedocs.io/en/2.22.1/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-003B57?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org)
[![Seaborn](https://img.shields.io/badge/Seaborn-0C4B33?style=for-the-badge&logo=seaborn&logoColor=white)](https://seaborn.pydata.org)

</div>

## Getting Started

To run this project locally, you will need to have Python and the necessary libraries installed on your machine.

### Prerequisites

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/). Make sure to check the box to add Python to your PATH during installation.
  
2. **Install Required Libraries**: Open your terminal or command prompt and run the following commands to install the required libraries:

   ```bash
   pip install pandas spotipy matplotlib seaborn
   ```
   
3. **Configure Spotify API Credentials**: 
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in with your Spotify account.
   - Create a new application to get your `Client ID` and `Client Secret`.
   - Set up a redirect URI for your application. For local development, you can use something like `http://localhost:8888/callback`.
   - Save your credentials securely, as you will need them to authenticate your API requests.

4. **Collect Your Data**: 
   - Use the Spotipy library to write a Python script that retrieves your desired data from Spotify. 
   - You can utilize various endpoints, such as fetching your top tracks or playlists. Here’s a simple example to get your top tracks:

   ```
   import spotipy
   from spotipy.oauth2 import SpotifyOAuth

   sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='YOUR_CLIENT_ID',
                                                  client_secret='YOUR_CLIENT_SECRET',
                                                  redirect_uri='YOUR_REDIRECT_URI',
                                                  scope='user-top-read'))

   top_tracks = sp.current_user_top_tracks(limit=20)
   for idx, track in enumerate(top_tracks['items']):
       print(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}")
   ```
   
5. **Save Data to CSV**: 
   - After retrieving your data, you can save it to a CSV file for further analysis in Power BI.

   ```
   import pandas as pd

   data = [{'track': track['name'], 'artist': track['artists'][0]['name']} for track in top_tracks['items']]
   df = pd.DataFrame(data)
   df.to_csv('top_tracks.csv', index=False)
   ```

### Analyzing Data in Power BI

1. **Import CSV to Power BI**:
   - Open Power BI Desktop.
   - Click on "Get Data" and select "Text/CSV".
   - Choose the `top_tracks.csv` file you created.

2. **Create Visualizations**:
   - Use Power BI’s features to create various visualizations based on the data imported.
   - You can analyze trends, compare artists, and explore your listening habits visually.

## Roadmap

Here's the roadmap listing all completed and ongoing stages for the current project:

- [x] **Setup of Python and Required Libraries**
- [x] **Configuration of Spotify API Credentials**
- [x] **Data Collection Script Development**
- [x] **Saving Data to CSV Format**
- [x] **Importing Data into Power BI**
- [x] **Creating Visualizations in Power BI**

## Contact

You can reach me through the following contact methods:

<br />

<div align="Center">
  
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Gmail][email-shield]][email-url]
[![Whatsapp][whatsapp-shield]][whatsapp-url]

</div>

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/sarah-kelly-024351155/
[email-shield]: https://img.shields.io/badge/Gmail-black?style=for-the-badge&logo=gmail&colorB=555&logoColor=white
[email-url]: mailto:sarah.sqn@gmail.com
[whatsapp-shield]: https://img.shields.io/badge/Whatsapp-black?style=for-the-badge&logo=whatsapp&colorB=555&logoColor=white
[whatsapp-url]: https://wa.me/5531983238839/


