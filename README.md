# *QR-code-Generator*
This program generates a QR code that encodes a LinkedIn profile URL and saves it as an image file. Here's a brief description of the program:

1. The program imports the qrcode module for generating QR codes and the Image module from PIL for image manipulation.

2. It creates a QRCode object, specifying the QR code version, error correction level, box size, and border.

3. The program adds the LinkedIn profile URL to the QR code object using the add_data() method.

4. It generates the QR code using the make() method.

5. The program creates an image representation of the QR code, specifying the fill color (black) and background color (white) using the make_image() method.

6. It saves the generated QR code image as "Zain_LinkedIn.png" using the save() method.

In summary, this program uses the qrcode module to generate a QR code for a specific LinkedIn profile URL. The resulting QR code is then saved as a PNG image file, allowing it to be shared and scanned by others to access the LinkedIn profile directly.
