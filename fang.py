# coding:utf-8
import urllib2
import urllib
import chardet
import zlib
from bs4 import BeautifulSoup
import time
base_url = 'http://newhouse.fang.com/house/web/newhouse_sumall.php'
first_page = 1
last_page = 9
per_common_page = 12
per_last_page = 4
current_page = 1
start_time = 0
end_time = 0
my_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch'
}

def handle():
    print '===========================正在努力抓取数据中============================'
    start_time = time.time()
    for current_page in range(first_page,last_page+1):
        current_html_content = fetchHTMLSource(current_page)
        if current_html_content != None:
            soup = BeautifulSoup(current_html_content, "html.parser")
            ul = soup.select('div.listArea')[0]
            list_array = ul.select('li')
            if len (list_array) > 0:
                temp = 0
                for item_house in list_array:
                    temp += 1
                    a_array = item_house.select('div.text a')
                    span_array = item_house.select('div.price span')
                    p_a_array = item_house.select('div p.address a')
                    a_address = p_a_array[0].string
                    span_price = span_array[0].string
                    price = ' price ' + span_price 
                    address = ' address '+a_address    
                    print str((current_page-1)*per_common_page+temp) + a_array[0].string+price+address
                    if current_page == last_page:
                        if temp == per_last_page:
                            end_time = time.time()
                            total_time = end_time - start_time
                            print '===========================为您下载完毕 谢谢使用==========================='
                            print '总耗时'+str(total_time)    
        

def fetchHTMLSource(page):
    param = {
        'page':page
    }
    encode_param = urllib.urlencode(param)
    target_url = base_url+'?'+encode_param
    request = urllib2.Request(target_url)
    response = urllib2.urlopen(request)
    # 返回的数据是经过Gzip压缩过的 需要解压
    if response.info().get('Content-Encoding') == 'gzip':
        respHtml = zlib.decompress(response.read(),16+zlib.MAX_WBITS);    
        # print respHtml.decode('gb2312','ignore').encode('utf-8')
        return respHtml.decode('gb2312','ignore').encode('utf-8')


if __name__ == '__main__':
    handle()
