# coding:utf-8
import urllib2
import urllib
import zlib
import simplejson
import time
base_url = 'https://api.readhub.me/topic'
custom_header = {
   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
   'Accept-Encoding':'gzip, deflate, sdch, br',
   'Accept-Language':'zh-CN,zh;q=0.8'
}
default_page_size = 10
last_cursor = 0
isFirstRequest = True
total_count = 0;
current_count = 0
def getData():
    start_time = time.time()
    global isFirstRequest
    global last_cursor
    global total_count
    global current_count

    if isFirstRequest:
        request = urllib2.Request(base_url+'?pageSize=1',headers=custom_header)
        isFirstRequest = False
    else:
        if last_cursor != 0:
            param = {
                'lastCursor':last_cursor,
                'pageSize':default_page_size
            }
            str_param = urllib.urlencode(param)
            target_url = base_url+'?'+str_param
            request = urllib2.Request(target_url,headers=custom_header)     

    response =urllib2.urlopen(request)
    if response == None:
        print '程序出现异常 error_code == -2'
        return
    
    if response.info().get('Content-Encoding') == 'gzip':
        real_json = zlib.decompress(response.read(),16+zlib.MAX_WBITS);              
    else :
        real_json = response.read()
        
    obj_data = simplejson.loads(real_json)
    if last_cursor == 0 :
        last_cursor = obj_data.get('data')[0].get('order')
        total_count = obj_data.get('totalItems')
        current_count += 1
        print str(current_count) + '  ' + obj_data.get('data')[0].get('title')
        
    else :
         if  len (obj_data.get('data')) > 0 :
                for news in obj_data.get('data'):
                    current_count += 1
                    print str(current_count) + '  ' + news.get('title')
                    last_cursor = obj_data.get('data')[len (obj_data.get('data')) - 1].get('order')
                     
    if total_count >= current_count:
        getData()
    else:
        end_time = time.time()
        print '下载用时：' + str(end_time - start_time)
        print '============下载完成  人生苦短 我用Python============='  
        
                         
if __name__ == '__main__':
    print '正在玩命加载中...'
    getData()

     