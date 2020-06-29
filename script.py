from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.open("dog.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("impact.ttf", 120)
draw.text(((img.width/2)-120,0),"JOÃO",(255,255,255),font=font)
img.save('dog2.jpg')