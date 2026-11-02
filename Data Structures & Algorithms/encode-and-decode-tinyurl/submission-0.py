class Solution:
    def __init__(self):
        self.urls={}
        self.next=0
    
    def encode(self,longUrl:str)->str:
        self.next+=1
        short='https://tiny.url/'+str(self.next)
        self.urls[short]=longUrl
        return short
    
    def decode(self,shortUrl:str)->str:
        return self.urls[shortUrl]
