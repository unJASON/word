from gensim.models import word2vec

import logging

# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# sentences = word2vec.Text8Corpus("text8/text8")  # 加载语料
sentences = word2vec.Text8Corpus("shuju/test_after.txt")  # 加载语料
model = word2vec.Word2Vec(sentences, size=200)  # 训练skip-gram模型; 默认window=5
s1 = "成龙"
s2 = "吴京"
# 计算两个词的相似度/相关程度
y1 = model.similarity(s1, s2)
print (s1+","+s2+"相似度为："+ str(1-y1))
print ("--------\n")
y2 = model.most_similar(s1, topn=20)  # 20个最相关的
print("与"+s1+"最相关的20个词:")
for item in y2:
    print (item[0], 1-item[1])
