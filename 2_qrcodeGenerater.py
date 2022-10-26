# Simple type qr code making using qrcode module and convert this code in png file and using some advance type making like change background , border 
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)

qr.add_data("https://stechpic1.blogspot.com/")
qr.make(fit=True)
img = qr.make_image(fill_color="yellow",back_color="blue")
img.save("Stech_web.png")