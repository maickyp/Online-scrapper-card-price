
# Online Card Scrapper

This project is an Online Card Price Scrapper where you can take as an input a deck list provided by a web [YGOProDeck] and will search through [TCGplayer] for every card, and gives a excel file with all finding.
This was for learning purposes about Python stuff, and wanted to make it challenging to my skills.


## Needed Libraries

Besides Python, you will need the following libs
- [Selenium]
- [Openpyxl]

## What is YGOProDeck

[YGoProDeck] is a web that people uploads decks for YuGiOh TCG so they can be played either physically, Master duel or other simulators. 

## What is TCGPlayer

[TCGplayer] is a web where you can sell/buy cards for several tcg games, including YuGiOh, Pokemon, or Magic The Gathering.
Within it has a search engine that allows you to search for specific card and shows you all existing rarities, if stock is available but the most important thing is the **Market Price** for each rarity, this number is an good guide to buy cards at your local game store a check if they are above or below de average price.


## How does it work?
When you search for a deck at [YGoProDeck], you can get your list in text as shown bellow

>  |- MONSTER CARDS :
   |- 1x Wandering Gryphon Rider
 |- SPELL CARDS (16 cards):
   |- 3x Rite of Aramesir
   |- 3x Virtual World Gate - Qinglong
 |- TRAP CARDS :
   |- 1x Infinite Impermanence
   |- 2x Virtual World Gate - Chuche
   |- 1x Virtual World Gate - Xuanwu
>
 >|- EXTRA DECK CARDS :
   |- 1x Ultimaya Tzolkin
   |- 1x Swordsoul Supreme Sovereign - Chengying
>
 >|- SIDE DECK CARDS :
   |- 2x Nibiru, the Primal Being

You shall save it in a *.txt file and use it as an input.

Python will process it and return it in a list that may look like this:

>['"Wandering Gryphon Rider", "Rite of Aramesir", "Virtual World Gate - Qinglong", "Infinite Impermanence", "Virtual World Gate - Chuche", "Virtual World Gate - Xuanwu", "Ultimaya Tzolkin", "Swordsoul Supreme Sovereign - Chengying", "Nibiru, the Primal Being"]

Then, the scrapper will open a Chrome Window, get to [TCGPlayer] page and search for the first card in the list.
Once the web return the data, it will filter, among all results, the cards that contain the card we searched for, This is just to avoid false positives for cards with common words like "Card" or "Number" 

The data we will retrieve from the web will be:

- **Card Name**
- **Card Set**
- **Card Rarity**
- **Market Price**

e.g.
- **Card Name:** Madolche Puddingcess Chocolat-a-la-Mode
- **Card Set:** Crossed Souls
- **Card Rarity:** Ultra Rare · #CROS-EN051
- **Market Price:** $5.51

If multiple copies/rarities of the card are available, either for higher/lower rarities or the same rarity in another set, the search engine of TCGPlayer differentiate them so it will be another entry in the list.

Following the example with **Madolche Puddingcess Chocolat-a-la-Mode**, it has, as per now, two copies in the same rarity but in different sets. You would receive both above and below entry

e.g.
- **Card Name:** Madolche Puddingcess Chocolat-a-la-Mode
- **Card Set:** Duel Overload
- **Card Rarity:** Ultra Rare · #DUOV-EN082
- **Market Price:** $2.14

Once all the info is crapped, this project returns a list with all this data, each card is an entry, and saves them in an excel file.

## Known Issues

 - Some cards will have duplicates in the final excel file given, or have some cards that may not be in the deck
   
   e.g.
   **Madolche Puddingcess** - **Madolche Puddingcess Chocolat-a-la-Mode**
   **Dark Magician - Dark Magician Girl** - **Toon Dark Magician (Girl)**
   **Red-Eyes Black Dragon** - **Red-Eyes Black Dragon Sword** 
   **All Number 39:  Utopia**

- It only shows the first page of the search card, if any 2nd or 3rd page, it will not be searched.

## Follow  up
Some features that I would be glad to integrate are the following:

- Support more pages to search other than TCGPlayer
- Support more pages to create decks
- Create a GUI for this
- Support other TCG's either in TCGPlayer or other webs.
- Avoid using *time* to wait until the page is fully loaded

## Contributing

Pull request are welcome. For major chances, please open an issue first to discuss what you would like to change.

Please make sure to update test as appropiate.


[Selenium]: https://www.selenium.dev
[Openpyxl]: https://openpyxl.readthedocs.io/en/stable/
[YGOProDeck]: https://ygoprodeck.com
[TCGPlayer]: https://www.tcgplayer.com