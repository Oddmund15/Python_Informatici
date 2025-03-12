print ("una funzione built-in")

print ("Inserisciil tuo nome ")
nome = input()
print ("Ciao", nome)

saldo = 1000

def preleva(importo):
    global saldo
    if importo > 500: