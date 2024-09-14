#爬虫学习
import os
import requests
from lxml import etree # pip install lxml

def main(page):

    #用户输入界面
    #n = int(input("请输入您要查询的页数:"))

    #1.拿到网页源码
    #url = "https://pic.netbian.com/"

    #判断网页
    if page == 1:
        url = "https://pic.netbian.com/"
    else :
        url = f"https://pic.netbian.com/index_{page}.html"

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'

              }
    #r = requests.get(url , headers = header).text  #text就是获取网页源代码 ,注意编码问题,--->乱码
    r = requests.get(url, headers=header).content.decode('gbk')  #也是获取网页源代码,默认UTF-8
                                                         #gbk  gb2312

    #检查拿到的网页代码是不是正确的
    #print(r)

    #2.从源代码中提取所有图片的地址
    #取图片
    ret =etree.HTML(r)

    #先拿到所有的图片标签(li标签),然后再遍历的过程中拿到img标签
    li_list = ret.xpath('//div[@class="slist"]/ul/li')  #提取所有图片地址
                #获取父类标签,通过父类定向子类,父类不行就祖父类

    #判断所取值
    print(len(li_list))

    #对其进行遍历
    for li in li_list :
        li.xpath('./a/span/img') # 表示当前a标签下面的span标签下面的img标签
        #li.xpat('//img') -----> (错误的,会找重复的)  # 表示所有路径的img标签
        src = 'https://pic.netbian.com' + li.xpath('.//img/@src')[0]  # 表示当前路径任意位置的img标签
        print(src)
    #取文字
        name = li.xpath('.//img/@alt')[0]

    #3.保存图片
        img_code = requests.get(src).content
        with open(f'{picture_package}/{name}.jpg', 'wb') as f:
            f.write(img_code)







# 程序入口
if __name__ == '__main__' :
    picture_package = '彼岸图网照片库'
    if not os.path.exists(picture_package):  #如果没有picture_package这个文件夹就去创建一个
        os.mkdir(picture_package)

    for page in range(1 , 3 ) :
        main(page)












