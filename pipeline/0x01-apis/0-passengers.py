#!/usr/bin/env python3
"""
Method to consum Starwars api and fetch some data
"""

import requests as rq


def availableShips(passengerCount):
    """
    Passengercount: int
    Return: available ships
    """
    url = "https://swapi-api.hbtn.io/api/starships"
    ships = rq.get(url).json()
    availale = []
    for i in range(100):
        try:
            if int(ships['results'][i]["cargo_capacity"]) >= passengerCount:
                availale.append(ships['results'][i]['name'])
        except IndexError:
            break
    return availale
