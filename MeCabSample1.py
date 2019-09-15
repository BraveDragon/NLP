# coding:"utf_8"
import MeCab

text = '今日は晴れかな？'

#天気の関連語をまとめたgazetteer
weather_set = set([u'晴れ',u'天気',u'雨'])

mecab = MeCab.Tagger("-Ochasen") #MeCabの取得
tokens = mecab.parse(text) #分かち書きを行う
token = tokens.split("\n")

#以下、分かち書き後の単語を抽出
for ele in token:
    element = ele.split("\t")
    if element[0] == "EOS":
        break
    
    # 単語の表層を取得
    surface = element[0]
    
    if surface in weather_set:
        print(surface)
