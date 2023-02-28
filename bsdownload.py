from bs4 import BeautifulSoup
import re
import os
import requests
import string

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"}
root ='https://papers.gceguide.com/Cambridge%20IGCSE/Mathematics%20(0580)/2021/'

#访问网页，并且用beautifulsoup获取下载链接
def getHtml(url):
    res = requests.get(url, headers=headers)
    #用BS4解析res.text
    #BeautifulSoup(markup=...,features=...,builder=...,)以下的keyarg
    soup = BeautifulSoup(res.text,'html.parser') #BS库，加入html parse是使用html剖析器，避免报错
    links = soup.find_all('a') #输出a标签中的内容 这时候的links还包含很多 a href = '......' <span>
    url_group = []
	#判断link当中的链接是否是否为  ...pdf
    for link in links:
        if 'w19' in link.get('href', []) and '.pdf' in link.get('href', []):
            content = link.get('href').replace('download_file.php?files=','')
            print(content)
            url_group.append(content)  #link.get('href')就只保留下来下载链接了
    return url_group

def getFile(link):
    file_name = link.split('/')[-1]
    pdf = requests.get(link, headers)
    with open(file_name, "wb") as code:
        code.write(pdf.content)
    print("Sucessful to download" + " " + file_name)

#主程序
url ='https://pastpapers.papacambridge.com/papers/caie/cambridge-advanced-as-and-a-level-mathematics-9709-2019-oct-nov'
url_group = getHtml(url)


os.chdir(os.path.join(os.getcwd(), '0625_download')) #选择目录，通过关键词
jg = open('全部下载链接.txt','w',encoding='utf8') #当前目录下创建全部下载链接.txt

for link in url_group:
    if 'k-9' in link:
        pass
    else:
        jg.write(link+'\r')
        getFile(link)
jg.close()
