import requests
import re
import time

hd = {'user-agent': 'Mozilla/5.0'}

def getUrl(url,params):
    try:
        r=requests.get(url, headers=hd, params=params)
        r.raise_for_status()
        r.encoding='UTF-8'
        return r.text
    except:
        print('Error!')

def getText(url):
    demo=''
    for snum in range(0,200,25):
        params = {'start': str(snum)}
        demo+=getUrl(url,params)
    return demo

def getInfo(demo):
    mat = [['' for i in range(2)] for j in range(240)]
    pat=re.compile(r'title=".+" class=""')
    pat2=re.compile(r'class="r-count ">\d+')
    i=0
    for title in pat.finditer(demo):
        mat[i][0]=title.group(0)[7:-10]
        i+=1
    j=0
    for number in pat2.finditer(demo):
        mat[j][1]=number.group(0)[17:]
        j+=1
    return mat

def printData(data, num):
    #按需打印
    print('豆瓣XX小组最新贴子'+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    tplt='{0:^4}\t{1:{3}^60}\t{2:{4}^5}'
    print(tplt.format('编号', '讨论标题', '回复数', chr(12288),chr(12288)))
    for i in range(num):
        print(tplt.format(i, data[i][0],data[i][1],chr(12288),chr(12288)))

demo=getText('https://www.douban.com/group/######/discussion')
data=getInfo(demo)
printData(data,240)
