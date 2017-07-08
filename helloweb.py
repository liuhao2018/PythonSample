# -*- coding: utf-8 -*-
# @Author: liuhao
# @Date:   2017-03-18 16:30:25
# @Last Modified by:   liuhao
# @Last Modified time: 2017-03-18 22:56:59
import web
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        return 'hello webpy'

if __name__ == "__main__":
    app.run()
