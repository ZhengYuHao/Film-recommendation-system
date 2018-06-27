'''
Created on 2018年6月5日

@author: Administrator
'''
import requests
import re
import os
import urllib
import re  
import sys  
import urllib  
import os  
  
import requests  
  
class image_get():
    def get_onepage_urls(self,onepageurl):  
        if not onepageurl:  
            print('执行结束')  
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
                with open(localPath + '%s.jpg' %self.key, 'wb')as f:  
                    f.write(pic.content)  
              #  with open(string, 'wb') as f:  
              #      f.write(pic.content)  
                    print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))  
                    break
            except Exception as e:  
                print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))  
                print(e)  
                continue  
      
      
    def main(self):  
        
        fname_1=open('电影名.txt','r')
        for line in fname_1.readlines():
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
            keyword =line.strip("\n").strip(" ").strip(")") # 关键词, 改为你想输入的词即可  
            print(keyword)
            self.key=keyword
            keyword=keyword+"海报"
            url_init_first = r'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1497491098685_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1497491098685%5E00_1519X735&word='  
            url_init = url_init_first + urllib.parse.quote(keyword, safe='/')  
            all_pic_urls = []  
            onepage_urls, fanye_url = self.get_onepage_urls(url_init)  
            all_pic_urls.extend(onepage_urls)  
          
            fanye_count = 0  # 图片所在页数，下载完后调整这里就行  
            while 1:  
                onepage_urls, fanye_url = self.get_onepage_urls(fanye_url)  
                fanye_count += 1  
                print('第%s页' % fanye_count)  
                if fanye_url == '' and onepage_urls == []:  
                    break  
                all_pic_urls.extend(onepage_urls)  
          
            self.down_pic(list(set(all_pic_urls)),'F:/PythonPic/' )#保存位置也可以修改  
a=image_get()
a.main()