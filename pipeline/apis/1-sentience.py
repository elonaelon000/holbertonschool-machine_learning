#!/usr/bin/env python3
"""
Module for retrieving home planets of sentient species from the SWAPI API.
"""

import requests


def sentientPlanets():
    """
    Return the names of home planets of all sentient species.
    """
    planets = []
    url = "https://swapi-api.hbtn.io/api/species/"

    while url:
        response = requests.get(url)
        data = response.json()

        for species in data.get("results", []):
            classification = species.get("classification", "").lower()
            designation = species.get("designation", "").lower()

            if classification == "sentient" or designation == "sentient":
                homeworld = species.get("homeworld")

                if homeworld is None:
                    planets.append("unknown")
                else:
                    planet_response = requests.get(homeworld)
                    planet = planet_response.json()
                    planets.append(planet.get("name"))

        url = data.get("next")

    return planets
