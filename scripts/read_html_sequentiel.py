# coding: utf-8

import time
from io import StringIO

import pandas as pd
import requests


def f(url):
    email = "prenom.nom@gmail.com"  # A COMPLETER
    headers = {"User-Agent": f"Mozilla/5.0 (cours data science; {email})"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    tables = pd.read_html(StringIO(response.text))
    print([df.shape for df in tables])


def run():
    url1 = "https://fr.wikipedia.org/wiki/Produit_int%C3%A9rieur_brut_par_habitant"
    url2 = "https://fr.wikipedia.org/wiki/Jeux_olympiques"
    url3 = "https://fr.wikipedia.org/wiki/Langues_les_plus_parl%C3%A9es"

    urls = [url1, url2, url3]

    # CODE A COMPLETER
    list(map(f, urls))

if __name__ == "__main__":
    start = time.perf_counter()
    run()
    print(f"Durée : {time.perf_counter() - start:.2f} s")
