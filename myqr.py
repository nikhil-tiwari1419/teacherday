import qrcode
from PIL import  Image, ImageDraw, ImageFont

data = "https://nikhil-tiwari1419.github.io/teacherday/"

qr = qrcode.QRCode(
    version = 5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border =4,
)
qr.add_data(data)
qr.make(fit=True)
qr_img= qr.make_image(fill_color="black",back_color="white").convert("RGB")

try:
    font = ImageFont.truetype("arial.ttf",40)
except:
    font = ImageFont.load_default()

draw = ImageDraw.Draw(qr_img)
text = "Teacher's Day "
bbox = draw.textbbox((0,0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

x = (qr_img.size[0] - text_width) //2
y = (qr_img.size[1] - text_height) //2

draw.rectangle(
    [x - 10, y - 15, x+text_width +10 , y + text_height +10],
    fill="white"
)

for dx in [0, 1, -1]:
    for dy in [0, 1, -1]:
        draw.text((x + dx, y + dy), text, font=font, fill="blue")

draw.text((x,y), text, font=font, fill=("blue"))

qr_img.save("qr_img.png")

