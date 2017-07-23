# coding:utf-8
import jieba
import jieba.analyse
def analyse():
    content = open('Readhub.md').read()
    tags = jieba.analyse.extract_tags(content,topK=100)
    print '  '.join(tags)
if __name__ == '__main__':
    analyse()