# coding:utf-8

import requests
import re
from lxml import html

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'Cookie': 'd_c0="ABACW_WGFguPTlTHXZbuMeL8nupkFPj-4Yk=|1483270334"; _zap=158ff443-d491-40fd-84bf-980f803839d3; aliyungf_tc=AQAAAEvweA+RjA0AQtsiecJWG8NHBj+R; s-t=autocomplete; q_c1=ac198176efaa4b2e8988d8719222627e|1486039590000|1483270332000; _xsrf=eddd49ef164f48d204422af1192fbbb4; r_cap_id="NzVmMWQxZTA3OWZmNDE3MGJmY2VmOTIwNjEyN2E5MjQ=|1487036128|3a09d1f3e8137d05d0cd243be53485f135b7a2a5"; login="NDYyMjY0NDJmYzExNDc0NDllMGEwYjlhYTMxZDQwYmQ=|1487042981|55b01bcb95933242c7efac91ccdfa4efa6971f50"; l_cap_id="MmI5MTI1OThjYTE1NGE1NGI1OTIwNDJiZGM1ZDNkNTA=|1487142508|4e81b724cc726915f88e2ec1668068815a693e5e"; cap_id="Mjc3ODFiN2I5YmEyNDczNjg4Mzk3MTJkNjk3YWE0M2M=|1487142508|f6476fd269b094d771f5897cc9f9adc76279b7d7"; n_c=1; s-q=%E6%8B%89%E5%8B%BE%E7%88%AC%E8%99%AB; s-i=19; sid=a4s7n4bs; z_c0=Mi4wQUFBQTFqTWRBQUFBRUFKYjlZWVdDeGNBQUFCaEFsVk5pWXZMV0FBQldtR2p6a1JaZUpYVXFFSEU4aGtpN2tVVjNR|1487913012|581aebec7ae75f9574e61eba7473cd9800e76f67; nweb_qa=heifetz; __utma=51854390.909385150.1487847492.1487847492.1487913015.2; __utmb=51854390.0.10.1487913015; __utmc=51854390; __utmz=51854390.1487913015.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20130818=1^3=entry_date=20130818=1',
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