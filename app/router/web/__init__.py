from fastapi import APIRouter
from moligeek.core.web import *


router = APIRouter()

@router.get("/src")
async def get_src(path:str):
    src = upform(path)
    return {"src": src}

@router.get("/upform")
async def up_form(path: str, method = 'get', data = None):
    output = upform(path, method = method, formdata = data)
    return {"output": output}

@router.get("/find")
async def find_admin(path: str, kind:str = "php"):
    find = findadmin(path, kind = kind)
    return {"find": find}