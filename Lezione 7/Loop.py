#Con i Loop ho la possibilità di ripetere deiblocchi di codice

#Loop indefiniti: sono dei loop che potrbbero ciclare all'infinito

#Sintassi : while condizioneTrue:
#          fai qualcosa


#fin tanto che la condizione è true continua ad eseguire il codice 

#Attenzione un loop del genere è loop infinito
#while true:
    #print("Ciao")



numStop = 10 

while numStop <10:
    numStop += 1
    print("Adesso il numero vale: ", numStop)

#ES

num_enorme = 999999999

numero = int(input("Inserisci un numero opppure digita -1 per fermare il loop"))

while numero != -1:
    if numero > num_enorme:
        num_enorme = numero

    numero = int(input("Inserisci un numero opppure digita -1 per fermare il loop"))

print("Il numero più grande è: ", num_enorme)