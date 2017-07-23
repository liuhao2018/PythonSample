
# coding:utf-8
import json
import requests
import time
current_page = 0;
end_page = 100
base_url = 'https://club.jd.com/comment/productPageComments.action?productId=3867555&score=0&sortType=5&pageSize=10&isShadowSku=0&rid=0&fold=1'
custom_header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Cookie':'TrackID=1tZQPZprEeMnQAs2UupqrhskTeQ6veeQw7p_mwNuHR_scD1E1LE1pvI9rTCyUYGbjMckghzFFQ8sQQ02H97WumEGZqfppLGXyz1UZ1TrGu55JDzin4Bin7LmAgzgNixVk; pinId=tqSDXi4Wz7jtMjzhrVXbUw; unpl=V2_ZzNtbUADRUYhDUIBf0tVBWJUR10RVRNFJgpFV3gRX1ZlVxoKclRCFXMUR1NnGlQUZwcZX0ZcQxRFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2V3oeWwxmARVVSmdzEkU4dlR9G1kDYTMTbUNnAUEpC0BQcx9USGQCFVpLVkESfQB2VUsa; __jdv=122270672|baidu|-|organic|not set; ipLoc-djd=1-72-2799-0; __jda=122270672.2066803699.1469756424.1498721740.1499838848.19; __jdb=122270672.9.2066803699|19.1499838848; __jdc=122270672; 3AB9D23F7A4B3C9B=3F52EDASMTDIDSLSXWIOQZYH3ZAZLUZHQZTT56LGRBAHRNIKIY77GW2AXXX5KPAIKHT72LTAAVMBNJNK2SU764UUXM; __jdu=2066803699'
}
def fetchCommentJSON():
    global current_page
    current_page += 1
    if current_page < end_page:
        print current_page
        target_url = base_url+'&page='+str(current_page)
        response = requests.get(target_url,headers = custom_header)
        if response.status_code == 200:
            result = response.text
            try:
                goods = json.loads(result.encode('utf-8'))
                if len (goods['comments']) > 0:
                    for comment in goods['comments']:
                        print comment['content']
            except ValueError:
                print 'error'

        time.sleep(1)            
        fetchCommentJSON()        

if __name__== '__main__':
    fetchCommentJSON()