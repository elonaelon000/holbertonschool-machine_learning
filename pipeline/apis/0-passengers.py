#!/usr/bin/env python3
"""
Module for retrieving available starships from the SWAPI API.
"""

import requests


def availableShips(passengerCount):
    """
    Return a list of starship names that can hold passengerCount passengers.
    """
    ships = []
    url = "https://swapi-api.hbtn.io/api/starships/"

    while url:
        response = requests.get(url)
        data = response.json()

        for ship in data.get("results", []):
            passengers = ship.get("passengers", "")

            try:
                passengers = int(passengers.replace(",", ""))
            except (ValueError, AttributeError):
                continue

            if passengers >= passengerCount:
                ships.append(ship.get("name"))

        url = data.get("next")

    return ships
