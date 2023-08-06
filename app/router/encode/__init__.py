from fastapi import APIRouter
from moligeek.core.encode import *


router = APIRouter()

@router.get("/decode")
async def to_decode(text:str):
    code = todecode(text)
    return code.autodecode()

@router.get("/fence")
async def to_fence(text:str, key:int = 2, method:str = 'encode'):
    if method == 'encode':
        code = fence.encrypt(text,key)
    elif method == 'decode':
        code = fence.decrypt(text,key)
    return {"output": code}