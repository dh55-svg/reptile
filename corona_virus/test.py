import urllib.request
import urllib.parse
import urllib.error
import re
from bs4 import BeautifulSoup
import json
import xlwt
def main():
    baseurl="https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&page="
    datalist=getData(baseurl)
    # print(datalist)
    savepath="C:\\Users\\dell\\Desktop\\Image\\iphone.xls"
    # saveData(datalist,savepath)
    # askUrl(baseurl)

findLink=re.compile(r"<em>(.*)</em>")  #创建正则表达式对象，表示规则（字符串的模式）
#爬取页面
def getData(baseurl):
    datalist=[]
    for i in range(0,1):
        url=baseurl+str(2*i-1)+"&s=1&click=0"
        html=askUrl(url)
    #逐一解析页面
        soup=BeautifulSoup(html,"lxml")
        for item in soup.find_all("div",class_="p-name p-name-type-2"):
            data=[]#保存手机的所有信息
            link=item.get_text()
            # link.replace("\n","")
            link.rstrip('\n')
            link.lstrip('\n')
            print(link)
            data.append(link)
            datalist.append(data)

    return datalist
# 得到指定的URL的页面内容
def askUrl(url):
    head={"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
# 保存到excel中
def saveData(datalist,savepath):
    data=[]
    workbook=xlwt.Workbook(encoding="utf8")
    sheet=workbook.add_sheet("手机销量")
    col=("手机名","评论数")
    # 列名添加
    for i in range(0,2):
        sheet.write(0,i,col[i])
    # 元素添加
    for i in range(0,30):
        data.append(datalist[i])
    # print(data)
    for j in range(0,1):
        for i in range(len(data)):
            sheet.write(i+1,j,data[i])
    workbook.save(savepath)
if __name__ == '__main__':
    main()