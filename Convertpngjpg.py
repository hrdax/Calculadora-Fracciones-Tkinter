from PIL import Image
image = Image.open(".png")
convertergb = image.convert("RGB")
convertergb.save(".jpg")