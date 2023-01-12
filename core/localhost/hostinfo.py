import socket,json,os,platform,time
from urllib.request import urlopen

def getip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        address = ("8.8.8.8", 80)
        s.connect(address)
        sockname = s.getsockname()
        ip = sockname[0]
        port = sockname[1]
    finally:
        s.close()
    return ip
def getoutip():
    try:
        return json.load(urlopen('http://jsonip.com'))['ip']
    except:
        return "未获取到公网IP"
def hostinfo():
    outip = getoutip()
    ip = getip()
    return {
        "网络信息":
        {"公网": outip , "内网" : ip},
        "系统信息":{
            "系统类型" : platform.system(),
            "系统版本" :platform.version(),
            "计算机名字" : platform.node(),
            "CPU架构" : platform.machine(),
            "CPU厂商" : platform.processor(),
            "系统时间" : time.asctime()
        },
        "脚本信息":{
        "脚本位置" : os.path.split(os.path.realpath(__file__))[0].replace(r"core\localhost",'')
        }
    }
