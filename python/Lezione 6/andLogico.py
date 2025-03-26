# L' AND logico(&&) mi permette di unire più condizioni. Vuol dire che ho bisogno che entrambe
#  le consizioni siamo valide affinchè tutta la condizione sia true 

nome = input("Come ti chiami: ")
eta = int(input("Quanti anni hai?: "))
invito = input("Hai ricevuto un invito? (sì/no): ").lower() == 'sì'

if eta >= 18 and invito:
    print(f"Ciao {nome}, puoi far parte del club dei programmatori")
elif eta < 18 and invito:
    print(f"Caro {nome}, non hai ancora compiuto 18 anni. Anche se hai l'invito non puoi entrare")
elif eta >= 18 and not invito:
    print(f"Caro {nome}, non hai l'invito per entrare nel club")
else:
    print(f"Mi spiace {nome}, non puoi fare parte del club. Non hai 18 anni e non hai neppure un invito")
