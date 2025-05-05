import qrcode

data = 'Matte er løye med Python'

img = qrcode.make(data)

img.save('C:/Users/willi/Python koder/minqrcode.png')