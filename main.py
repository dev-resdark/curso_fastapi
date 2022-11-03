# python
from typing import Optional
from enum import Enum

# pydantic es una libreria de la cual llamamos a la clase BaseModel con 
# la cual podemos crear los modelos
from pydantic import BaseModel
from pydantic import Field


#fastapi
from webbrowser import get
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

#Models

class HairColor(Enum):
    black = "black"
    white = "white"
    brown = "brown"
    red = "red"
    purple = "purple"
    blonde = "blonde"

class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=6,
        max_length=75,
        ge=0
        )
    state: str=Field(
        ...,
        min_length=6,
        max_length=75,
        ge=0
        )
    country: str = Field(
        ...,
        min_length=6,
        max_length=75,
        ge=0
        )


class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ..., 
        min_length=1, 
        max_length=50
        )

    age: int = Field(
        ...,
        gt=0,
        le=80
        )
    hair_color:Optional[str] = Field(default=None) 
    is_married:Optional[bool] = Field(default=None)

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

# Validaciones: Request Body.

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ..., 
        title="Person Id", 
        description="This is the person's Id",
        gt=0
    ),
    person:Person = Body(...),
    Location: Location = Body(...)

):
    results = preson.dict()
    results.update(location.dict())
    return person
