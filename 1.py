import gensim
from gensim.models import Word2Vec
# 加载预训练的 Word2Vec 模型
model = Word2Vec.load(r'E:\python\learningproject\deeplearning\word2vec-tutorial-master\word2vec.model')
# 计算两个词语的相似度
word1 = '国土局'
word2 = '卫生局'
similarity = model.wv.similarity(word1, word2)

print(f"“{word1}”和“{word2}”的相似度为：{similarity:.2f}")