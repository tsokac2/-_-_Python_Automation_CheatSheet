import qrcode

img = qrcode.make('https://google.com')
img.save('src/qr1.png')

# Create a program that reads a text file containing URLs and generates a QR code for each URL. For example, if the text file contains five URLs, 
# the program will generate five different image files each containing a QR code. You can use the urls.txt file attached to this article.
 
with open('src/urls.txt') as file:
  lines = file.readlines()
  count = 1
  for line in lines:
    img = qrcode.make(line)
    img.save(f"src/{count}.png")
    count += 1