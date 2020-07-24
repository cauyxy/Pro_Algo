import jieba
from pypinyin import lazy_pinyin
def CutWord(str):
    res_word=[]
    res_pinyin=[]
    str_cut=jieba.cut(str)
    str_cut={}.fromkeys(str_cut).keys()
    for word in str_cut:
        if(len(word)>=2):
            res_pinyin.append(''.join(lazy_pinyin(word)))
            res_word.append(word)

    return res_word,res_pinyin