import opencc
from tqdm import tqdm
import os
# 创建转换器，将繁体中文转换为简体中文
converter = opencc.OpenCC('t2s.json')
# 打开输入文件和输出文件
input_path = r'E:\python\learningproject\deeplearning\word2vec-tutorial-master\wiki_texts.txt'
output_path = 'wiki_simplify.txt'
# 获取输入文件的大小（字节数）
input_size = os.path.getsize(input_path)
# 打开输入文件并读取内容
with open(input_path, 'r', encoding='utf-8') as f:
    text = f.read()
# 初始化进度条
with tqdm(total=input_size, unit='B', unit_scale=True, desc='Converting') as pbar:
    # 将文本转换为简体中文，并写入输出文件
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in text:
            simplified_line = converter.convert(line)
            f.write(simplified_line)
            pbar.update(len(line.encode('utf-8')))