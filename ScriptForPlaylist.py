import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# # ==== CONFIG ====
CSV_FILE = "liked_songs.csv"
APPLE_MUSIC_URL = "https://music.apple.com/"
PLAYLIST_NAME = "Minha Primeira Play"  # Nome exato da playlist criada manualmente

# ==== CONFIGURA WEBDRIVER (Windows) ====
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service("chromedriver.exe")  # Caminho para o chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 15)

# driver.get(f"{APPLE_MUSIC_URL}search?term={search_term.replace(' ', '%20')}")

# ==== LER CSV ====
songs = pd.read_csv(CSV_FILE)

# ==== CONFIGURA WEBDRIVER (Windows) ====
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service("chromedriver.exe")  # Caminho para o chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# ==== ABRE APPLE MUSIC ====
driver.get(APPLE_MUSIC_URL)

print("\n➡ Faça login no Apple Music no navegador que abriu.")
input("Pressione ENTER aqui quando terminar o login...")

print("\n➡ Crie manualmente uma playlist vazia chamada exatamente:", PLAYLIST_NAME)
input("Pressione ENTER aqui quando terminar de criar a playlist...")




# ==== ADICIONAR MÚSICAS ====
for idx, row in songs.iterrows():
    search_term = f"{row['Track Name']} {row['Artist Name(s)']}"
    print(f"🔍 Pesquisando: {search_term}")

    # Abre a página de pesquisa diretamente
    driver.get(f"{APPLE_MUSIC_URL}search?term={search_term.replace(' ', '%20')}")
    time.sleep(5)  # Aguarda resultados carregarem

    try:
        # Botão de "Mais opções" (primeira música)
        more_btn = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Mais') or contains(@aria-label, 'More')]")
        more_btn.click()
        time.sleep(1)

        # Botão "Adicionar à Playlist"
        add_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Adicionar à Playlist') or contains(text(), 'Add to Playlist')]")
        add_btn.click()
        time.sleep(1)

        # Seleciona a playlist pelo nome
        playlist_btn = driver.find_element(By.XPATH, f"//button[contains(text(), '{PLAYLIST_NAME}')]")
        playlist_btn.click()
        time.sleep(2)

        print(f" Adicionada: {search_term}")

    except Exception as e:
        print(f" Não foi possível adicionar {search_term}: {e}")

print("\n Playlist finalizada!")
driver.quit()
