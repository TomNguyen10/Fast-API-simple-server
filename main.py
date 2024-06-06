from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()


inventory = {
    1: {
        "name": "milk",
        "price": 2.5,
        "brand": "Nestle"
    },
    2: {
        "name": "bread",
        "price": 1.5,
        "brand": "Bimbo"
    }
}


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.get("/about")
def about():
    return {"message": "About page"}


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item you'd like to view"), gt=0, lt=3):
    return inventory[item_id]


@app.get("/get-by-name")
def get_item(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}
