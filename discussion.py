import requests
from bs4 import BeautifulSoup
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
    for snum in range(0,2600,100):
        params = {'start': str(snum)}
        demo+=getUrl(url,params)
    return demo

def getInfo(demo):
    ls=[]
    count=0
    content=BeautifulSoup(demo, 'html.parser')
    reply_ls=content('li',attrs={'class': 'clearfix comment-item reply-item '})
    for reply in reply_ls:
        count+=1
        try:
            ls.append('\n第' + str(count) + '楼')
            quote=reply('span',attrs={'class':'all'})[0].text
            if(len(quote)<=45):
                ls.append('--回复：'+quote+'--')
            else:
                ls.append('--回复：' + quote[:45] + '...--')
        except:
            pass
        ls.append(reply('p')[0].text)
        print('\r当前进度{:2f}%'.format(count * 100 / 2600), end='')
    return ls

def writeText(data, path):
    #按需打印
    with open(path, 'a', encoding='utf-8') as f:
        f.write('Title Name）'+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+'\n')
        for item in data:
            f.write(item+'\n')


path='your_file.txt'
demo=getText('https://www.douban.com/group/topic/#########/')
data=getInfo(demo)
writeText(data,path)
