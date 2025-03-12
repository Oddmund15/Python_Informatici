nomeUtente = "Dario Mennillo"
presentazione = "Ciao," + nomeUtente + "Questa è la calcolatrice più scema"
print (presentazione)

numero1 = 42.3
numero2 = 6.4
numero3 = 4 

#Calcolatrice le 4 operazioni matematiche di base
somma = numero1 + numero2
print("La somma vale: ", somma)

prod = numero1 * numero2
print("Il prodotto vale:", prod)

sottr = numero1 - numero2
print("La sottrazione vale:", sottr)

div = numero1 / numero2
print("Il quozioente vale:", div)

# elevamento a potenza
# eleva all potenza 2 entrambi i numeri

potenza1 = numero1 ** 3
potenza2 = numero2 ** 2
potenza3 = numero3 ** 2

print ("La potenza del primo numero vale:", potenza1)
print ("La potenza del secondo numero vale:", potenza2)

# Calcola la radice quadrata utilizzando le potenze
radice1 = numero1 ** (0.5)
radice2 = numero2 ** (1/2)
radice3 = numero3 ** (2)

print ("La Radice del primo numero vale:", radice1)
print ("La Radice del primo numero vale:", radice2)


potenza3 = pow (numero3, 2)
print("La potenza di", numero3, "alla seconda vale", potenza3)

#import delle librerie 
import math
radice3 = math.sqrt(numero3)
print("La radice di", numero3, "vale", radice3)
