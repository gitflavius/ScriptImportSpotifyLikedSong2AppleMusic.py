markdown
# 🎵 Spotify Liked Songs to Apple Music Importer

A Python script that automatically transfers your liked songs from Spotify to Apple Music using Selenium WebDriver.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-orange)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

  ## ✨ Features
  
  - **Automated Transfer**: Moves your liked songs from Spotify to Apple Music seamlessly
  - **CSV Integration**: Works with exported Spotify data
  - **Smart Matching**: Finds the closest matches in Apple Music's library
  - **Playlist Management**: Automatically adds songs to your specified playlist
  - **User-Friendly**: Simple setup with clear instructions
  
  ## 📋 Prerequisites

Before using this script, ensure you have:

1. **Exported your Spotify liked songs** to a CSV file named `liked_songs.csv`
2. **Chrome browser** installed
3. **ChromeDriver** downloaded and placed in the script directory
4. **Python 3.8+** installed with required packages

## 🛠 Installation

1. **Clone the repository**:

  ```bash
    git clone https://github.com/yourusername/spotify-to-apple-music.git
    cd spotify-to-apple-music

    Install required packages:

    pip install selenium pandas
    Download ChromeDriver:
  
    Visit ChromeDriver download page
    
    Download the version matching your Chrome browser
    
    Place chromedriver.exe in the project folder
  ```

📁 File Structure
```text
spotify-to-apple-music/
├── ScriptimportSpotify.LikedSong2AppleMusic.py
├── chromedriver.exe
├── liked_songs.csv (you need to create this)
└── README.md
```
🚀 Usage

Prepare your Spotify data:

Export your liked songs from Spotify (using Spotify export tools)

Save as liked_songs.csv in the project directory

Run the script:

```bash
  python ScriptimportSpotify.LikedSong2AppleMusic.py
  Follow the prompts:
  
  The script will open Chrome and navigate to Apple Music
  
  Log in to your Apple Music account when prompted
  
  Create a playlist manually when instructed (named exactly as specified in the script)
  
  Press Enter in the terminal to continue
  
  Let the magic happen:
  
  The script will search for each song and add it to your playlist
  
  Progress will be shown in the terminal
```
⚙️ Configuration
Edit these variables in the script to customize:

```python
CSV_FILE = "liked_songs.csv"  # Your Spotify export file
APPLE_MUSIC_URL = "https://music.apple.com/"
PLAYLIST_NAME = "Minha Primeira Play"  # Exact name of your manually created playlist
📊 CSV Format Requirements
Your liked_songs.csv should contain at least these columns:

Track Name - The name of the song

Artist Name(s) - The artist(s) name
```

  ##  ⚠️ Important Notes
Internet Connection: Stable connection required for the entire process

Don't Close Browser: Keep the Chrome window open during execution

Manual Steps: You need to manually log in and create the initial playlist

Matching Accuracy: Some songs might not be found if titles/artists don't match exactly


  ##  🐛 Troubleshooting
Common issues and solutions:

ChromeDriver version mismatch:

Ensure ChromeDriver version matches your Chrome browser version

Element not found errors:

Apple Music's UI might have changed - check XPaths in the script

Login issues:

Make sure you're logged into Apple Music in the opened browser

Slow performance:

The script includes delays to ensure proper loading - be patient

🔧 Customization
You can modify these aspects:

Timing: Adjust time.sleep() values if needed

Search Logic: Modify the search term generation

Error Handling: Enhance exception handling for specific cases


  ## 🤝 Contributing
Feel free to contribute by:

Reporting bugs

Suggesting new features

Improving the documentation

Submitting pull requests


  ##  📄 License
This project is open source and available under the MIT License.

 
  ## ⭐ Support
If this project helped you, please give it a star on GitHub!

 
  ###  Note: This script is for educational purposes. Please respect the terms of service of both Spotify and Apple Music.

Happy listening! 🎧
