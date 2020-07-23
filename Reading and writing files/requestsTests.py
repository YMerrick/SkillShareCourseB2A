import requests


myData = {"Name":"Nick","email":"nick@example.com"}
r = requests.post("https://www.w3schools.com/php/welcome.php", data=myData)

f = open("myfile.html","w+")

f.write(r.text)
