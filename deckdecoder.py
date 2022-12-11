from hearthstone.deckstrings import Deck
from hearthstone.enums import FormatType
from hsapi import *
from topSort import DirectedGraph, toposort
from classes import classes

cards = getStandard()
prompt = input("decode or encode: ")

while prompt != "close":
    if prompt == "decode": 
        deckCode = ''

        deckCode = input("Enter a deck list code: ")
        try:
            deck = Deck.from_deckstring(deckCode)
            deckIds = deck.get_dbf_id_list()
            hero = deck.heroes[0]

            outputDeck = []

            for i in range(len(deckIds)):
                card = cards.getCard(deckIds[i][0])
                card.amount = deckIds[i][1]
                outputDeck.append(card)
            for card in outputDeck:
                for next in outputDeck:
                    if card.cost < next.cost:
                        card.addEdgeTo(next)
                    
            graph = DirectedGraph(outputDeck)
            graph.updateAll()
            toposort(graph)

        except(ValueError):
            print("Invalid decklist")

    elif prompt == 'encode': 
        temp = input("Enter a class: ")
        hero = [heroes for heroes in classes if classes[heroes]==temp]
        decklist = []
        print("Enter decklist: ")

        line = input()
        while line != 'close':
            decklist.append(line)
            line = input()
        dbfIdList = []
        try:
            for card in decklist:
                amount = card[:card.index('x')]
                cost = card[card.index('(')+1:card.index(')')]
                name = card[card.index(')')+2:]

                response = cards.getCardName(name)
                id = response.value

                tup = (id, int(amount))
                dbfIdList.append(tup)

            deck = Deck()
            deck.cards = dbfIdList
            deck.heroes = hero
            deck.format = FormatType.FT_STANDARD
            print(deck.as_deckstring)

        except(ValueError):
            print("Invalid decklist")

    prompt = input("decode or encode: ")

### Reno my beloved <3
# Class: Rogue
# Format: Standard
# Year of the Hydra
#
# 1x (0) Preparation
# 1x (0) Shadowstep
# 1x (1) Blackwater Cutlass
# 1x (1) Door of Shadows
# 1x (1) Gone Fishin'
# 1x (1) SI:7 Extortion
# 1x (2) Double Cross
# 1x (2) Jackpot!
# 1x (2) Kidnap
# 1x (2) Maestra of the Masquerade
# 1x (2) Murder Accusation
# 1x (2) Perjury
# 1x (2) Reconnaissance
# 1x (2) Serrated Bone Spike
# 1x (2) Sinstone Graveyard 
# 1x (2) Sketchy Stranger
# 1x (2) Sticky Situation
# 1x (2) Tooth of Nefarian
# 1x (2) Vanessa VanCleef
# 1x (2) Wicked Stab (Rank 1)
# 1x (3) Ghastly Gravedigger
# 1x (3) Murloc Holmes
# 1x (3) Prince Renathal
# 1x (3) Shroud of Concealment
# 1x (4) Edwin, Defias Kingpin
# 1x (4) Halkias
# 1x (4) Private Eye
# 1x (4) Scabbs Cutterbutter
# 1x (4) Swiftscale Trickster
# 1x (5) Contraband Stash
# 1x (5) Queen Azshara
# 1x (5) Theotar, the Mad Duke
# 1x (5) Wildpaw Gnoll
# 1x (6) Crabatoa
# 1x (6) Reno Jackson
# 1x (7) Mutanus the Devourer
# 1x (7) Tess Greymane
# 1x (8) Shadowcrafter Scabbs
# 1x (9) The Sunwell
# 1x (10) Sire Denathrius
# 
# AAECAY7ABCiX5wOq6wP+7gOm7wOd8AOh9AOh+QO9gATtgAT7igT2nwT3nwS6pAT7pQTspwT5rAS3swTVtgTYtgTbuQTp0ASa1AS42QTc2gTd2gTe2gTf2gTg2gT03QT13QSS3wTD4wT37QT47QSX7wS/8AT58QTBgwXUoQWLpAUAAA==
# 
# To use this deck, copy it to your clipboard and create a new deck in Hearthstone