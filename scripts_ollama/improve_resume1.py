# code avec appel explicite de l'API avec requests

import sys
from pathlib import Path

import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"

SYSTEM_PROMPT = (
    "Tu es un expert en rédaction de CV. Reformule la phrase fournie "
    "de manière professionnelle et concise, dans la même langue. "
    "N'invente aucune information. Réponds uniquement avec la phrase améliorée."
)


def improve(phrase: str, session: requests.Session) -> str:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},  # défini une seule fois plus haut
            {"role": "user", "content": phrase},           # seul élément qui change
        ],
        "stream": False,
        "options": {"temperature": 0.3},
    }
    r = session.post(OLLAMA_URL, json=payload, timeout=120)
    r.raise_for_status()
    return r.json()["message"]["content"].strip()


def main() -> None:
    file = Path(sys.argv[1] if len(sys.argv) > 1 else "./phrases.txt")

    with open(file) as f:
        phrases = f.readlines()

    with requests.Session() as session:  # réutilise la connexion HTTP entre les appels
        for phrase in phrases:
            print("Avant :", phrase)
            print("Après :", improve(phrase, session), "\n")


if __name__ == "__main__":
    main()
