from random import randint, choice, choices
from datetime import datetime
import string

class Bike:
    def __init__(self, type,dataBike, dataTime):
        self._type = type
        self._descType = dataBike[type-1][1]
        self._timeTask = {}
        self.setTimeTask(dataTime)
        self._defectCoef = 0
        self.setDefectCoef(dataBike)

    def setTimeTask(self, dataTime):
        for row in dataTime:
            if self._type == row[1]:
                self._timeTask["T"+str(row[2])] = {"min":int(row[3]),"max":int(row[4])}

    def setDefectCoef(self, dataBike):
        self._defectCoef = float(dataBike[self._type-1][2])

    def getDescType(self):
        return self._descType
    
    def getType(self):
        return self._type
    
    def getTimeTask(self):
        return self._timeTask
    
    def getDefectCoef(self):
        return self._defectCoef
        

    def __str__(self):
        return f"Bicycle type: {self._descType}, Time Task: {self._timeTask}, defect coefficient: {self._defectCoef}"


class ConstructionBike:
    def __init__(self, nStations, hoursDay, bikeBatch, dataBike,dataTime, database):
        self._idBatch = ''.join(choices(string.ascii_letters + string.digits, k=8))
        self._nStations = nStations
        self._minuteDay = hoursDay*60
        self._timeWork = 0
        self._workingDays =0
        self._listEndWork = []
        self.costruction(bikeBatch, dataBike,dataTime)
        self.setWorkingDays()
        self.insertDB(database)
    def costruction(self, bikeBatch,dataBike,dataTime):
        while len(bikeBatch) > 0:
            keyC = choice(list(bikeBatch.keys()))
            if bikeBatch[keyC] >0:
                time = self._timeWork 
                
                bike = Bike(keyC, dataBike,dataTime)
                task = bike.getTimeTask()
                for keyT in task:
                    self._timeWork += randint(task[keyT]["min"],task[keyT]["max"])
                self.setWorkingDays()
                defect = True if randint(1,100) <= self._timeWork / self._nStations/self._workingDays * bike.getDefectCoef() else False
                timeBike = self._timeWork-time
                if randint(0,50) ==1:
                     timeBike = int(timeBike* (bike.getDefectCoef()*10+1))
                
                self._listEndWork.append([self._idBatch,str(datetime.now()).split(".")[0],str(int(self._workingDays)),str(bike.getType()),bike.getDescType(),str(timeBike),str(defect)])
                if not defect:
                    bikeBatch[keyC]-=1
                
            else:
                del bikeBatch[keyC]
    def setWorkingDays(self):
        self._workingDays =self._timeWork/self._nStations /self._minuteDay
    
    def getWorkingDays(self):
        return self._workingDays
    
    def getTimeWork(self):
        return self._timeWork

    def getListEndWork(self):
        return self._listEndWork
    
    def insertDB(self,database):
        query= "INSERT INTO Production(ID_Batch, Date_Time, Working_Days,ID_Bike, Time_Product, Defect) VALUES (%s, %s, %s,%s, %s,%s)"
        data = [(el[0],el[1], el[2],el[3],el[5],el[6]) for el in self._listEndWork]
        database.insert(query, data)
    
    def exportCsv(self,nFile):
        rows = [",".join(el) for el in self._listEndWork]
        data = "ID_Batch,Date_Time,Working_Days,ID_Bike,Desc_Bike,Time_Product,Defect\n"+"\n".join(rows)
        with open(nFile+".csv","w")as file:
            file.write(data)



