import qrcode

data = "https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version=1,
                   box_size=10,
                   border=5)
# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color='yellow',
                    back_color='blue')

img.save('MyQRCode2.png')