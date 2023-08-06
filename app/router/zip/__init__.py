from fastapi import APIRouter
from moligeek.core.zip import zipkey


router = APIRouter()

@router.get("/")
async def zip_password(path: str, mode: int = 1):
    password,time = zipkey(path, mode)
    return {"password": password, "time": time}