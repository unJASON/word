#coding:utf-8
import sys,re
import json
import gc
import jieba
import jieba.analyse
import codecs
#import chardet

jieba.load_userdict("userdic.txt")  # 用户词典，自带词典不一定符合语境
default_encoding = "utf-8"
try:
    f = open('data/resource.csv', 'rb')  # 源csv文本
    line = f.readline()
    count = 0
    ct = 0

    f1 = open('stopwords.txt', 'rb')
    line1 = f1.readline()
    stopwords = line1.decode('utf-8').split(' ')
    f1.close()
    """以天为单位存储处理的数据"""
    list1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
             '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    while line:
        desc = line.decode('GBK', 'ignore').split(',')[5]
        fenci_text = jieba.cut(desc)

        final = ""
        for word in fenci_text:
            if word not in stopwords:
                final = final + " " + word
        """
        print("去除停用词后的文本：")
        print(final)
        """
        segs = jieba.analyse.extract_tags(final, topK=5)
        """
        print u"关键词:"
        print " ".join(segs)
        print " "
        print " "
        """
        # 时间格式2016/3/8  14:35:19
        # print(line.decode('GBK', 'ignore'))
        #数据图片都有逗号,应当取最后一个数组
        time = line.decode('GBK', 'ignore').split(',')[-1]
        sj = time[8:10]
        sj = ''.join(sj.split())
        while ct < 31:
            if list1[ct] == sj:
                a = 'shuju/'+sj+'.txt'
                f2 = codecs.open(a, 'a', 'utf-8')
                try:
                    f2.write(json.dumps(segs,ensure_ascii=False))
                    f2.close()
                    ct = 0
                    break
                except IOError as err:
                    print('write error')
            ct += 1
            if ct == 30:
                ct = 0
                break
        count = count + 1

        if count % 10000 == 0:
            print("current lines:", count)
        if count % 200000 == 0:
            print("GC")
            gc.collect()
        line = f.readline()
    f.close()

except IOError as err:
    print('File error:', str(err))