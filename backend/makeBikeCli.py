#Importazione dei miei script 
import mainBike
import db
from analysis import analysis
from random import randint

#Dati db simulati
dataBike = [[1, 'Mountain Bike', 0.003], [2, 'Racing Bike', 0.007], [3, 'Electric Bike', 0.005], [4, 'City Bike', 0.002]]

dataTime = [[1, 1, 1, 30, 60], [5, 1, 2, 10, 20], [9, 1, 3, 20, 40], 
    [13, 1, 4, 10, 20], [17, 1, 5, 40, 80], [21, 1, 6, 15, 30], 
    [25, 1, 7, 15, 25], [29, 1, 8, 10, 20], [33, 1, 9, 10, 20],
    [37, 1, 10, 5, 10], [41, 1, 11, 10, 20], [45, 1, 12, 5, 15], 
    [49, 1, 13, 20, 40], [53, 1, 14, 15, 30], [2, 2, 1, 30, 50], 
    [6, 2, 2, 10, 15], [10, 2, 3, 20, 30], [14, 2, 4, 10, 15], [18, 2, 5, 30, 60],
    [22, 2, 6, 15, 25], [26, 2, 7, 15, 20], [30, 2, 8, 10, 15], [34, 2, 9, 10, 15], 
    [38, 2, 10, 5, 10], [42, 2, 11, 10, 15], [46, 2, 12, 5, 10], [50, 2, 13, 20, 30],
    [54, 2, 14, 15, 25], [3, 3, 1, 30, 50], [7, 3, 2, 5, 10], [11, 3, 3, 20, 30], 
    [15, 3, 4, 10, 15], [19, 3, 5, 40, 60], [23, 3, 6, 15, 25], [27, 3, 7, 15, 25], 
    [31, 3, 8, 10, 15], [35, 3, 9, 10, 15], [39, 3, 10, 10, 15], [43, 3, 11, 10, 15],
    [47, 3, 12, 10, 15], [51, 3, 13, 20, 30], [55, 3, 14, 15, 25], [4, 4, 1, 20, 40], 
    [8, 4, 2, 5, 10], [12, 4, 3, 15, 25], [16, 4, 4, 5, 10], [20, 4, 5, 30, 50], 
    [24, 4, 6, 10, 20], [28, 4, 7, 10, 20], [32, 4, 8, 5, 10], [36, 4, 9, 5, 10],
    [40, 4, 10, 5, 10], [44, 4, 11, 5, 10], [48, 4, 12, 5, 10], [52, 4, 13, 15, 25], [56, 4, 14, 10, 20]]

dataTask =[[1, 'Assemblaggio del telaio'], [2, 'Installazione della forcella'], 
    [3, 'Gruppo manubrio e cambio'], [4, 'Installazione della leva del freno'], 
    [5, 'Gruppo ruota [raggi e cerchio]'], [6, "Installazione di pneumatici e camere d'aria"], 
    [7, 'Installazione del deragliatore e della catena'], [8, 'Regolazione del cambio'], 
    [9, 'Calibrazione del sistema frenante'], [10, 'Installazione manubrio e manopole'], 
    [11, 'Installazione pedali e guarnitura'], [12, 'Installazione di sella e reggisella'], 
    [13, 'Controllo qualità e regolazioni'], [14, 'Imballaggio ed etichettatura']]

#Archivio produzione simulato
archiveProductionDB= [["ID_Batch", "Date_Time", "Working_Days","ID_Bike", "Time_Product", "Defect"]]

print("\nBenvenuto nell'interfaccia CLI per la produzione delle bici!")

#Variabile bandiera per l'utilizzo del db reale
useDB = False

while True:
    print("-----------\n")
    print("Vuoi utilizzare il programma con un db reale o con un db simulato?")
    #Scelta dell'utilizzo di un db reale o simulato
    selectDB = input("1 per DB reale\n2 per DB simulato\n3 per uscire: ")
    #Se reale richiama i dati dal db
    if selectDB == "1":
            try:
                database =db.DB()
                useDB = True
                query = "SELECT * FROM Bike_Type"
                dataBike = database.select(query)
                query = "SELECT * FROM Time_Task ORDER BY ID_Bike, ID_Task"
                dataTime = database.select(query)
                query = "SELECT * FROM Task_Cost"
                dataTask = database.select(query)
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
    print("\n-----------")
    print("Cosa vuoi fare?")
    #menu principale
    menu = """1 per produrre le bici
2 per vedere le tipologie di bici disponibili
3 per modificare le tipologie di bici che si possono produrre
4 per vedere le tempistiche dei task
5 per modificare le tempistiche dei task
6 per vedere lo storico delle bici prodotte
7 per vedere le analisi dei dati
8 per uscire: """
    selectMenu = input(menu)
    print("\n-----------")

    #Produzione bici
    if selectMenu =="1":
        # Scelta del numero di postazioni di lavoro o selezione randomica
        nStations = input("Quante postazioni di lavoro ha l'azienda (0 per valore random): ")
        if not nStations.isdecimal():
            print("Valore non valido!")
            continue
        elif nStations == "0":
            nStations = str(randint(1,20))
            print(f"N.Postazioni: {nStations}")

        # Scelta del numero di ore lavorative o selezione randomica
        hoursDay = input("Quante ore di lavoro fa al giorno l'azienda (0 per valore random): ")
        if not hoursDay.isdecimal():
            print("Valore non valido!")
            continue
        elif hoursDay == "0":
            hoursDay = str(randint(4,24))
            print(f"N.Ore giornaliere: {hoursDay}")
        
        # Scelta del numero di bici del tipo1 da produrre o selezione randomica
        nBike1 = input(f"Quante {str(dataBike[0][1])} vuoi produrre (0 per valore random): ")
        if not nBike1.isdecimal():
            print("Valore non valido!")
            continue
        elif nBike1 == "0":
            nBike1 = str(randint(1,50))
            print(f"N. {str(dataBike[0][1])}: {nBike1}")
        
        # Scelta del numero di bici del tipo2 da produrre o selezione randomica
        nBike2 = input(f"Quante {str(dataBike[1][1])} vuoi produrre (0 per valore random): ")
        if not nBike2.isdecimal():
            print("Valore non valido!")
            continue
        elif nBike2 == "0":
            nBike2 = str(randint(1,50))
            print(f"N. {str(dataBike[1][1])}: {nBike2}")
        
        # Scelta del numero di bici del tipo3 da produrre o selezione randomica
        nBike3 = input(f"Quante {str(dataBike[2][1])} vuoi produrre (0 per valore random): ")
        if not nBike3.isdecimal():
            print("Valore non valido!")
            continue
        elif nBike3 == "0":
            nBike3 = str(randint(1,50))
            print(f"N. {str(dataBike[2][1])}: {nBike3}")
        
        # Scelta del numero di bici del tipo4 da produrre o selezione randomica
        nBike4 = input(f"Quante {str(dataBike[3][1])} vuoi produrre (0 per valore random): ")
        if not nBike4.isdecimal():
            print("Valore non valido!")
            continue
        elif nBike4 == "0":
            nBike4 = str(randint(1,50))
            print(f"N. {str(dataBike[3][1])}: {nBike4}")
        
        batchBike = {1:int(nBike1),2:int(nBike2),3:int(nBike3),4:int(nBike4)}
        
        costructBatch = mainBike.ConstructionBike(int(nStations), int(hoursDay),batchBike,dataBike,dataTime)

        # Se hai scelto il db reale salva i dati nel database
        if useDB:
            try:
                costructBatch.insertDB(database)
            except:
                print("Errore nella connessione al Database")
                continue
        
        # Altrimenti salva i dati nel database simulato
        else:
            data = [[el[0],el[1], el[2],el[3],el[5],el[6]] for el in costructBatch.getListEndWork()]
            archiveProductionDB.extend(data)
        
        # Stampa output
        print("\n-----------")
        print(f"Tempo totale: {costructBatch.getTimeWork()}")
        print("-----------\n")

        #Intestazione per stampa produzione
        print("ID_Batch | Date_Time | Working_Days | ID_Bike | Type_Bike | Time_Product | Defect")
        print("-----------")
        for row in costructBatch.getListEndWork():
            print(row[0]+" | "+row[1]+" | "+row[2]+" | "+row[3]+" | "+row[4]+" | "+row[5]+"minutes  | "+row[6])
        
    #Stampa delle caratteristiche delle bici che si possono produrre
    elif selectMenu == "2":
        print("\nID_Bike | Type_Bike | Defect_Coefficient")
        print("-----------")
        for row in dataBike:
            print(f"{row[0]} | {row[1]} | {row[2]}")
    
    #Modifica bici da produrre
    elif selectMenu == "3":
        # Inserimento dell'id della bici da modificare e verifica input
        idBikeEdit = input("Inserisci ID bici da modificare (valore da 1 a 4): ")
        listId = ["1","2","3","4"]
        if idBikeEdit not in listId:
            print("Valore non valido!")
            continue
        idBikeEdit = int(idBikeEdit)
        
        # Inserimento nuova descrizione
        descBike = input("Inserisci Descrizione bici: ")

        # Inserimento nuovo coefficiente di difetto
        defectBike = input("Inserisci Coefficiente di Difettosità: ")
        try:
            defectBike = float(defectBike)
        except:
            print("Valore non valido!")
            continue
        
        # Se hai scelto il db reale aggiorna i dati nel database
        if useDB:
            query= "UPDATE Bike_Type SET Descri = %s, Defect_Coefficient= %s WHERE ID_Type = %s"
            dataQ = (descBike,defectBike,idBikeEdit)
            rowU =database.update(query, dataQ)

            # E legge i dati i aggiornati
            query = "SELECT * FROM Bike_Type"
            dataBike = database.select(query)
        
        # Altrimenti aggiorno il db simulato
        else:
            dataBike[idBikeEdit-1][1]= descBike
            dataBike[idBikeEdit-1][2]= defectBike
        
        #Stampa delle bici modificate
        print("\nID_Bike | Type_Bike | Defect_Coefficient")
        print("-----------")
        for row in dataBike:
            print(f"{row[0]} | {row[1]} | {row[2]}")
    
    #Stampa caratteristiche singoli task
    elif selectMenu == "4":
        print("ID_BiKe | Type_Bike | ID_Task | Type_Task | Min_Time | Max_Time")
        print("-----------")
        for row in dataTime:
            print(f"{row[1]} | {dataBike[row[1]-1][1]} | {row[2]} | {dataTask[row[2]-1][1]} | {row[3]} | {row[4]}")


    elif selectMenu == "8":
        print("Grazie per aver utilizzato il programma!")
        break
    else:
        print("Comando non valido!")

"""
list_endWordk =[['mPW5iRXm', '2025-04-04 16:23:57', '0', '1', 'Mountain Bike', '307', 'False'], ['mPW5iRXm', '2025-04-04 16:23:57', '0', '2', 'Racing Bike', '255', 'False'], ['mPW5iRXm', '2025-04-04 16:23:57', '0', '3', 'Electric Bike', '263', 'False'], ['mPW5iRXm', '2025-04-04 16:23:57', '0', '4', 'City Bike', '194', 'False']]
archiveDb =[['ID_Batch', 'Date_Time', 'Working_Days', 'ID_Bike', 'Time_Product', 'Defect'], ['mPW5iRXm', '2025-04-04 16:23:57', '0', '1', '307', 'False'], ['mPW5iRXm', '2025-04-04 16:23:57', '0', '2', '255', 'False'], ['mPW5iRXm', '2025-04-04 16:23:57', '0', '3', '263', 'False'], ['mPW5iRXm', '2025-04-04 16:23:57', '0', '4', '194', 'False']]
"""
        
