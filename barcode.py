import qrcode

qrcode_data = 'https://www.youtube.com/c/EmbeddedProgrammer'
image  = qrcode.make(qrcode_data)
image.save('QR.png')
