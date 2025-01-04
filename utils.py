import re
def get_word_dict(path):
    #定义变量
    max_L = 0
    out=[]
    #ⅰ打开文本文档
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        match = re.search(r'\d', line)
        cleaned_line = line[:match.start()-1]
        out.append(cleaned_line)
        if len(cleaned_line) > max_L:
            max_L=len(cleaned_line)

    #ⅳ返回结果
    out=tuple(out)
    return [out,max_L]


def get_sentences(path):
    sentence=[]
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        cleaned_line = line.strip()
        cleaned_line = cleaned_line.replace(' ', '')  # 去除空格
        sentence.append(cleaned_line)
    return sentence



def get_result_splited(path,splitsign='  '):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    cleaned_lines = []
    for line in lines:
        cleaned_line = line.strip()
        segments = cleaned_line.split('  ')  # 两个空格作为分割符
        cleaned_lines.append(segments)
    return cleaned_lines
