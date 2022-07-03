#!/usr/bin/env python
# coding: utf-8

# Yahoo Finance APIから為替価格を取得する
from pandas_datareader.data import get_quote_yahoo
import datetime

# 小数点以下を切り捨てるメソッド
def truncate(num,n):
    temp = str(num)
    for x in range(len(temp)):
        if temp[x] == '.':
            try:
                return float(temp[:x+n+1])
            except:
                return float(temp)      
    return float(temp)

# 算出したい金額
price_jp = 2000.0

# 現在の時刻を取得
dt_now = datetime.datetime.now()
dt_nowformat = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')

print(dt_now, 'における為替で', price_jp, 'をそれぞれの通貨で算出')

# 国通貨の日本円に対する為替コード
currency_dic = {'アメリカ': 'JPY=X',
                 'ユーロ': 'EURJPY=X',
                 'イギリス': 'GBPJPY=X',
                 '中国': 'CNYJPY=X',
                 'カナダ': 'CADJPY=X',
                 'オーストラリア': 'AUDJPY=X',
                 'シンガポール': 'SGDJPY=X',
                 '香港': 'HKDJPY=X',
                 'インド': 'INRJPY=X',
                 'ブラジル': 'BRLJPY=X',
                 'ロシア': 'RUBJPY=X',
                 'ニュージーランド': 'NZDJPY=X',
                 'タイ': 'THBJPY=X',
                 '韓国': 'KRWJPY=X',
                 '南アフリカ': 'ZARJPY=X',
                 'メキシコ': 'MXNJPY=X',
                 'アラブ': 'AEDJPY=X',
                 'サウジアラビア': 'SARJPY=X',
                 'ポーランド': 'PLNJPY=X',
                 '台湾': 'TWDJPY=X',
                 'スウェーデン': 'SEKJPY=X',
                 'ノルウェイ': 'NOKJPY=X',
                 'デンマーク': 'DKKJPY=X',
                 'スイス': 'CHFJPY=X',
                 'マレーシア': 'MYRJPY=X',
                 'フィリピン': 'PHPJPY=X',
                 'ベトナム': 'VNDJPY=X',
                 'インドネシア': 'IDRJPY=X',
                 'パキスタン': 'PKRJPY=X',
                 'バングラデシュ': 'BDTJPY=X',
                 'イスラエル': 'ILSJPY=X',
                 'チリ': 'CLPJPY=X',
                 'エジプト': 'EGPJPY=X',
                 'ナイジェリア': 'NGNJPY=X',
                 'アルゼンチン': 'ARSJPY=X',
                 'コロンビア': 'COPJPY=X',
               }

# リストのkey一覧を得る
country_list = list(currency_dic)

# テキストファイルを開く
f = open('output.csv', 'w')

# ヘッダーとして現在時刻を書き込む
header = str(dt_now) + ' Exchange Rate \n\n'
f.write(header)

i = 0
for country in country_list:
    print(i+1, '/', len(country_list))
    # 国ごとの為替金額をAPIから取得
    result = get_quote_yahoo(currency_dic.get(country))
    ary_result = result["price"].values
    price = ary_result[0]

    # 為替金額を指定の金額で割り、小数点以下2桁で切り捨て
    temp_price = truncate((price_jp/price), 2)
    
    # 書き込む金額
    write_price = str(temp_price)
    
    div = i % 4
    if div in {0, 1, 2}:
        write_price = write_price + ','
    else:
        write_price = write_price + '\n'
    
    f.write(write_price)
    i = i + 1

print('Done!!')
f.close()
