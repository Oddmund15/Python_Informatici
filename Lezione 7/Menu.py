uscita = ''

while uscita != 'q':
    print("-----Menu-----")
    print("a) Gioca")
    print("b) Calcola")
    print("c) Saluta")
    print("q) Esci")
    print("--------------")

    scelta = input("Scegli una voce del menu: ").lower()  # Converte in minuscolo per evitare errori

    if scelta == 'a':
        print("Hai scelto di giocare!")
    elif scelta == 'b':
        print("Hai scelto di calcolare qualcosa!")
    elif scelta == 'c':
        print("Hai scelto di salutare qualcuno!")
    elif scelta == 'q':
        print("Ciao, sei uscito dal programma!")
        break  # Uscita immediata dal ciclo
    else:
        print("Scelta non valida, riprova!")
