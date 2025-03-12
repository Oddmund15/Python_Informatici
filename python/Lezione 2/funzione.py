#Funzioni Built-in
print("Anche print è una funzione built-in")

print("Inserisci il tuo nome")
nome = input() #input() è una funzione built che mi 
# permette di ricevere in input un valore e registralo in una variabile
print("Ciao", nome)

saldo = 1000

print ("Qaunto desideri prelevare?")
prelievo =int(input()) # sto forzando l'input ad essere un intero : CAST del dato
saldo -= prelievo

print("Il tuo saldo attuale è", saldo)

