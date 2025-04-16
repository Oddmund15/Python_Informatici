combinazione = [3, 5, 7]
tentativi = 4

while tentativi > 0:
    a, b, c = input("Combinazione (tre numeri): ").split()
    a, b, c = int(a), int(b), int(c)
    
    if [a, b, c] == combinazione:
        print("Lucchetto aperto!")
        break
    
    tentativi -= 1
    print("Sbagliato!")

print("La combinazione era", combinazione)
