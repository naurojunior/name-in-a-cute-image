from PIL import (
    Image,
    ImageFont,
    ImageDraw
)

def image_with_text(text):
    img = Image.open("dog.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("impact.ttf", 120)
    draw.text(((img.width/2)-120,0),text,(255,255,255),font=font)
    return img

def save_image(image, filename):
    image.save(filename)
