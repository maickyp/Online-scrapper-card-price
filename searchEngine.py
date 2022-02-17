from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time


def tcg_player(deck):
    ser = Service("C:\Program Files (x86)\chromedriver.exe")
    driver = webdriver.Chrome(service=ser)
    driver.get("https://www.tcgplayer.com")
    print(driver.title)
    search = driver.find_element(By.ID, 'autocomplete-input')
    return_deck = []

    for card in deck:
        search.send_keys("Yugioh " + card)
        search.send_keys(Keys.RETURN)
        time.sleep(2)
        elements = driver.find_elements(By.CLASS_NAME, "search-result")

        for element in elements:

            card_name = element.find_element(By.CLASS_NAME, "search-result__title").text
            card_set = element.find_element(By.CLASS_NAME, "search-result__subtitle").text

            try:
                card_rarity = element.find_element(By.CSS_SELECTOR, "section.search-result__rarity").text

            except NoSuchElementException:
                card_rarity = "Rarity not Available"

            try:
                card_price = element.find_element(By.CLASS_NAME, "search-result__market-price--value").text

            except NoSuchElementException:
                card_price = "Price not Available"

            if card in card_name:
                card_info = [card_name, card_set, card_rarity, card_price]
                print(card_info)
                return_deck.append(card_info)

        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(Keys.DELETE)

    driver.quit()

    return return_deck
