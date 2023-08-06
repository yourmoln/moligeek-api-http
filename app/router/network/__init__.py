from fastapi import APIRouter
from moligeek.core.network import *


router = APIRouter()

@router.get("/info")
async def host_info():
    info = Hostinfo()
    return info.all()

@router.get("/ping")
async def to_ping(ip:str):
    output = ping(ip)
    return {"output": output}

@router.get("/getip")
async def get_ip(name:str):
    ip = getip(name)
    return {"ip": ip}