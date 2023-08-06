from fastapi import APIRouter
from moligeek.core.LAN import *


router = APIRouter()

@router.get("/{ip_range}")
async def LAN_scan(ip_range:str = "192.168.31"):
    scan = Scan(ip_range)
    return {"ip": scan.run()}