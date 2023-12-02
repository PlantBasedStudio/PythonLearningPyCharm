
#Écrire dans un fichier
file = open("hello.txt", "w")
file.write("Hello, I have wrote this by python code.")
file.close()



#lire le fichier ligne par ligne
with open("hello.txt") as file:
    for lign in file:
        print(lign)




