# Spotify Automation Bot

In honor of Spotify Wrapped releasing, I've made this little Spotify automation bot.

This project automates following artists, on Spotify. It uses the `selenium` library to simulate user interactions with Spotify's web interface. The bot logs into Spotify with your credentials, navigates to the pages of specified artists, and clicks the "Follow" button for them.

### Key Features

-**Automated Login**: Logs into Spotify using provided credentials.

-**Follow Artists**: Automates the process of following artists using their Spotify URLs.

-**Randomized Delays**: Introduces random delays between actions to mimic human behavior.

-**Error Handling**: Handles common errors, such as missing elements.

### Prerequisites

- Python 3.x
- Chrome Browser
- Chrome Driver
- Spotify Account

### Installation

Install the required Python packages using pip:
```bash
pip install selenium
```
### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/spotify-automation-bot.git
cd spotify-automation-bot
```
2. Download [ChromeDriver](https://chatgpt.com/c/67563eea-2488-800f-ace4-5e2053953aae#:~:text=Download%20ChromeDriver%3A-,ChromeDriver,-Download).

3. Update the following fields in the script `(spotify_bot.py)`:

- `CHROME_DRIVER_PATH`: Path to the downloaded ChromeDriver executable.

- `SPOTIFY_EMAIL` and `SPOTIFY_PASSWORD`: Your Spotify login credentials.
Add artist URLs to the artist_urls list in the script.


## How to Run:
1. Open a terminal and navigate to the project directory.
2. Run the script:
```bash
python spotify_bot.py
```

## Usage Notes
- Artist URLs: Add Spotify artist URLs to the `artist_urls` list in the script. Example:
```bash
artist_urls = [
    "https://open.spotify.com/artist/20qISvAhX20dpIbOOzGK3q",  # Nas
    "https://open.spotify.com/artist/6Q192DXotxtaysaqNPy5yR",  # Amy Winehouse
]
```
- **Max Follows**: The script will follow up to 25 artists by default. Adjust the max_follows parameter in the follow_artists function if needed.

- **Error Logging**: If an error occurs while following an artist, the script logs it to the console.
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## Limitations
- This bot relies on Spotify's current web interface. 
- If the interface changes, the script may require updates.
- Use this script responsibly to avoid violating Spotify's terms of service. (pls don't sue me, I'm a student and this was for fun!)

**Always comply with Spotify's terms of service.**

## License
This project is licensed under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.