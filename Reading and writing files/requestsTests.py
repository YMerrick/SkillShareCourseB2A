import requests



params = {"q":"pizza"}
r = requests.get("http://bing.com/search", params=params)
print(r.url)
f = open("./page.html","w+")
f.write(r.text)
