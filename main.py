import pyqrcode



url=input("url:")

qr_code=pyqrcode.create(url)
qr_code.svg('qrCode.svg',scale=8)

