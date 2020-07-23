import requests

r = requests.get("http://google.com

f = open("./page.html","w+")
f.write(r.text)
