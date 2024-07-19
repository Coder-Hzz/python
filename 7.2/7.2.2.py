url=""
import requests
res=requests.get(url)
open("shipingg.mp4","wb").write(res.content)

