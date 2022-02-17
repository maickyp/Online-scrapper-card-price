
import searchEngine
import deckTxtToList
import saveToExcel

path = "Resources/utopia.txt"  # Deck_list in a txt file

deck = deckTxtToList.deck_txt_to_list(path)   # Process the file to a list

deck_scrapped = searchEngine.tcg_player(deck)  # Scrap the cards

saveToExcel.list_to_excel(deck_scrapped)  # Excel


