import qrcode
from PIL import Image
qr= qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=10,border=4)
qr.add_data("https://www.linkedin.com/in/zain-ali-26ba96267/")         #Your Url here
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("Zain_LinkedIn.png")