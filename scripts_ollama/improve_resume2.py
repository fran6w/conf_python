# code avec appel implicite de l'API avec ollama

import sys
from pathlib import Path

import ollama

MODEL = "llama3.2"  # tout modèle génératif installé (qwen3, mistral, gemma3...)

SYSTEM_PROMPT = (
    "Tu es un expert en rédaction de CV. Reformule la phrase fournie "
    "de manière professionnelle et concise, dans la même langue. "
    "N'invente aucune information. Réponds uniquement avec la phrase améliorée."
)


def main() -> None:
    file = Path(sys.argv[1] if len(sys.argv) > 1 else "./phrases.txt")

    with open(file) as f:
        phrases = f.readlines()

    for phrase in phrases:
        response = ollama.chat(
            model=MODEL,
            messages=[
            {"role": "system", "content": SYSTEM_PROMPT},  # défini une seule fois plus haut
            {"role": "user", "content": phrase},           # seul élément qui change
            ],
            options={"temperature": 0.3},  # faible : reformulation plus stable
        )
        print("Avant :", phrase)
        print("Après :", response["message"]["content"], "\n")


if __name__ == "__main__":
    main()
