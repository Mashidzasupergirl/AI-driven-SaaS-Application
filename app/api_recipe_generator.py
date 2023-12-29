from typing import Union
from recipe_generator import generate_recipe

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/generate_recipe")
async def generate_recipe_api(prompt: str):
    recipe = generate_recipe(prompt)
    return recipe

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}