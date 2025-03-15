# -*- coding: utf-8 -*-
import logging
from gensim.corpora import WikiCorpus
def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    wiki_corpus = WikiCorpus(r"E:\python\learningproject\deeplearning\word2vec-tutorial-master\zhwiki-latest-pages-articles.xml.bz2", dictionary={})
    texts_num = 0

    with open("wiki_texts.txt",'w',encoding='utf-8') as output:
        for text in wiki_corpus.get_texts():
            output.write(' '.join(text) + '\n')
            texts_num += 1
            if texts_num % 10000 == 0:
                logging.info("已處理 %d 篇文章" % texts_num)

if __name__ == "__main__":
    main()
