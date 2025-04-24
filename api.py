#Importazione libreria fastapi e dipendenze per la creazione del server backend
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

#Importazione dei miei script 
import mainBike
import db
from analysis import analysis

#Creazione variabile globale in cui salvare i lotti di produzione
costructBatch =""

# Creazione applicazione FastAPI
app = FastAPI()

#Impostazione del CORS per accettare richieste da qualsiasi fonte
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Creazione delle Classi per la tipizzazione dei dati ricevuti tramite richieste POST 
class EditBikes(BaseModel):
   id: int
   desc: str
   defCoef :float

class EditTask(BaseModel):
   idTask: int
   idBike: int
   min: int
   max :int

class CreateChart(BaseModel):
   total: str
   idBatch: str
   idBike: int =0

#Impostazione della Route per recuperare le esportazioni dei grafici
app.mount("/graph", StaticFiles(directory="graph"), name="graph")

#Route Get utilizzata per la produzione delle bici
@app.get("/")
async def productionBike(nStations: int=1, hoursDay: int=8 , bike1:int=0,bike2:int=0,bike3:int=0,bike4:int=0):
    
    #Creazione del dizionario che contiene l'elenco delle bici da produrre 
    batchBike = {1:bike1,2:bike2,3:bike3,4:bike4}
    
    #Tramite il costrutto try exept verifico la corretta connessione al db e la produzione delle bici
    try:

        #Connessione al DB e query per recupero informazioni bici
        database =db.DB()
        query = "SELECT * FROM Bike_Type"
        dataBike = database.select(query)
        query = "SELECT * FROM Time_Task ORDER BY ID_Bike, ID_Task"
        dataTime = database.select(query)
        
        #Produzione effettiva del lotto di bici
        global costructBatch
        costructBatch = mainBike.ConstructionBike(nStations, hoursDay,batchBike,dataBike,dataTime)
        
        #Richiamo del metodo per salvare le bici prodotte nel db
        costructBatch.insertDB(database)
        
        #Creazione dell'oggetto da restituire che conterrà le bici prodotte e il tempo di produzione
        objReturn = {"bikeMake":[],"timeWork":0}
        
        #Inserimento nell'oggetto delle bici prodotte
        for row in costructBatch.getListEndWork():
            objReturn["bikeMake"].append(row)
            
        
        #Disconnessione DB
        database.disconnect()

        #Inserimento nell'oggetto del tempo effettivo di produzione
        objReturn["timeWork"] = costructBatch.getTimeWork()

        #Restituzione dell'oggetto alla richiesta GET
        return objReturn
    
    #Se ho qualsiasi problema con la connessione al DB o la produzione restituisco errore
    except:
        raise HTTPException(status_code=503, detail="Error Connection DB or Build Bike")

#Route Get utilizzata per visualizzazione caratteristiche generiche bici
@app.get("/bike")
async def showBike():

    try:
        database =db.DB()
        query = "SELECT * FROM Bike_Type"
        dataBike = database.select(query)
        database.disconnect()
        return dataBike
    
    except:
        raise HTTPException(status_code=503, detail="Error Connection DB")

#Route Get utilizzata per filtrare le informazioni di visualizzazione dei singoli task
@app.get("/task/view")
async def showTaskFilter(idBike:int=0,idTask:int=0):
    
    try:
        database =db.DB()

        #Filtro sulla base dell'id della bici
        if idBike == 0:
            query = f"""SELECT Time_Task.ID_Bike,Bike_Type.Descri,Task_Cost.ID_Task, Task_Cost.Description, Time_Task.Min, Time_Task.Max 
            FROM Time_Task
            INNER JOIN Bike_Type
            ON Time_Task.ID_Bike = Bike_Type.ID_Type
            INNER JOIN Task_Cost
            ON Time_Task.ID_Task = Task_Cost.ID_Task
            WHERE Time_Task.ID_Task = {idTask}
            ORDER by Bike_Type.ID_Type, Task_Cost.ID_Task"""
        
        #Filtro sulla base dell'id del task
        else:
            query = f"""SELECT Time_Task.ID_Bike,Bike_Type.Descri,Task_Cost.ID_Task, Task_Cost.Description, Time_Task.Min, Time_Task.Max 
            FROM Time_Task
            INNER JOIN Bike_Type
            ON Time_Task.ID_Bike = Bike_Type.ID_Type
            INNER JOIN Task_Cost
            ON Time_Task.ID_Task = Task_Cost.ID_Task
            WHERE Time_Task.ID_Bike = {idBike}
            ORDER by Bike_Type.ID_Type, Task_Cost.ID_Task"""

        
        dataBike = database.select(query)
        database.disconnect()
        return dataBike
    except:
        raise HTTPException(status_code=503, detail="Error Connection DB")

#Route Get utilizzata per visualizzazione dei singoli task
@app.get("/task")
async def showTask():
    try:
        database =db.DB()
        query = """SELECT Time_Task.ID_Bike,Bike_Type.Descri,Task_Cost.ID_Task, Task_Cost.Description, Time_Task.Min, Time_Task.Max 
        FROM Time_Task
        INNER JOIN Bike_Type
        ON Time_Task.ID_Bike = Bike_Type.ID_Type
        INNER JOIN Task_Cost
        ON Time_Task.ID_Task = Task_Cost.ID_Task
        ORDER by Bike_Type.ID_Type, Task_Cost.ID_Task"""
        dataBike = database.select(query)
        database.disconnect()
        return dataBike
    
    except:
        raise HTTPException(status_code=503, detail="Error Connection DB")

#Route Get utilizzata per filtrare la visualizzazione dello storico di tutte le bici prodotte
@app.get("/prod/view")
async def showProdFilter(idBatch:str="",idBike:int=0,defect:str=""):
    try:
        database =db.DB()

        #Filtro sulla base dell'id del lotto
        if idBatch != "":
            query = f"""SELECT Production.ID , Production.ID_Batch, Production.Date_Time, 
            Production.ID_Bike,Bike_Type.Descri,Production.Working_Days, 
            Production.Time_Product, Production.Defect 
            FROM Production INNER JOIN Bike_Type ON Production.ID_Bike = Bike_Type.ID_Type
            WHERE Production.ID_Batch ='{idBatch}'"""
        
        #Filtro sulla base dell'id delle bici
        elif idBike != 0:
            query = f"""SELECT Production.ID , Production.ID_Batch, Production.Date_Time, 
            Production.ID_Bike,Bike_Type.Descri,Production.Working_Days, 
            Production.Time_Product, Production.Defect 
            FROM Production INNER JOIN Bike_Type ON Production.ID_Bike = Bike_Type.ID_Type
            WHERE Production.ID_Bike ={idBike}"""
        
        #Filtro sulla base della difettosità
        elif defect != "":
            query = f"""SELECT Production.ID , Production.ID_Batch, Production.Date_Time, 
            Production.ID_Bike,Bike_Type.Descri,Production.Working_Days, 
            Production.Time_Product, Production.Defect 
            FROM Production INNER JOIN Bike_Type ON Production.ID_Bike = Bike_Type.ID_Type
            WHERE Production.Defect ='{defect}'"""

        dataBike = database.select(query)
        database.disconnect()
        return dataBike
    
    except:
        raise HTTPException(status_code=503, detail="Error Connection DB")

#Route Get utilizzata per visualizzazione dello storico di tutte le bici prodotte
@app.get("/prod")
async def showProd():
    try:
        database =db.DB()
        query = """SELECT Production.ID , Production.ID_Batch, Production.Date_Time, 
        Production.ID_Bike,Bike_Type.Descri,Production.Working_Days, 
        Production.Time_Product, Production.Defect 
        FROM Production INNER JOIN Bike_Type ON Production.ID_Bike = Bike_Type.ID_Type"""
        dataBike = database.select(query)
        database.disconnect()
        return dataBike
    
    except:
        raise HTTPException(status_code=503, detail="Error Connection DB")

#Route POST utilizzata per modificare il tipo di bici che si possono produrre
@app.post("/edit-bike/")
async def editBike(listBike:EditBikes):
    try:
        database =db.DB()
        #Trasformazione dei dati ricevuti in dizionario
        data = listBike.model_dump()
        query= "UPDATE Bike_Type SET Descri = %s, Defect_Coefficient= %s WHERE ID_Type = %s"
        dataQ = (data["desc"],data["defCoef"],data["id"])
        rowU =database.update(query, dataQ)
        database.disconnect()
        return rowU
    
    except:
        raise HTTPException(status_code=503, detail="Error Connection DB")

#Route POST utilizzata per modificare le tempistiche dei singoli task
@app.post("/edit-task/")
async def editTask(listTask:EditTask):
    try:
        database =db.DB()
        data = listTask.model_dump()
        query= "UPDATE Time_Task SET Min = %s, Max= %s WHERE ID_Task = %s AND ID_Bike =  %s"
        dataQ = (data["min"],data["max"],data["idTask"],data["idBike"])
        rowU =database.update(query, dataQ)
        database.disconnect()
        return rowU
    
    except:
        raise HTTPException(status_code=503, detail="Error Connection DB")

#Route POST utilizzata per la creazione dei grafici di analisi
@app.post("/create-chart/")
async def createChart(listParam:CreateChart):
    try:
        database =db.DB()
        data = listParam.model_dump()
        #Se l'argomento total ricevuto è diverso da "false" crea un grafico con tutti i dati
        if data["total"] != "false":
            query = """SELECT Production.ID , Production.ID_Batch, Production.Date_Time, 
            Production.ID_Bike,Bike_Type.Descri,Production.Working_Days, 
            Production.Time_Product, Production.Defect 
            FROM Production INNER JOIN Bike_Type ON Production.ID_Bike = Bike_Type.ID_Type"""
        
        #Se l'argomento "idbatch" ricevuto è diverso da "false" crea un grafico per uno specifico lotto di produzione
        elif data["idBatch"] != "false":
            query = f"""SELECT Production.ID , Production.ID_Batch, Production.Date_Time, 
            Production.ID_Bike,Bike_Type.Descri,Production.Working_Days, 
            Production.Time_Product, Production.Defect 
            FROM Production INNER JOIN Bike_Type ON Production.ID_Bike = Bike_Type.ID_Type
            WHERE Production.ID_Batch ='{data["idBatch"]}'"""

        #Se l'argomento "idBike" ricevuto è diverso da 0 crea un grafico per uno specifico tipo di bici
        elif data["idBike"] != 0:
            query = f"""SELECT Production.ID , Production.ID_Batch, Production.Date_Time, 
            Production.ID_Bike,Bike_Type.Descri,Production.Working_Days, 
            Production.Time_Product, Production.Defect 
            FROM Production INNER JOIN Bike_Type ON Production.ID_Bike = Bike_Type.ID_Type
            WHERE Production.ID_Bike ={data["idBike"]}"""

        dataBike = database.select(query)
        database.disconnect()

        #Solo quando il grafico viene creato restituisco il percorso che verrà utilizzato per visualizzarlo sul frontend
        path =analysis(dataBike)
        return {"path":path}
    
    except:
        raise HTTPException(status_code=503, detail="Error Connection DB")

#Esecuzione del server uvicorn
if __name__ == "__main__":
   uvicorn.run("api:app", host="backend", port=8000, reload=True)

