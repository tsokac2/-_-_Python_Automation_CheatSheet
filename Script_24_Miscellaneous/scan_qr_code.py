import cv2
import webbrowser

image = cv2.imread('src/qr.png')
decetor = cv2.QRCodeDetector()
url, coords, pixels = decetor.detectAndDecode(image)
print(url, coords, pixels)

webbrowser.open(url)