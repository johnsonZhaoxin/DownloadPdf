from bs4 import BeautifulSoup
import re
import os
import requests
import string
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"}
root ='https://cdn.savemyexams.co.uk/pdfs/'

# 访问本地连接储存网页，并且用beautifulsoup获取下载链接
def getNamesHtml(url):
    with open(url) as fp:
        soup = BeautifulSoup(fp,'html.parser')
        links = soup.find_all('a') #这里就是一个列表了 a href 
        url_group= []
        file_names = []
        for link in links:
            #print(link)
            name = link.get_text().replace('\n','')
            orginal_link = link.get('href')
            downloadlink = getDownloadUrl(orginal_link)
            url_group.append(root+downloadlink[0])
            file_names.append(name)
    fp.close()
    result = dict(zip(file_names,url_group))
    return result

# 虚假链接的处理
# 结果一般是
# https://pdf3.savemyexams.co.uk/?get=%7B%22url%22%3A%22https%3A%2F%2Fwww.savemyexams.co.uk%2Fdp%2Fmaths_ai-hl%2Fib%2F21%2Ftopic-questions%2F4-statistics--probability%2F4-10-poisson-distribution%2F-%2F-%2Fmedium%2F%22%2C%22file%22%3A%22GhUbxomn~ltrvBgy.pdf%22%2C%22bucket%22%3A%22cdn.savemyexams.co.uk%22%7D.nvdfD7I2E7g%2FVAgXzk6K%2BUZc8uEwxmBUfr0uriUWINY
# https://pdf3.savemyexams.co.uk/?get=%7B%22url%22%3A%22https%3A%2F%2Fwww.savemyexams.co.uk%2Fdp%2Fmaths_ai-hl%2Fib%2F21%2Ftopic-questions%2F4-statistics--probability%2F4-1-statistics-toolkit%2F-%2F-%2Fvery-hard%2F%22%2C%22file%22%3A%22ra8uPINb-JOzcLKR.pdf%22%2C%22bucket%22%3A%22cdn.savemyexams.co.uk%22%7D.8epNTe0XEazjE2eiG4WpE4zndVeDxg6RkVsNdFmycYI
# 其中真实有用的部分是：
# %22%3A%22GhUbxomn~ltrvBgy.pdf%22%2C%22
#          ra8uPINb-JOzcLKR.pdf
def getDownloadUrl(link):
    pattern = re.compile('file%22%3A%22(.+)%22%2C%22')
    result = pattern.findall(link)
    return result

# 下载pdf文件并且命名
def getFile(Filename_LinkDict):
    for filename,link in Filename_LinkDict.items():
        pdf = requests.get(link, headers)
        with open(filename+'.pdf', "wb") as code:
            code.write(pdf.content)
        print("Sucessful to download" + " " + filename+'.pdf')

#主程序
url ='/Users/Johnson 1/Desktop/original.html'
dowonload_res = getNamesHtml(url)
os.chdir("/Users/Johnson 1/Desktop/savemyexam") #选择目录
jg = open('全部下载链接.txt','w',encoding='utf8') #当前目录下创建全部下载链接.txt
for filename,downloadlink in dowonload_res.items():
    print(filename,downloadlink)
    jg.write(filename+':'+'\r'+downloadlink+'\r')
jg.close()
getFile(dowonload_res)
