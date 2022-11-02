# python
from typing import Optional

# pydantic es una libreria de la cual llamamos a la clase BaseModel con 
# la cual podemos crear los modelos
from pydantic import BaseModel


#fastapi
from webbrowser import get
from fastapi import FastAPI
from fastapi import Body, Query, Path

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


# Validaciones: Query Parameters

@app.get("/person/detail")
def show_person(
    name:Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="Person Name",
        description="This is the person's name. It's between 1 to 50 characters"
    ),
    age:Optional[str] = Query(
        ...,
        title="person age",
        description="This is the person's age. It's requeride"
    )
):
    return{name: age}

# Validaciones: Path Parameters.

@app.get("/person/detail/{person_id}")
def show_person(
    person_id:Optional[int] = Path(
        ..., 
        gt=0,
        title="Person Id",
        description="This is the person's id. This must be greater than zero. It's requeride"
    )
):

    return{person_id: "It exists!"}