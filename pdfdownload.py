import re
import os
import requests
import string
from tqdm import tqdm

headers = headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"}

def getFile(url):
    file_name = url.split('/')[-1]
    pdf = requests.get(url, headers)
    with open(file_name, "wb") as code:
        code.write(pdf.content)
    print("Sucessful to download" + " " + file_name)

def getFile2(url):
	r = requests.get(url, headers, stream=True)
	filename = url.split('/')[-1]
	total_size = int(r.headers.get('content-length', 0))
	#Printing Total size in Bytes
	print(total_size)
	with open(local_filename, 'wb') as f:
    	for data in tqdm(r.iter_content(chunk_size = 512), total=total_size, unit='B', unit_scale=True):
        	f.write(data)
    print("成功下载pdf")



book_url = str(input("请复制包含有pdf的链接"))
getFile(book_url)