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
    availale = []
    while True:
        ships = rq.get(url).json()
        for v in ships['results']:
            try:
                capacity = int(v['passengers'].replace(",", ""))
                if capacity >= passengerCount:
                    availale.append(v['name'])
            except ValueError:
                continue
        url = rq.get(url).json()['next']
        if url is None:
            break
    return availale
