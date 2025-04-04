#Importazione dei miei script 
import mainBike
import db
from analysis import analysis
from random import randint

#Dati db simulati
dataBike = [(1, 'Mountain Bike', 0.003), (2, 'Racing Bike', 0.007), (3, 'Electric Bike', 0.005), (4, 'City Bike', 0.002)]
dataTime = [(1, 1, 1, 30, 60), (5, 1, 2, 10, 20), (9, 1, 3, 20, 40), 
    (13, 1, 4, 10, 20), (17, 1, 5, 40, 80), (21, 1, 6, 15, 30), 
    (25, 1, 7, 15, 25), (29, 1, 8, 10, 20), (33, 1, 9, 10, 20),
    (37, 1, 10, 5, 10), (41, 1, 11, 10, 20), (45, 1, 12, 5, 15), 
    (49, 1, 13, 20, 40), (53, 1, 14, 15, 30), (2, 2, 1, 30, 50), 
    (6, 2, 2, 10, 15), (10, 2, 3, 20, 30), (14, 2, 4, 10, 15), (18, 2, 5, 30, 60),
    (22, 2, 6, 15, 25), (26, 2, 7, 15, 20), (30, 2, 8, 10, 15), (34, 2, 9, 10, 15), 
    (38, 2, 10, 5, 10), (42, 2, 11, 10, 15), (46, 2, 12, 5, 10), (50, 2, 13, 20, 30),
    (54, 2, 14, 15, 25), (3, 3, 1, 30, 50), (7, 3, 2, 5, 10), (11, 3, 3, 20, 30), 
    (15, 3, 4, 10, 15), (19, 3, 5, 40, 60), (23, 3, 6, 15, 25), (27, 3, 7, 15, 25), 
    (31, 3, 8, 10, 15), (35, 3, 9, 10, 15), (39, 3, 10, 10, 15), (43, 3, 11, 10, 15),
    (47, 3, 12, 10, 15), (51, 3, 13, 20, 30), (55, 3, 14, 15, 25), (4, 4, 1, 20, 40), 
    (8, 4, 2, 5, 10), (12, 4, 3, 15, 25), (16, 4, 4, 5, 10), (20, 4, 5, 30, 50), 
    (24, 4, 6, 10, 20), (28, 4, 7, 10, 20), (32, 4, 8, 5, 10), (36, 4, 9, 5, 10),
    (40, 4, 10, 5, 10), (44, 4, 11, 5, 10), (48, 4, 12, 5, 10), (52, 4, 13, 15, 25), (56, 4, 14, 10, 20)]

#Archivio produzione simulato
archiveDB= ""

print("\nBenvenuto nell'interfaccia CLI per la produzione delle bici!")

#Variabile bandiera per l'utilizzo del db reale
useDB = False

while True:
    print("-----------")
    print("Vuoi utilizzare il programma con un db reale o con un db simulato?")
    #Scelta dell'utilizzo di un db reale o simulato
    selectDB = input("1 per DB reale\n2 per DB simulato\n3 per uscire: ")
    print("-----------")
    #Se reale richiama i dati dal db
    if selectDB == "1":
            try:
                database =db.DB()
                useDB = True
                query = "SELECT * FROM Bike_Type"
                dataBike = database.select(query)
                query = "SELECT * FROM Time_Task ORDER BY ID_Bike, ID_Task"
                dataTime = database.select(query)
                break
            except:
                print("Errore di Connessione!")
    
    elif selectDB =="2":
        break

    elif selectDB =="3":
        print("Grazie per aver utilizzato il programma!")
        quit()
    
    else:
        print("Comando non valido!")

while True:
    print("-----------")
    print("Cosa vuoi fare?")
    #menu principale
    menu = """1 per produrre le bici
2 per vedere i tipi di bici disponibili
3 per modificare i tipi di bici che si possono produrre
4 per vedere le tempistiche dei task
5 per modificare le tempistiche dei task
6 per vedere lo storico delle bici prodotte
7 per uscire: """
    selectMenu = input(menu)
    print("-----------")

    #Produzione bici
    if selectMenu =="1":
        # scelta del numero di postazioni di lavoro o selezione randomica
        nStations = input("Quante postazioni di lavoro ha l'azienda (0 per valore random): ")
        if not nStations.isdecimal():
            print("Valore non valido!")
            continue
        elif nStations == "0":
            nStations = str(randint(1,20))

        # scelta del numero di ore lavorative o selezione randomica
        hoursDay = input("Quante ore di lavoro fa al giorno l'azienda (0 per valore random): ")
        if not hoursDay.isdecimal():
            print("Valore non valido!")
            continue
        elif hoursDay == "0":
            hoursDay = str(randint(4,24))
        
        # scelta del numero di bici del tipo1 da produrre o selezione randomica
        nBike1 = input(f"Quante {str(dataBike[0][1])} vuoi produrre (0 per valore random): ")
        if not nBike1.isdecimal():
            print("Valore non valido!")
            continue
        elif hoursDay == "0":
            hoursDay = str(randint(4,24))
        


        #Se hai scelto il db reale recupera dati
        if useDB:
            query = "SELECT * FROM Bike_Type"
            dataBike = database.select(query)
            query = "SELECT * FROM Time_Task ORDER BY ID_Bike, ID_Task"
            dataTime = database.select(query)
        costructBatch = mainBike.ConstructionBike(nStations, hoursDay,batchBike,dataBike,dataTime)

    elif selectMenu == "7":
        print("Grazie per aver utilizzato il programma!")
        break
    else:
        print("Comando non valido!")
        
