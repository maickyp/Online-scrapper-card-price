from openpyxl import Workbook
import string

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)

start_of_columns = 1


def list_to_excel(deck):

    wb = Workbook()
    sheet = wb.active
    i = start_of_columns
    j = 1

    print("Card Name" + ' · ' + "Card Set" + ' · ' + "Card Rarity" + ' · ' + "Market Price")
    deck.insert(0, ["Card Name", "Card Set", "Card Rarity", "Market Price"])

    for card in deck:
        for column in card:
            sheet[alphabet_list[i]+str(j)] = column
            i += 1
        j += 1
        i = start_of_columns

    wb.save("deck.xlsx")
