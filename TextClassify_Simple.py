import MeCab

#天気の関連語をまとめたgazetteer
weather_set = set(['晴れ','天気','雨','曇り'])

#ナビゲーションの関連語をまとめたgazetteer
navi_set = set(['渋谷','東京','電車','地図'])

mecab = MeCab.Tagger("-Ochasen") #MeCabの取得

def classify_category(text):
    tokens = mecab.parse(text) #分かち書きを行う
    token = tokens.split("\n")
    weather_score = 0 #天気である可能性のスコア
    navi_score = 0 #ナビゲーションである可能性のスコア

    #以下、分かち書き後の単語を抽出
    for ele in token:
        element = ele.split("\t")
        if element[0] == "EOS":
            break
    
        # 単語の表層を取得
        surface = element[0]
    
        if surface in weather_set:
            weather_score += 1
        if surface in navi_set:
            navi_score += 1
    
    if weather_score > navi_score:
        print("天気")
    else:
        print("ナビゲーション")

text = "ここから東京までは何分？"
classify_category(text)
