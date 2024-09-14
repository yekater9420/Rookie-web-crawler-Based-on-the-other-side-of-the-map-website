#保存图片代码
import requests

url = ''
img_code = requests.get(url).content
with open('1.jpg' , 'wb') as f :
    f.write(img_code)