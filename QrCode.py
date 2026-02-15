import  pyqrcode
url=input("Enter URL: ")

qr_code=pyqrcode.create(url)
qr_code.svg("qr_code.svg",scale=5)
