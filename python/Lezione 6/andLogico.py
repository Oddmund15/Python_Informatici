# L' AND logico(&&) mi permette di unire più condizioni. Vuol dire che ho bisogno che entrambe
#  le consizioni siamo valide affinchè tutta la condizione sia true 

input("Come ti chiami")
eta = int(input("Quanti anni hai?"))
invito = bool(input("Hai ricevuto un invito ?"))

if eta >= 18 and invito:
    print("Ciao Stefan, puoi far parte del club dei programmatori")
elif eta < 18 and invito:
    print("Caro Stefan, non hai ancora compiuto 18 anni. Anche se hai l'invito non puoi entrare")
elif eta >= 18 and not invito:
    print("Caro Stefan, non hai ancora compiuto 18 anni e non hai l'invito per entrare")
else:
    print("Mi spiace, non puoi fare parte del club. Non hai 18 anni e non hai neppure un invito" )
