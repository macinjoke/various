#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *****************************************************************************************
# ぐるなびWebサービスのレストラン検索APIで緯度経度検索を実行しパースするプログラム
# 注意：ここでは緯度と経度の値は固定でいれています。
# 　　　APIアクセスキーの値にはユーザ登録で取得したものを入れてください。
# *****************************************************************************************
import sys
import urllib.request, urllib.parse, urllib.error
import json


####
# 変数の型が文字列かどうかチェック
####
def is_str(data=None):
    if isinstance(data, str) or isinstance(data, str):
        return True
    else:
        return False


####
# 初期値設定
####
# APIアクセスキー
keyid = "97b6539681e1256aaeee812d954d654b"
# エンドポイントURL
url = "http://api.gnavi.co.jp/RestSearchAPI/20150630/"
# 緯度・経度、範囲を変数に入れる
# 緯度経度は日本測地系で日比谷シャンテのもの。範囲はrange=1で300m以内を指定している。
# 緯度
latitude = "35.670083"
# 経度
longitude = "139.763267"
# 範囲
range = "1"

####
# APIアクセス
####
# URLに続けて入れるパラメータを組立
query = [
    ("format", "json"),
    ("keyid", keyid),
    ("latitude", latitude),
    ("longitude", longitude),
    ("range", range)
]
# URL生成
url += "?{0}".format(urllib.parse.urlencode(query))
# API実行
try:
    result = urllib.request.urlopen(url).read()

except ValueError:
    print("APIアクセスに失敗しました。")
    sys.exit()

####
# 取得した結果を解析
####
data = json.loads(result.decode('utf-8'))

# エラーの場合
if "error" in data:
    if "message" in data:
        print("{0}".format(data["message"]))
    else:
        print("データ取得に失敗しました。")
    sys.exit()

# ヒット件数取得
total_hit_count = None
if "total_hit_count" in data:
    total_hit_count = int(data["total_hit_count"])


# ヒット件数が0以下、または、ヒット件数がなかったら終了
if total_hit_count is None or total_hit_count <= 0:
    print("指定した内容ではヒットしませんでした。")
    sys.exit()

# レストランデータがなかったら終了
if not "rest" in data:
    print("レストランデータが見つからなかったため終了します。")
    sys.exit()

# ヒット件数表示
print("{0}件ヒットしました。".format(total_hit_count))
print("----")

# 出力件数
disp_count = 0

# レストランデータ取得
for rest in data["rest"]:
    line = []
    id = ""
    name = ""
    access_line = ""
    access_station = ""
    access_walk = ""
    code_category_name_s = []
    # 店舗番号
    if "id" in rest and is_str(rest["id"]):
        id = rest["id"]
    line.append(id)
    # 店舗名
    if "name" in rest and is_str(rest["name"]):
        name = "{0}".format(rest["name"])
    line.append(name)
    if "access" in rest:
        access = rest["access"]
        # 最寄の路線
        if "line" in access and is_str(access["line"]):
            access_line = "{0}".format(access["line"])
        # 最寄の駅
        if "station" in access and is_str(access["station"]):
            access_station = "{0}".format(access["station"])
        # 最寄駅から店までの時間
        if "walk" in access and is_str(access["walk"]):
            access_walk = "{0}分".format(access["walk"])
    line.extend([access_line, access_station, access_walk])
    # 店舗の小業態
    if "code" in rest and "category_name_s" in rest["code"]:
        for category_name_s in rest["code"]["category_name_s"]:
            if is_str(category_name_s):
                code_category_name_s.append("{0}".format(category_name_s))
    line.extend(code_category_name_s)
    # タブ区切りで出力
    print("\t".join(line))
    disp_count += 1

# 出力件数を表示して終了
print("----")
print("{0}件出力しました。".format(disp_count))
sys.exit()
