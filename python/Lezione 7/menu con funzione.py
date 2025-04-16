import random

def gioca():
    numero = random.randint(1, 10)
    tentativo = -1
    print("\nHo scelto un numero tra 1 e 10. Indovinalo!")
    
    while tentativo != numero:
        try:
            tentativo = int(input("Inserisci un numero: "))
            if tentativo < numero:
                print("Troppo basso! Riprova.")
            elif tentativo > numero:
                print("Troppo alto! Riprova.")
            else:
                print("Bravo! Hai indovinato!\n")
        except ValueError:
            print("Errore! Devi inserire un numero.")

def calcola():
    try:
        num1 = float(input("\nInserisci il primo numero: "))
        operatore = input("Scegli un'operazione (+, -, *, /): ")
        num2 = float(input("Inserisci il secondo numero: "))

        if operatore == '+':
            risultato = num1 + num2
        elif operatore == '-':
            risultato = num1 - num2
        elif operatore == '*':
            risultato = num1 * num2
        elif operatore == '/':
            if num2 == 0:
                print("Errore: Divisione per zero!")
                return
            risultato = num1 / num2
        else:
            print("Operatore non valido!")
            return

        print(f"Risultato: {risultato}\n")
    except ValueError:
        print("Errore! Devi inserire numeri validi.")

def saluta():
    nome = input("\nCome ti chiami? ")
    print(f"Ciao {nome}, spero tu stia bene!\n")

uscita = ''

while uscita != 'q':
    print("----- Menu -----")
    print("a) Gioca")
    print("b) Calcola")
    print("c) Saluta")
    print("q) Esci")
    print("----------------")

    scelta = input("Scegli una voce del menu: ").lower()

    if scelta == 'a':
        gioca()
    elif scelta == 'b':
        calcola()
    elif scelta == 'c':
        saluta()
    elif scelta == 'q':
        print("Ciao! Alla prossima!")
        break
    else:
        print("Scelta non valida! Riprova.\n")
