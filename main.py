# python
from typing import Optional

# pydantic es una libreria de la cual llamamos a la clase BaseModel con 
# la cual podemos crear los modelos
from pydantic import BaseModel


#fastapi
from webbrowser import get
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

#Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color:Optional[str] = None
    is_married:Optional[bool] = None

@app.get("/") #esto es un decodorador de la funcion que vamos a crear

def home(): 
    return{"Hello": "World"}

#Request and Response Body.

@app.post("/person/new")

def create_person(person: Person = Body(...)):
    return person
