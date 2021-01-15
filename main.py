# -*- coding: utf-8 -*
print("\n")
import sys
sys.path.append("modules")
import loading_bar as ld_b
ld_b.create_bar(bar_width=40,bar_text='Loading：')
ld_b.load(write_num=10)

import re
import signal
ld_b.load(write_num=10)
import requests
from bs4 import BeautifulSoup as soup
ld_b.load(write_num=10)

url1='tw.news.yahoo.com'
url2='search'
url='https://'+url1+"/"+url2

def exit(signum, frame):
    print('\n 爬蟲被終止！ \n')
    sys.exit()
signal.signal(signal.SIGINT, exit)
signal.signal(signal.SIGTERM, exit)

ld_b.load(write_num=10)
ld_b.end_bar()

while 1:
	print("載入成功！\n提醒: 可以使用\"Ctrl+C\"退出爬蟲程序\n")
	while True:
	# 定義參數
		keyword=input("搜尋關鍵字：")
		ld_b.create_bar(bar_width=40,bar_text='Searching：')
		req_params={"p":keyword}
		ld_b.load(write_num=10)
		req_headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Debian Chromium/79.0.3945.79 Chrome/79.0.3945.79 Safari/537.36"}
		ld_b.load(write_num=20)
	# 請求
		req=requests.get(url,headers=req_headers,params=req_params,timeout=10)
		ld_b.load(write_num=10)
		ld_b.end_bar()
		print("\n")
	# 檢查回應
		print("HOST => HTTP: "+req.url)
		if req.status_code!=requests.codes.ok:
			print("HTTP 回應失敗！ ("+str(req.status_code)+")")
			break
		print("HOST <= HTTP: "+str(req.status_code))
		req.encoding='utf-8'
		print("\n")
	# 解析&輸出
		req=soup(req.text,"html.parser")
		datas=req.select("div.Ov(h).Pend(44px).Pstart(25px) a")
		contents=req.select("div.Ov(h).Pend(44px).Pstart(25px) p")
		i=0
		for data in datas:
			#pt_url=fdt.find("a").get("href")
			# print('網址：'+pt_url)
			print("("+str(i)+") "+data.text+"\n")
			i+=1
		while len(datas)>0:
			whatisthisurl=input("輸入編號獲取詳細資訊(或Enter跳過)：")
			whatisthisurl=whatisthisurl.replace(" ","")
			pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
			result = pattern.match(whatisthisurl)

			if whatisthisurl=='':
				break
			elif not result:
				continue
			elif int(whatisthisurl)>len(datas)-1 or int(whatisthisurl)<0:
				continue
			else:
				print("內容: "+contents[int(whatisthisurl)].text+"\n網址: https://"+url1+"/"+url2+datas[int(whatisthisurl)]["href"]+"\n")
		