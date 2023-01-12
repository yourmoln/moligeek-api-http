import os,subprocess,sys
from fastapi import FastAPI

script_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(script_path)
from core import *

app = FastAPI()
@app.get("/")
async def root():
    return "welcome to moligeek-api-http"

@app.get("/ping/{ip:path}")
async def ping(ip:str):
    return "ping"+ip

@app.get("/network/getip/{ip:path}")
async def getip(ip:str):
    return network.getip(ip)

@app.get("/localhost/hostinfo/")
async def hostinfp():
    return localhost.hostinfo()

print("moligeek-api-http已启动")