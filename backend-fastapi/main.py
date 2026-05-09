from fastapi import FastAPI
from sqlalchemy import create_engine

app = FastAPI()

DATABASE_URL = "mysql+pymysql://myuser:mypassword@mysql-db/myappdb"

engine = create_engine(DATABASE_URL)

@app.get("/api/test-db")
def test_db():
    connection = engine.connect()
    connection.close()

    return {"database": "connected"}
