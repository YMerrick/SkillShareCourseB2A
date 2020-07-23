import requests
from PIL  import Image
from io import BytesIO

r = requests.get("https://i.pinimg.com/originals/a0/f4/33/a0f433603c8a62e9df3d7d25d3b3649e.png")
print('Status code:', r.status_code)
image = Image.open(BytesIO(r.content))

path = "./image1."+image.format

print(image.size,image.format,image.mode)

try:
    image.save(path,image.format)
except IOError:
    print('Can not save image')
