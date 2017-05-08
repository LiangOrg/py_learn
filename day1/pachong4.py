#!/usr/bin/python
#encoding=utf-8
import urllib2    
import urllib    
import re    
import thread    
import time    

class Spider(object):
    
    def  __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False
    
    def Start(self):
        self.enable = True
        page = self.page
        thread.start_new_thread(self.LoadPage,()) 
        while self.enable:
            if self.pages:
                nowpage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowpage,page)
                page += 1
               
    def LoadPage(self):
        while self.enable:
            if len(self.pages)<2:
                try:
                    myPage = self.GetPage(str(self.page))
                    self.pages.append(myPage)
                    self.page += 1
                except:
                    print "无法链接糗事百科"
            else:
                time.sleep(1)
                    
    def ShowPage(self,nowpage,page):
        for item in nowpage:
            print "the %d page"%(page)
            print item[0],item[1]
            myInput = raw_input()
            if myInput == "q" :
                self.enable = False
                break    
            
    def GetPage(self,page):
        url = "http://m.qiushibaike.com/hot/page/" + page 
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {"User-Agent":user_agent}
        req = urllib2.Request(url,headers = headers)
        res = urllib2.urlopen(req)
        myPage = res.read()
        unicodePage = myPage.decode("utf-8")
        
        # 找出所有class="content"的div标记    
        #re.S是任意匹配模式，也就是.可以匹配换行符    
        myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage,re.S)  
        items = []
        for i in myItems:
            items.append([i[0],i[1]])
        return items
#----------- 程序的入口处 -----------    
print u"""  
        ---------------------------------------  
            程序：糗百爬虫  
            语言：Python 2.7  
            操作：输入q
            退出阅读糗事百科  
            功能：按下回车依次浏览今日的糗百热点  
        ---------------------------------------  
        """  
             
             
print u'请按下回车浏览今日的糗百内容：'    
raw_input(' ')       
my_spider = Spider()
my_spider.Start()
