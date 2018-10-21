from gensim.models import word2vec

import logging

# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# sentences = word2vec.Text8Corpus("text8/text8")  # 加载语料
sentences = word2vec.Text8Corpus("test_after.txt")  # 加载语料
model = word2vec.Word2Vec(sentences, size=200)  # 训练skip-gram模型; 默认window=5

# 计算两个词的相似度/相关程度
y1 = model.similarity("詹姆斯", "韦德")
print ("相似度为："+ str(y1))
print ("--------\n")
y2 = model.most_similar("詹姆斯", topn=20)  # 20个最相关的
print("最相关的词有:")
for item in y2:
    print (item[0], item[1])
