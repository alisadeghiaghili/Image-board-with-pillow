from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("readonly/fanwood-webfont.ttf", 50)
image = Image.open("readonly/msi_recruitment.gif")
image = image.convert('RGB')

channels = image.split()

# create every partial image
images=[]
for channel in range(3):
    for intensity in [0.1, 0.5, 0.9]:
        rectangle = Image.new('RGB', (image.width, 60), color = 0)
        new_channels = list(channels)
        new_channels[channel] = new_channels[channel].point(lambda value: value * intensity)
        new_image = Image.merge('RGB', (new_channels[0], new_channels[1], new_channels[2]))
        text = "channel " + str(channel) + " intensity " + str(intensity)
        draw = ImageDraw.Draw(rectangle).text((0, 20), text, fill = new_image.getpixel((0, 50)), font = font)
        partial_image = Image.new(image.mode, (image.width, image.height + rectangle.height))
        partial_image.paste(new_image, (0, 0))
        partial_image.paste(rectangle, (0, image.height))
        images.append(partial_image)

# create canvas
first_image = images[0]
contact_sheet = Image.new(first_image.mode, (first_image.width * 3, first_image.height * 3))
x=0
y=0

# create big image
for img in images:
    contact_sheet.paste(img, (x, y))
    if x + first_image.width == contact_sheet.width:
        x = 0
        y += first_image.height
    else:
        x += first_image.width

# resize and display the big image
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2), int(contact_sheet.height/2) ))
display(contact_sheet)
