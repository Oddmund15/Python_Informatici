print("Benvenuto nella Banca")

print("Inserisci il tuo nome")
nome = input()
print("Caloroso", nome)

saldo = 1000

print("Desideri prelevare? (sì/no)")
risposta = input()

if risposta == 'sì':
    print("Quanto desideri prelevare?")
    importo = int(input()) 

    if importo > 500:
        print("Mi spiace, non puoi prelevare più di 500")
    elif importo > saldo:
        print("Mi spiace, non hai abbastanza soldi")
    else:
        saldo -= importo
        print("Il tuo saldo attuale è", saldo)
else:
    print("Quanto desideri depositare?")
    deposito = int(input())
    if deposito > 500:
        print("Mi spiace, non puoi depositare più di 600")
    elif deposito < 1:
        print("Non puoi depositare una cifra inferiore a 1.")
    else:
        saldo += deposito
        print("Il tuo saldo attuale è", saldo)