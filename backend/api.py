from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mainBike
import db
from analysis import analysis



costructBatch =""

# Creazione applicazione FastAPI
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


app.mount("/graph", StaticFiles(directory="graph"), name="graph")


@app.get("/")
async def productionBike(nStations: int=1, hoursDay: int=8 , bike1:int=0,bike2:int=0,bike3:int=0,bike4:int=0):
    
    batchBike = {1:bike1,2:bike2,3:bike3,4:bike4}
    
    try:
        database =db.DB()
        
        query = "SELECT * FROM Bike_Type"
        dataBike = database.select(query)
        query = "SELECT * FROM Time_Task ORDER BY ID_Bike, ID_Task"
        dataTime = database.select(query)
        
        global costructBatch
        costructBatch = mainBike.ConstructionBike(nStations, hoursDay,batchBike,dataBike,dataTime,database)
        objReturn = {"bikeMake":{},"timeWork":0}
        num = 0
        for row in costructBatch.getListEndWork():
            objReturn["bikeMake"][num] = row
            num +=1
        database.disconnect()
        objReturn["timeWork"] = costructBatch.getTimeWork()
        return objReturn
    except:
        
        raise HTTPException(status_code=503, detail="Error Connection DB")

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

@app.get("/task/view")
async def showTaskFilter(idBike:int=0,idTask:int=0):
    
    try:
        database =db.DB()
        
        if idBike == 0:
            query = f"""SELECT Time_Task.ID_Bike,Bike_Type.Descri,Task_Cost.ID_Task, Task_Cost.Description, Time_Task.Min, Time_Task.Max 
            FROM Time_Task
            INNER JOIN Bike_Type
            ON Time_Task.ID_Bike = Bike_Type.ID_Type
            INNER JOIN Task_Cost
            ON Time_Task.ID_Task = Task_Cost.ID_Task
            WHERE Time_Task.ID_Task = {idTask}
            ORDER by Bike_Type.ID_Type, Task_Cost.ID_Task"""
            
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


@app.get("/prod/view")

async def showProdFilter(idBatch:str="",idBike:int=0,defect:str=""):
    try:
        database =db.DB()
        if idBatch != "":
            query = f"""SELECT Production.ID , Production.ID_Batch, Production.Date_Time, 
            Production.ID_Bike,Bike_Type.Descri,Production.Working_Days, 
            Production.Time_Product, Production.Defect 
            FROM Production INNER JOIN Bike_Type ON Production.ID_Bike = Bike_Type.ID_Type
            WHERE Production.ID_Batch ='{idBatch}'"""
        elif idBike != 0:
            query = f"""SELECT Production.ID , Production.ID_Batch, Production.Date_Time, 
            Production.ID_Bike,Bike_Type.Descri,Production.Working_Days, 
            Production.Time_Product, Production.Defect 
            FROM Production INNER JOIN Bike_Type ON Production.ID_Bike = Bike_Type.ID_Type
            WHERE Production.ID_Bike ={idBike}"""
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


@app.post("/edit-bike/")
async def editBike(listBike:EditBikes):
    
    try:
        database =db.DB()
    
        data = listBike.model_dump()
        query= "UPDATE Bike_Type SET Descri = %s, Defect_Coefficient= %s WHERE ID_Type = %s"
        dataQ = (data["desc"],data["defCoef"],data["id"])
        rowU =database.update(query, dataQ)
        database.disconnect()
        return rowU
    
    except:
        raise HTTPException(status_code=503, detail="Error Connection DB")

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

@app.post("/create-chart/")
async def createChart(listParam:CreateChart):
    try:
        database =db.DB()
        data = listParam.model_dump()
        
        if data["total"] != "false":
            query = """SELECT Production.ID , Production.ID_Batch, Production.Date_Time, 
            Production.ID_Bike,Bike_Type.Descri,Production.Working_Days, 
            Production.Time_Product, Production.Defect 
            FROM Production INNER JOIN Bike_Type ON Production.ID_Bike = Bike_Type.ID_Type"""
            
        elif data["idBatch"] != "false":
            query = f"""SELECT Production.ID , Production.ID_Batch, Production.Date_Time, 
            Production.ID_Bike,Bike_Type.Descri,Production.Working_Days, 
            Production.Time_Product, Production.Defect 
            FROM Production INNER JOIN Bike_Type ON Production.ID_Bike = Bike_Type.ID_Type
            WHERE Production.ID_Batch ='{data["idBatch"]}'"""

        elif data["idBike"] != 0:
            query = f"""SELECT Production.ID , Production.ID_Batch, Production.Date_Time, 
            Production.ID_Bike,Bike_Type.Descri,Production.Working_Days, 
            Production.Time_Product, Production.Defect 
            FROM Production INNER JOIN Bike_Type ON Production.ID_Bike = Bike_Type.ID_Type
            WHERE Production.ID_Bike ={data["idBike"]}"""

        dataBike = database.select(query)
        database.disconnect()
        path =analysis(dataBike)
        return {"path":path}
    
    except:
        raise HTTPException(status_code=503, detail="Error Connection DB")
   
if __name__ == "__main__":
   uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)

