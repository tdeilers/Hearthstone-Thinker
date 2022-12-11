import requests
from node import Node
from avl import AVL

Standard = {
    0:"Core",
    1:"Forged in the Barrens",
    2:"United in Stormwind",
    3:"Fractured in Alterac Valley",
    4:"Voyage to the Sunken City",
    5:"Murder at Castle Nathria",
    6:"March of the Lich King"
}

def searchByName(card): 

    url = f"https://omgvamp-hearthstone-v1.p.rapidapi.com/cards/{card}"

    querystring = {"collectible":"1"}

    headers = {
        "X-RapidAPI-Key": "0a3684b998mshc7e210e9d44a937p1f6df0jsn3c92be12a993",
        "X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response

def getSet(set):

    url = f"https://omgvamp-hearthstone-v1.p.rapidapi.com/cards/sets/{set}"

    querystring = {"collectible":"1"}

    headers = {
        "X-RapidAPI-Key": "0a3684b998mshc7e210e9d44a937p1f6df0jsn3c92be12a993",
        "X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response

def getStandard():

    cards = AVL()

    for key, val in Standard.items():
        response = getSet(val)

        for val in response:
            cards.add(val['dbfId'], val['name'], val['cost'])
            cards.addName(val['dbfId'], val['name'], val['cost'])
    return cards
