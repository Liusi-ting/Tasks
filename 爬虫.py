import requests
import re
def getHtml(url):
   try:
     r=requests.get(url)
     r.raise_for_status()
     r.encoding=r.apparent_encoding
     return r.text
   except:
     print("产生异常") 

def parsePage(List,html):
    try:
        ult = re.findall(r'\"url\"\:\".*\"',html)
        tlt = re.findall(r'\"name\"\:\".*?\"',html)
        for i in range(len(tlt)):
            URL = eval(ult[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            List.append([title,URL])
    except:
        print("解析失败")

def printList(List):
    tplt = "{:20}\t{:50}"
    print(tplt.format("名称","详情地址"))
    for j in List:
        print(tplt.format(j[0],j[1]))
    print("打印失败")
def main():
    goods= '蓝牙耳机'
    url = 'https://ai.taobao.com/search/index.htm?key='+goods
    List= []
    html= getHtml(url)
    parsePage(List,html)
    printList(List)
main()
        
