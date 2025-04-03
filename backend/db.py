import mysql.connector

class DB:
    def __init__(self):
        with open("dbArchive/sql/config.txt") as file:
            self._data = file.read().split("\n")
            self._host = self._data[0].split(":")[1]
            self._user = self._data[1].split(":")[1]
            self._psw = self._data[2].split(":")[1]
            self._db= self._data[3].split(":")[1]
            self._port = self._data[4].split(":")[1]
        self.connectDB()

    def connectDB(self):
        self._connection= mysql.connector.connect(
        host=self._host,
        user=self._user,
        password=self._psw,
        database=self._db,
        port=self._port
        )

    
    def select(self,query):
        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def insert(self,query,data):
        cursor = self._connection.cursor()
        cursor.executemany(query, data)
        self._connection.commit()
        return f"{cursor.rowcount} was inserted."
    
    def update(self,query,data):
        cursor = self._connection.cursor()
        cursor.execute(query, data)
        self._connection.commit()
        return f"{cursor.rowcount} was updated."
    
    def disconnect(self):
        self._connection.close()
