#Or Logico. In questo caso vale una condizione Oppure l'altra affinchè quella globale sia true

#Esami : l'esame viene superato se passi lo scritto oppure l'orare

nome = input("Qual'è il tuo nome: ")
esameScritto = input("Hai passato l'esame scritto (si/no): ") == "si"
esameOrale = input("Hai passato l'esame orale (si/no): ") == "si"

# Caso con il professore "Bravo"
print("Professore Bravo")
if esameScritto or esameOrale:
    print("Complimenti, hai superato l'esame")
else:
    print("Mi spiace, non hai superato l'esame")

# Caso con il professore "Cattivo"
print("Professore Cattivo")
if esameScritto and esameOrale:
    print("Complimenti, hai superato l'esame")
else:
    print("Mi spiace, non hai superato l'esame perché uno dei due è andato male")
    if not esameScritto:
        print("Non hai passato l'esame scritto.")
    if not esameOrale:
        print("Non hai passato l'esame orale.")
