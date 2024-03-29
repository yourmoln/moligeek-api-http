from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

import app.router as router

app = FastAPI()
app.include_router(router.about.router, prefix="/about")
app.include_router(router.zip.router, prefix="/zip")
app.include_router(router.web.router, prefix="/web")
app.include_router(router.network.router, prefix="/network")
app.include_router(router.LAN.router, prefix="/LAN")
app.include_router(router.encode.router, prefix="/encode")
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}