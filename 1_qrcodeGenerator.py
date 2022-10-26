# Simple type qr code making using qrcode module and convert this code in png file
import qrcode as qr

img = qr.make("https://stechpic1.blogspot.com/")
img.save("stechpic_wev.png")