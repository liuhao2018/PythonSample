# coding:utf-8
import urllib2
import urllib
import zlib
from bs4 import BeautifulSoup
import re

# singer_artist_id = ['12977','11679','711683','5770','3681',
# '6731','5073','7122','1007170','8103','11370']
singer_artist_id = ['3681']
music_id = []

base_url = 'https://music.163.com'
global_headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
    +'(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Cookie':'vjuids=-1244cdd2f.15c0be1715f.0.385b52723cc2d; _ntes_nnid=acc75e002e736303'
    +'f180aa351ad817a3,1494847943155; _ntes_nuid=acc75e002e736303f180aa351ad817a3; P_IN'
    +'FO=m13659840537@163.com|1496547833|0|other|00&99|tij&1496329983&mail163#nmg&null#10#0#0'
    +'|136537&1|mail163|13659840537@163.com; UM_distinctid=15c82483b7146d-0d984ad7a4b8d5-474f0'
    +'820-100200-15c82483b7280c; vjlast=1494847943.1496834393.13; vinfo_n_f_l_n3=4510820c0d14a'
    +'fdf.1.1.1494847943166.1494847991915.1496834396619; playerid=25951319; __utma=94650624.'
    +'1926082313.1499553169.1499553169.1499585726.2; __utmb=94650624.70.10.1499585726; __utmc'
    +'=94650624; __utmz=94650624.1499553169.1.1.utmcsr=blog.csdn.net|utmccn=(referral)|utmcmd'
    +'=referral|utmcct=/magictong/article/details/4464024; JSESSIONID-WYYY=ea%2BQy7MmIjkafOIqFQn9'
    +'ykQO8hJRbd3Y7WUrkGYNCFu9c7wgIvkIxycvS4OxhkRWvHKgSaMmykceHaK3rypWMMeuo3gy2wfI04utOuR1c7cdcGsqSV'
    +'MPRUasR7IR4X4yapKndJtRzDGWHtQDzsu1NAWhceJbTPDg9okYIcT7w9xIsA0q%3A1499592747886; _iuqxldmzr_=32',
    'Connection':'keep-alive',
    'Referer': 'https://music.163.com',
    'Host': 'music.163.com'
}
def getMusicList():
    """ 
    获取所有歌曲的基本信息 对应的url
    """
    for id in singer_artist_id:
        target_url = base_url + '/artist?id='+ id 
        print '=====================' + target_url +'======================='
        request = urllib2.Request(target_url,headers=global_headers)
        response = urllib2.urlopen(request)
        if response.code == 200:
            if response.info().get('Content-Encoding') == 'gzip':
                result = zlib.decompress(response.read(),16+zlib.MAX_WBITS)
                soup = BeautifulSoup(result,'html.parser')
                ul_array = soup.select('ul.f-hide')
                if len (ul_array) > 0:
                    ul = ul_array[0]
                    a_array = ul.select('li a')
                    if len (a_array) > 0 :
                        for i in range(0,len(a_array)):
                           music_item_id = str(a_array[i]['href'][9:]) 
                           music_id.append(music_item_id)
                    if len (music_id) > 0 :       
                        for id in music_id:
                             music_url = 'http://music.163.com/api/song/lyric?'+'id='+str(id)+'&lv=1&kv=1&tv=-1'
                             print urllib2.urlopen(music_url).read()  
            else:
               result = response.read()
               print result
        else:
            print 'error '    

if __name__ == '__main__':
    getMusicList()

# pat = re.compile(r'\[.*\]')
# lrc = re.sub(pat,"",lrc)
# lrc = lrc.strip

# print lrc

# url = 'http://music.163.com/api/song/lyric?'+'id='+str(111)+'&lv=1&kv=1&tv=-1'