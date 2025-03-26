#If statemnt sever ad operare delle scelte in base a delle condizioni 
#Sintassi
#if condizione:
#    esegui se condizione è true

x = 10 
y = 10 
if x == y :
    print("I due numeri sono uguali ")
else:
    print("I due numeri sono diversi")

    ## Leggi i due numeri inseriti dall utente

num1 =int(input("Inserisci il primo numero:")) 
num2 =int(input("Inserisci il secondo numero:")) 

if num1 > num2:
    print("Il primo numero inserito è piu grande")
elif num1 < num2:
    print("Il secondo numero inserito è piu grande")
elif num1 == num2:
    print("I due numeri sono uguali")

else:print("I Due numeri sono uguali")