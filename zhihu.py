# coding:utf-8

import requests
import re
from lxml import html

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'Cookie': 'xxxxx' #你的cookie
    'Connection': 'keep-alive'
}

k = 0
for page in range(5):
    url = 'https://www.zhihu.com/topic/19776749/top-answers?page={}'.format(page+1)
    result = requests.get(url, headers=headers).content
    # print result
    sel = html.fromstring(result)
    title = sel.xpath('//div[@class="content"]')
    print 'top{}-{}:'.format(20*page+1, 20*page+20)
    for i in title:
        title = i.xpath('h2/a/text()')[0]
        link = i.xpath('h2/a/@href')[0]
        zan = i.xpath('div[1]/div[1]/a/text()')[0]
        url = 'https://www.zhihu.com' + link

        if i.xpath('div[1]/div[3]/span/span/a/text()'):
            author = i.xpath('div[1]/div[3]/span/span/a/text()')[0]
        else:
            author = u'匿名用户'
        print u"{} {} [{}]({}) ".format(zan, author, title, url)
        k += 1
    print '\n'

print '共%s ' % k
