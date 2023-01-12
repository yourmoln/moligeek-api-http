import base64,urllib

class todecode:
    def base64(self,text):
        try:
            return base64.b64decode(text.encode("utf-8")).decode("utf-8")
        except:
            return
    def base32(self,text):
        try:
            return base64.b32decode(text.encode("utf-8")).decode("utf-8")
        except:
            return
    def base16(self,text):
        try:
            return base64.b16decode(text.encode("utf-8")).decode("utf-8")
        except:
            return
    def url(self,text):
        try:
            return urllib.parse.unquote(text)
        except:
            return
    def unicode(self,text):
        try:
            return text.encode("utf-8").decode("unicode_escape")
        except:
            return
    def __init__(self,text):
        print("base64:",self.base64(text))
        print("base32:",self.base32(text))
        print("base16:",self.base16(text))
        print("URL:",self.url(text))
        print("unicode:",self.unicode(text))
