import utils
import re

sentence = utils.get_sentences('cbfc_test.txt')
# 只有一句
dict_words = utils.get_word_dict('dict.txt')[0]
max_length = utils.get_word_dict('dict.txt')[1]
sentence = sentence[0]

def FMM(sentence):
    segment = []
    start = len(sentence)
    end = max(start - max_length, 0)
    while start > 0:
        now = sentence[end:start]
        if now in dict_words or len(now) == 1:
            segment.append(now)  # 匹配成功
            start = end
            end = max(start - max_length, 0)
        else:
            end += 1
            if end >= start:
                segment.append(now)  # 未匹配成功，将单个字符作为一个词
                start -= 1
                end = max(start - max_length, 0)

    segment.reverse()  # 翻转分词结果
    return segment
