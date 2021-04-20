import csv  
archivo = open("appstore_games.csv","r")
csvreader = csv.reader(archivo, delimiter=",")
gratis_y_en_es = filter(lambda x: x[12] == "ES" and x[7] == "0", csvreader)
print("Estos son los juegos gratis en español: ")
for elem in gratis_y_en_es:
    print(elem[2])

