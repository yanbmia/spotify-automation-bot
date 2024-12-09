from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random
import datetime

# Set ChromeDriver path
CHROME_DRIVER_PATH = "path_to_your_chromedriver"
SPOTIFY_LOGIN_URL = "https://accounts.spotify.com/en/login"
SPOTIFY_TARGET_URL = "https://open.spotify.com"

# Spotify account credentials
SPOTIFY_EMAIL = "your_email"
SPOTIFY_PASSWORD = "your_password"

# Function to log into Spotify
def spotify_login(driver):
    driver.get(SPOTIFY_LOGIN_URL)
    time.sleep(5)
    
    # Enter email and password
    email_input = driver.find_element(By.ID, "login-username")
    password_input = driver.find_element(By.ID, "login-password")
    login_button = driver.find_element(By.ID, "login-button")

    email_input.send_keys(SPOTIFY_EMAIL)
    password_input.send_keys(SPOTIFY_PASSWORD)
    login_button.click()

    time.sleep(5)  # Wait for the page to load

# Function to automate following artists
def follow_artists(driver, artist_urls, max_follows=25):
    followed_count = 0
    for artist_url in artist_urls:
        if followed_count >= max_follows:
            break

        driver.get(artist_url)
        time.sleep(random.uniform(2, 4))  # Random wait to mimic human behavior

        try:
            # Look for the Follow button
            follow_button = driver.find_element(By.XPATH, "//button[contains(text(),'Follow')]")
            if follow_button:
                follow_button.click()
                followed_count += 1
                print(f"Followed artist at {artist_url}")
                time.sleep(random.uniform(1, 3))  # Random wait
        except Exception as e:
            print(f"Error following artist at {artist_url}: {e}")

    print(f"Total artists followed: {followed_count}")
    return followed_count

# Main function
def main():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        spotify_login(driver)

        # Example list of artist URLs
        artist_urls = [
            "https://open.spotify.com/artist/1dfeR4HaWDbWqFHLkxsg1d",  # Queen
            "https://open.spotify.com/artist/3fMbdgg4jU18AjLCKBhRSm",  # Michael Jackson
            # Add more artist URLs as needed
        ]

        total_follows = follow_artists(driver, artist_urls)
        print(f"Automation complete. Total followed: {total_follows}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
