import socket
def getip(name):
    try:
        return {"ip":socket.gethostbyname(name)}
    except:
        return {"ip":"null"}
