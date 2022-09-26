#from fastapi import FastAPI
from flask import Flask
import sqlite3

app = Flask(__name__)
#app = FastAPI()

myCon = sqlite3.connect("DBAUDITORIA",check_same_thread=False)
myCursor = myCon.cursor()
myCursor.execute("CREATE TABLE IF NOT EXISTS RESULTADOS (ID INTEGER PRIMARY KEY AUTOINCREMENT,SUMANDO01 INTEGER NOT NULL,SUMANDO02 INTEGER NOT NULL, RESULTADO INTEGER)")


def insertAuditoria(sumandouno,sumandodos,resultado):
    queryToInsert = """
    INSERT INTO RESULTADOS (ID,SUMANDO01,SUMANDO02,RESULTADO) VALUES (NULL, {sumando1}, {sumando2}, {result})
    """.format(sumando1=sumandouno,sumando2=sumandodos,result=resultado)
    myCursor.execute(queryToInsert)
    myCon.commit()
    
#insertAuditoria(100,100,200)

@app.route('/retoibm/sumar/<sumando01>/<sumando02>')
def suma(sumando01,sumando02):
    resultado = int(sumando01) + int(sumando02)
    insertAuditoria(int(sumando01),int(sumando02),int(resultado))
    return {"resultado": resultado}

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80,debug = True)






#--   Fast API

"""
@app.get("/retoibm/sumar/{sumando01}/{sumando02}")
#async def read_item(sumando01 : int,sumando02 : int):
def read_item(sumando01 : int,sumando02 : int):   
    resultado = sumando01 + sumando02
    insertAuditoria(sumando01,sumando02,resultado)
    return {"resultado": resultado}
"""