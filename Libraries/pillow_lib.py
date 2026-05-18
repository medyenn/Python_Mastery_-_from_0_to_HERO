from PIL import Image, ImageFilter, ImageOps
import requests


# You can run the requests_lib.py first to get a picture in this directory
# On which I'll try to apply my functions and methods:

image1 = Image.open('test.jpg')
# image1.show()
image1.save('chicago.jpeg')

image2 = Image.open('chicago.jpeg')
size_500 = (500, 500)
image2.thumbnail(size_500)
# image2.show()

image2.rotate(180).save('flipped_chic.jpeg')
image3 = Image.open('flipped_chic.jpeg')
# image3.show()

image2.convert(mode='L').save('chicago_BW.jpeg')
image4 = Image.open('chicago_BW.jpeg')
# image4.show()

image2.filter(ImageFilter.GaussianBlur(15)).save('chic_blur.jpeg')
image5 = Image.open('chic_blur.jpeg')
# image5.show()

url = 'https://static.vecteezy.com/system/resources/thumbnails/049/654/640/small/rectangle-shape-frame-glowing-blue-electric-arc-effect-transparent-background-image-free-png.png'

headers = {"User-Agent": "Mozilla/5.0"}
effect = requests.get(url, headers=headers)

if "image" in effect.headers.get("Content-Type", ""):
    with open("effect.png", "wb") as f:
        f.write(effect.content)

eff_im = Image.open("effect.png").convert("RGBA")

datas = eff_im.getdata()
new_data = []
for item in datas:
    r, g, b, a = item
    
    if r > 240 and g > 240 and b > 240:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

eff_im.putdata(new_data)
eff_im.save("effect_no_bg.png")
ImageOps.fit(image2, eff_im.size)

base = image2.convert("RGBA")
base.paste(eff_im, (0, 0), eff_im)
base.save("effected.png")

base.show()
