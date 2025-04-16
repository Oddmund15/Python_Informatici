#Crea un programma che legge un numero inserito da un utente e stabilisce se questo numero è pari o dispari.
#Il programma si interrompe se l'utente inserisce il numero 0

#Programma combinazione numeri (lucchetto). All'utente viene richiesta una combinazione di 3 numeri.
#  L'utente ha 4 tentativi per indovinare la combinazione che apre il lucchetto. 
# Il programma si interrompe quando l'utente indovina i 3 numeri oppure quando esaurisce i tentativi disponibili

while True:
    n = int(input("Numero (0 per uscire): "))
    if n == 0: break
    print("pari" if n % 2 == 0 else "dispari")



