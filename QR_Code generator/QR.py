import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=40,border=7)
qr.add_data("https://www.w3schools.com/python/default.asp")
qr.make(fit=True)

img = qr.make_image(fill_color="black" , back_color="white")
img.save("advan.png")



