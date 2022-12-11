from hearthstone.deckstrings import Deck
from hearthstone.enums import FormatType

# Create a deck from a deckstring
deck = Deck()
deck.heroes = [7]  # Garrosh Hellscream
deck.format = FormatType.FT_WILD

# Nonsense cards, but the deckstring doesn't validate.

deck.cards = [(1, 3), (2, 3), (3, 3), (4, 3)]  # id, count pairs
print(deck.as_deckstring)  # "AAEBAQcAAAQBAwIDAwMEAw=="

# Import a deck from a deckstring
deck = Deck.from_deckstring("AAECAZvDAwyh+QPtgAT7igTspwTYtgTbuQTd2gTg2gT23QSX7wT58QSLpAUOqusD/u4DvYAE9p8E958EuqQE+6UE+awE3NoE3toE9N0E9d0Ew+ME9+0EAA==")
# deck = Deck.from_deckstring("AAECAaIHCqH5A+2ABPuKBNi2BNu5BOnQBLjZBJfvBL/wBIukBQ+q6wP+7gOh9AO9gAT2nwT3nwS6pAT7pQTspwT5rAS3swTVtgT03QT13QT58QQA")
print(deck.cards)



# assert deck.heroes == [7]
# assert deck.format == FormatType.FT_WILD
# assert deck.cards == [(1, 3), (2, 3), (3, 3), (4, 3)]