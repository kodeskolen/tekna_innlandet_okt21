"""
Program som skriver ut dagens tema, 
ved hjelp av en liste og en for-løkke.
Vi bruker input() her så programmet skal
stå og vente etter hvert punkt. Da kan
bruker trykke enter i konsollen for å gå videre.
"""

print()
print("Velkommen tilbake!")
input()

dagens_tema = ["Repetisjon", "Lister", "Mer om løkker",
               "Tekstbehandling", "Hvis tid: Plotting"]

print("I dag skal vi dekke:")
input()
for tema in dagens_tema:
    print(f"- {tema}")
    input()
    
    