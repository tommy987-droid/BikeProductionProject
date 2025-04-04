#Importazione librerie: random per la randomizzazione dei dati, 
#datetime per la gestione delle date e string per la creazione di codici univoci di Produzione
from random import randint, choice, choices
from datetime import datetime
import string


#Classe delle singole biciclette
class Bike:
    def __init__(self, type,dataBike, dataTime):
        #Tipo di bicicletta
        self._type = type
        #Descrizione del tipo di bicicletta
        self._descType = dataBike[type-1][1]
        #Tempi di esecuzione per singolo task
        self._timeTask = {}
        #Richiamo del metodo per aggiornare il tempo di esecuzione
        self.setTimeTask(dataTime)
        #Coefficiente di difettosità
        self._defectCoef = 0
        #Richiamo del metodo per aggiornare il coefficiente di difettosità
        self.setDefectCoef(dataBike)

    #Metodo che, dato l'elenco dei task per tutte le bici, assegna quelli specifici per il tipo
    def setTimeTask(self, dataTime):
        for row in dataTime:
            if self._type == row[1]:
                self._timeTask["T"+str(row[2])] = {"min":int(row[3]),"max":int(row[4])}

    #Metodo che, dato l'elenco dei coefficienti di difettosità per tutte le bici, assegna quelli specifici per il tipo
    def setDefectCoef(self, dataBike):
        self._defectCoef = float(dataBike[self._type-1][2])

    #Metodo per visualizzare la descrizione della bici
    def getDescType(self):
        return self._descType
    
    #Metodo per visualizzare il tipo della bici
    def getType(self):
        return self._type
    
    #Metodo per visualizzare i tempi dei task
    def getTimeTask(self):
        return self._timeTask
    
    #Metodo per visualizzare il coefficente di difettosità
    def getDefectCoef(self):
        return self._defectCoef
        
    #Metodo per visualizzare le informazioni sulla bici
    def __str__(self):
        return f"Bicycle type: {self._descType}, Time Task: {self._timeTask}, defect coefficient: {self._defectCoef}"

#Classe che si occupa della produzione delle bici
class ConstructionBike:
    def __init__(self, nStations, hoursDay, bikeBatch, dataBike,dataTime):
        #creazione dell'id di lotto di produzione in maniera casuale
        self._idBatch = ''.join(choices(string.ascii_letters + string.digits, k=8))
        #Numero di postazioni di lavorazione
        self._nStations = nStations
        #Attributo che, passate le ore di lavoro giornaliere, le converte in minuti
        self._minuteDay = hoursDay*60
        #Minuti di lavoro effettuati
        self._timeWork = 0
        #Giorni di lavoro effettuati
        self._workingDays =0
        #Lista che contiene tutte le informazioni finali di lavorazione
        self._listEndWork = []
        #Richiamo del metodo per la produzione effettiva
        self.costruction(bikeBatch, dataBike,dataTime)
        #Richiamo del metodo per aggiornare i giorni di lavorazione
        self.setWorkingDays()
    
    """
    Metodo per la produzione effettiva, riceve come argomenti:
    - Lotto di bici in formato oggetto;
    - Elenco informazioni di tutti i tipi di bici;
    - Elenco tempi dei singoli task di tutti i tipi di bici."""
    def costruction(self, bikeBatch,dataBike,dataTime):
        #Ciclo che esegue il codice finche l'oggetto che contiene il lotto di bici non è vuoto e quindi sono state processate tutte le bici
        while len(bikeBatch) > 0:
            #Estazione casuale della prima bici da produrre, utile per non produrre i tipi in manierà sempre univoca
            keyC = choice(list(bikeBatch.keys()))
            if bikeBatch[keyC] >0:
                time = self._timeWork 
                #Creazione bici
                bike = Bike(keyC, dataBike,dataTime)
                task = bike.getTimeTask()
                #Script che si occupa di assegnare il tempo effettivo del singolo task
                for keyT in task:
                    self._timeWork += randint(task[keyT]["min"],task[keyT]["max"])
                self.setWorkingDays()
                #Script che, basandosi sul coefficiente di difetto, crea randomicamente alcuni bici difettate
                defect = True if randint(1,100) <= self._timeWork / self._nStations/self._workingDays * bike.getDefectCoef() else False
                #Calcolo del tempo effettivo di lavorazione per singola bici
                timeBike = self._timeWork-time
                #Script che, basandosi sul coefficiente di difetto, crea dei tempi di task anomali
                if randint(0,50) ==1:
                     timeBike = int(timeBike* (bike.getDefectCoef()*10+1))
                #Aggiunta della bici prodotta alla lista che contiene tutte le informazioni finali di lavorazione
                self._listEndWork.append([self._idBatch,str(datetime.now()).split(".")[0],str(int(self._workingDays)),str(bike.getType()),bike.getDescType(),str(timeBike),str(defect)])
                #Verifica della difettosità della bici così da capire se si deve procedere a produrla nuovamente
                if not defect:
                    bikeBatch[keyC]-=1
            #Se non ci sono più bici da produrre per quel tipo, si cancella il tipo dall'oggetto del lotto bici
            else:
                del bikeBatch[keyC]
    
    #Metodo per calcolare e settare i giorni lavorati
    def setWorkingDays(self):
        self._workingDays =self._timeWork/self._nStations /self._minuteDay
    
    #Metodo per visualizzare i giorni lavorati
    def getWorkingDays(self):
        return self._workingDays
    
    #Metodo per visualizzare i minuti di lavorazione
    def getTimeWork(self):
        return self._timeWork
    
    #Metodo per visualizzare la lista che contiene tutte le informazioni finali di lavorazione
    def getListEndWork(self):
        return self._listEndWork
    
    #Metodo per inserire i dati nel database
    def insertDB(self,database):
        query= "INSERT INTO Production(ID_Batch, Date_Time, Working_Days,ID_Bike, Time_Product, Defect) VALUES (%s, %s, %s,%s, %s,%s)"
        data = [(el[0],el[1], el[2],el[3],el[5],el[6]) for el in self._listEndWork]
        database.insert(query, data)
    
    #Metodo per esportare i dati in un csv
    def exportCsv(self,nFile):
        rows = [",".join(el) for el in self._listEndWork]
        data = "ID_Batch,Date_Time,Working_Days,ID_Bike,Desc_Bike,Time_Product,Defect\n"+"\n".join(rows)
        with open(nFile+".csv","w")as file:
            file.write(data)



