import requests
import json

api_key = "<your_api_access_token>"

url = f"https://graph.facebook.com/v19.0/10232031908089224?fields=id%2Cname&access_token={api_key}"
response = requests.get(url)
print(response.text)
# Returns: {"id":"10232031908089224","name":"Tomislav Soka\u010d"}

img_url = f"https://graph.facebook.com/v19.0/10231885381986163?fields=link%2Cimages&access_token={api_key}"
response_img = requests.get(img_url)
data = response_img.text
data = json.loads(data)

img_data = data['images'][0]['source']
images_bytes = requests.get(img_data).content

with open('image.jpg', 'wb') as file:
    file.write(images_bytes)

# Downloads image in the root folder

# print(data['images'][0]['source'])
# Returns: 
# {'height': 1440, 'source': 'https://scontent-dub4-1.xx.fbcdn.net/v/t39.30808-6/431470107_10231885381746157_3725969732798326165_n.jpg
#  ?_nc_cat=107&ccb=1-7&_nc_sid
#  =5f2048&_nc_ohc=whxeuNOp9koAb4Zuql1&_nc_ht=scontent-dub4-1.xx&edm
#  =AMAeTUEEAAAA&oh=00_AfAwwQSSnXiWPubVlEAGV-DCYp_bHG41KgK_Ff64EqJZGw&oe=661440F7', 'width': 1440}