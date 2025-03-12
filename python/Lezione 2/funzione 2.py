#Funzioni Built-in
print("Anche print è una funzione built-in")

print("Inserisci il tuo nome")
nome = input() #input() è una funzione built che mi 
# permette di ricevere in input un valore e registralo in una variabile
print("Ciao", nome)

saldo = 1000

print ("Qaunto desideri prelevare?")
importo =int(input()) # sto forzando l'input ad essere un intero : CAST del dato

if importo > 500:
    print("Mi spiace, non puoi prelevare più di 500")
else:
    if importo > saldo:
        print("Mi spiace, non hai abbasta")
    else:
        saldo -= importo

        print("Il tuo saldo attuale è", saldo)

