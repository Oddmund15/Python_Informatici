saldo = 10000
incasso = float(input("Quanto hai guadagnato questo mese ?"))

if incasso < -500:
    print("in questo mese sei in perdita")
elif incasso == 0 :
    print("Non hai guadagnato nulla")
elif incasso < 1000:
    print("Questo mese hai guadagnato così così")
else:
    print("Bravo questo mese hai guadagnato bene")

saldo =+ incasso 
print ("Saldo attuale", saldo)