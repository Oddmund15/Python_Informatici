#Instanziare una variabile "saldo" = 10000
#Chiedere all' utente quanto ha guadagnato questo mese (utilizza un valore con la virgola)
#se l'utente ha guadagnato piu di 1000 euro stampare: "Bravo , questo mese hai guadagnato bene "
#calcolare quanto ha effettivamente guadagnato (guadagno 1500, incasso (1500- 1000)= 500)

#Se l'utente ha guadagnato meno di 1000 euro stampare: ("mi dispiace, questo mese hai guadagnato cosi cosi ")
# calcolare il saldo su 1000 euro

#Se l'utente ha guadagnato 0 stampare: " Questo mese non hai guadagnato nulla"
# 
# Se l'utente è andato in perdita stampare: "Questo mese stai perdendo soldi". Calcolare il saldo 

# Inizializzazione del saldo
saldo = 10000.0  

# Chiedere all'utente quanto ha guadagnato
guadagno = float(input("Quanto hai guadagnato questo mese? (Usa il punto come separatore decimale): ")) #type casting 

# Controllo delle condizioni e calcolo del saldo aggiornato
if guadagno > 1000:
    print("Bravo, questo mese hai guadagnato bene!")
    incasso = guadagno 
    saldo += incasso
    print("Incasso aggiuntivo:", round(incasso, 2), "€")
elif 0 < guadagno < 1000:
    print("Mi dispiace, questo mese hai guadagnato così così.")
    saldo += guadagno
elif guadagno == 0:
    print("Questo mese non hai guadagnato nulla.")
else:
    print("Questo mese stai perdendo soldi.")
    saldo += guadagno # Se in perdita, il saldo diminuisce

# Stampare il saldo aggiornato
print("Saldo aggiornato:", round(saldo, 2), "€")



