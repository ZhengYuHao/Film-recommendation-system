'''
Created on 2018年6月5日

@author: Administrator
'''
# coding:utf-8  
import urllib3
import urllib
from bs4 import  BeautifulSoup
import re
import requests
import os
class data_net():
    def main_func(self):
        fname_1=open('电影名.txt','r')
#         print(fname_1)
        i=0
        for line in fname_1.readlines():
            if i<=185:
                i+=1
                print(i)
                continue
            print(i)   
            i+=1
#                 continue
            
            line=line.replace(":","")
            line=line.replace("*","")
            line=line.replace("?","")
            line=line.replace("&","")
            line=line.replace("/","")
            line=line.strip("\n").strip(")").split(",")
            
            if len(line)>=2:
                term=line[0]
                line[0]=line[1]
                line[1]=term
            line=''.join(line)
#             print(type(line))
#             print(line.strip("\n").strip(" "))
            try:
                self.keyword =line.strip("\n").strip(" ").strip(")") #title # 关键词, 改为你想输入的词即可  
                url_init_first = 'https://en.wikipedia.org/wiki/'
                url_init=url_init_first+self.keyword
                req = urllib.request.Request(url_init)
                with urllib.request.urlopen(req) as response:
                   the_page = response.read()
                soup=BeautifulSoup(the_page,'lxml')
#                 print(soup.p.get_text())
#                
                the_page=the_page.decode('utf-8')              
                fname=open("user/"+self.keyword+'.txt','w+')
                fname.write(soup.p.get_text())
                fname.close()
            except Exception as e:
                print(e)
                fname=open("user/"+self.keyword+'.txt','w+')
                fname.write("because of some error,we cannot offer anyinformation!")
                fname.close()
                continue
#             self.get_image()
        
         #以下三个函数用于爬取相关电影的图片
    def get_onepage_urls(self,onepageurl):  
        if not onepageurl:    
            return [], ''  
        try:  
            html = requests.get(onepageurl).text  
        except Exception as e:  
            print(e)  
            pic_urls = []  
            fanye_url = ''  
            return pic_urls, fanye_url  
        pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)  
        fanye_urls = re.findall(re.compile(r'<a href="(.*)" class="n">下一页</a>'), html, flags=0)  
        fanye_url = 'http://image.baidu.com' + fanye_urls[0] if fanye_urls else ''  
        return pic_urls, fanye_url  
    def down_pic(self,pic_urls,localPath):  
        if not os.path.exists(localPath):  # 新建文件夹  
            os.mkdir(localPath)  
        """给出图片链接列表, 下载图片"""  
        for i, pic_url in enumerate(pic_urls):  
            try:  
                pic = requests.get(pic_url, timeout=15)  
                string = str(i + 1) + '.jpg'  
                with open(localPath + '%s.jpg' %self.keyword, 'wb')as f:  
                    f.write(pic.content)  
                    if i==1:
                        break
            except Exception as e:  
                continue  
    def get_image(self):
 # 关键词, 改为你想输入的词即可  
        url_init_first = r'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1497491098685_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1497491098685%5E00_1519X735&word='  
        url_init = url_init_first + urllib.parse.quote(self.keyword, safe='/')  
        all_pic_urls = []  
        onepage_urls, fanye_url = self.get_onepage_urls(url_init)  
        all_pic_urls.extend(onepage_urls)  
        fanye_count = 1  # 图片所在页数，下载完后调整这里就行  
        while 1:  
            onepage_urls, fanye_url = self.get_onepage_urls(fanye_url)  
            fanye_count += 1  
            if fanye_url == '' and onepage_urls == []:  
                break  
            all_pic_urls.extend(onepage_urls)  
        self.down_pic(list(set(all_pic_urls)),'image/')#保存位置也可以修改
    #以上三个函数用于爬取相关电影的图片   
        
a=data_net()
a.main_func()