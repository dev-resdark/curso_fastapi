from webbrowser import get
from fastapi import FastAPI

app = FastAPI()

@app.get("/") #esto es un decodorador de la funcion que vamos a crear

def home(): 
    return{"Hello": "World"}