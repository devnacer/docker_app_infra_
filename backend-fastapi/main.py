from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Python backend 🚀"}

@app.get("/api/test")
def test():
    return {"status": "ok", "data": "Backend working"}
