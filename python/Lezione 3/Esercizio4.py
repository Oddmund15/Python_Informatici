import math

# Raggio del cerchio
raggio = 8.7

# Calcolo dell'area usando i due metodi per la potenza
area1 = math.pi * raggio ** 2  
area2 = math.pi * pow(raggio, 2)  

# Calcolo del perimetro usando i due metodi per la potenza
perimetro1 = 2 * math.pi * raggio 
perimetro2 = 2 * math.pi * raggio  

# Stampa dei risultati
print("Area (usando **):", area1)
print("Area (usando pow:", area2)
print("Perimetro:", perimetro1)
