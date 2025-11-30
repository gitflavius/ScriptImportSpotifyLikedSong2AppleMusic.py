import time
import argparse
import os
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# # ==== CONFIG ====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, 'liked_songs.csv')   # Caminho para o arquivo CSV exportado do Spotify
APPLE_MUSIC_URL = "https://music.apple.com/"
PLAYLIST_NAME = "Minha Primeira Play"  # Nome exato da playlist criada manualmente


def init_driver(chromedriver_path: str = "chromedriver.exe", start_maximized: bool = True):
    chrome_options = Options()
    if start_maximized:
        chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 15)
    return driver, wait

def query_shadow(driver, root, selector):
    return driver.execute_script(
        "return arguments[0].querySelector(arguments[1])",
        root, selector
    )

def expand_shadow(driver, element):
    return driver.execute_script("return arguments[0].shadowRoot", element)


def add_song_to_playlist(driver, search_term: str, playlist_name: str):
    from time import sleep
    driver.get(f"https://music.apple.com/search?term={search_term.replace(' ', '+')}")
    sleep(4)

    try:
        # === 1. Seção SONGS ===
        songs_section = driver.find_element(By.XPATH, "//div[contains(@aria-label,'Songs')]")

        # Primeiro item
        first_song = songs_section.find_element(By.CSS_SELECTOR, "li")
        driver.execute_script("arguments[0].scrollIntoView(true);", first_song)
        sleep(1)

        # === 2. Navegar até o botão "more" no SHADOW DOM ===
        # botão more é um elemento shadow-root dentro do item
        more_btn_host = first_song.find_element(By.CSS_SELECTOR, "music-button[data-testid='more-button']")

        shadow1 = expand_shadow(driver, more_btn_host)
        more_btn = query_shadow(driver, shadow1, "button")

        more_btn.click()
        sleep(1)

        # === 3. Menu → Add to playlist ===
        add_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Add to Playlist')]")
        add_btn.click()
        sleep(1)

        # === 4. Escolher a playlist ===
        playlist_btn = driver.find_element(By.XPATH, f"//button[contains(text(), '{playlist_name}')]")
        playlist_btn.click()

        print(f"🎵 Sucesso: {search_term}")
        return True

    except Exception as e:
        print("❌ ERRO:", e)
        return False


def main(dry_run: bool = False, limit: int | None = None, chromedriver_path: str = "chromedriver.exe"):
    songs = pd.read_csv(CSV_FILE)

    driver, wait = init_driver(chromedriver_path)

    # ==== ABRE APPLE MUSIC ====
    driver.get(APPLE_MUSIC_URL)

    print("\n➡ Faça login no Apple Music no navegador que abriu.")
    input("Pressione ENTER aqui quando terminar o login...")

    print("\n➡ Crie manualmente uma playlist vazia chamada exatamente:", PLAYLIST_NAME)
    input("Pressione ENTER aqui quando terminar de criar a playlist...")

    count = 0
    for idx, row in songs.iterrows():
        if limit is not None and count >= limit:
            break
        search_term = f"{row['Track Name']} {row['Artist Name(s)']}"
        add_song_to_playlist(driver, wait, search_term, PLAYLIST_NAME, dry_run=dry_run)
        count += 1

    print("\n Playlist finalizada!")
    driver.quit()


def debug_print_list(limit: int | None = 10):
    songs = pd.read_csv(CSV_FILE)
    for idx, row in songs.head(limit).iterrows():
        search_term = f"{row['Track Name']} {row['Artist Name(s)']}"
        print(f"{idx+1}. {search_term}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Import liked Spotify songs to Apple Music (manual playlist creation required).')
    parser.add_argument('--dry-run', action='store_true', help='Do not click; just open search URLs and print them.')
    parser.add_argument('--limit', type=int, default=None, help='Process only the first N songs (useful for testing).')
    parser.add_argument('--debug-list', action='store_true', help='Print the first 10 songs from the CSV and exit (quick check).')
    args = parser.parse_args()

    if args.debug_list:
        debug_print_list(limit=args.limit or 10)
    else:
        main(dry_run=args.dry_run, limit=args.limit)
