import json

from random import seed
from random import randint

seed(1)


print("wassup")
f = open("cards.txt", encoding = "utf8")
jsonfiles = f.read()
player1 = {
    "health": 30,
    "class":"",
    "deckcode": ""

}
deck1 = [ "Arcane Shot", "Arcane Shot", "Leper Gnome", "Leper Gnome", "Bloodfen Raptor","Bloodfen Raptor", "Dire Wolf Alpha", "Explosive Trap", "Freezing Trap", "Freezing Trap", "Hunter's Mark", "Hunter's Mark", "Scavenging Hyena", "Scavenging Hyena", "Snake Trap", "Animal Companion", "Animal Companion", "Eaglehorn Bow", "Eaglehorn Bow", "Jungle Panther", "Kill Command", "Kill Command", "Unleash the Hounds", "Unleash the Hounds", "Houndmaster", "Houndmaster", "Tundra Rhino", "Savannah Highmane", "Savannah Highmane", "King Krush"]
deck2 = deck1

player2 = {
    "health":30,
    "class":"",
    "deckcode":""
}
hand1 = [ "","","","","","","","","",""]
hand2 = hand1
def draw(decksize):
    
	value = randint(0, decksize -1)
    
	return (value)

def game(turn):
    if turn % 2 == 1:
        
    else:
def cardread(cardname):
    cardstring = '"name":"' + cardname + '"'
    
    location = jsonfiles.find(cardstring)
   
    if location == -1:
        
        print( "card not found")
    else:
        print("card found")
    counter = location
   
    while jsonfiles[counter] != "}":
        counter += 1 
    rlimit = counter
    couter = location
    
    while jsonfiles[counter] != "{":
        counter -= 1 
    llimit = counter

    
    return(jsonfiles[llimit:rlimit + 1])
print("hey")

game(1)






