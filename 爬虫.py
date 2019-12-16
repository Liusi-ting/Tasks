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
        ult = re.findall(r'\"url\"\:\".*?\"',html)
        tlt = re.findall(r'\"name\"\:\".*?\"',html)
        for i in range(len(ult)):
            ur=eval(ult[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            List.append([title,ur])
def printList(List):
   try:
    tplt = "{:20}\t{:100}"
    print(tplt.format("名称","详情网址"))
    for j in List:
        print(tplt.format(j[0],j[1]))
   except:
    print("打印失败")
def main():
    url ='https://ai.taobao.com/search/index.htm?key=%E8%93%9D%E7%89%99%E8%80%B3%E6%9C%BA'
    List= []
    html= getHtml(url)
    parsePage(List,html)
    printList(List)
main()
        
        
