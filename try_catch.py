while True:
    try:
        x = int(input("Entrez un nombre entier : "))
        break
    except ValueError:
        print("Oops ! Ce n'est pas un nombre entier. Essayez encore...")



# En py, on utilise try/except à la place de try/catch