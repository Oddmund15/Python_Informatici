
def calcola_media(voti):

    somma_voti = sum(voti)
    
    numero_voti = len(voti)
    
    media = somma_voti / numero_voti
    return media

voti = [100, 80 ,70, 85, 57, 95, 80, 65, 80, 65, 100, 90]  

media = calcola_media(voti)
print("La media dei voti è:", round(media))


