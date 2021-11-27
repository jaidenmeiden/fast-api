from fastapi import FastAPI

app = FastAPI()


# app.get decorator
@app.get("/")
def home():
    return {"Hello": "World"}
