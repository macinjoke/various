import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from datetime import *
import student_deploy3.get_student_deploy as get_student_deploy
from MyHomePage import settings
from utils import tweet

THIS_DIRECTORY = settings.BASE_DIR + "/student_deploy3/"
_api = tweet.api

# 　教師データ初期化
data_teacher = ['絹川', '小山', '矢島', '齊藤', '小坂', '中島', '高橋', '鉄谷', '川澄', '増田',
                '猪俣・佐々木', '岩井', '竜田', '山田', '柿崎', '森谷', '井ノ上', '学科外(系列等)', '(未定)']
X_teacher = list(data_teacher)
X_teacher[10] = '猪俣\n佐々木'
X_teacher[17] = '学科外\n(系列等)'
for i in range(13, 17):
    X_teacher[i] += '\n(2)'

# グラフ色初期化
cl_list = []
for x in range(len(data_teacher)):
    cl_list.append([1.0, 0.0, 0.0])

# グラフ色設定
cl_low = [0.2, 0.2, 1.0]  # 0~2
cl_middle = [0.2, 1.0, 0.2]  # 3~5
cl_high = [1.0, 1.0, 0.2]  # 6~8
cl_veryhigh = [1.0, 0.5, 0.2]  # 9~11
cl_outzone = [1.0, 0.2, 0.2]  # 12~

# 　フォント設定
# fp = FontProperties(fname=r'./AquaKana.ttc', size=14)
fp = FontProperties(fname=THIS_DIRECTORY + 'AquaKana.ttc', size=14)


# 　前回のログデータ
def getPrevLog(t_name):
    f = open(t_name)
    prev_html = f.read()
    prev_student_deploy_list = prev_html.split('\n')
    f.close()
    return prev_student_deploy_list


# 　htmlデータをcsvの形に変更
def parseHtml(prev_list, new_list):
    for i, line in enumerate(prev_list):
        if line.find("fi") != -1:
            new_list.append(
                str(i) + line.replace('	', '').replace('<tr><td>', ',').replace('</td><td>', ',').replace(
                    '</td></tr>', ''))


# リストの人数計算
def personNumber(p_list, y_list):
    for li in p_list:
        s = li.split(",")
        for i, t in enumerate(data_teacher):
            if s[3] == t:
                y_list[i] += 1


# 人数の差分計算
def setDiff_Y(prev_list, now_list, diff_list):
    for i, y in enumerate(now_list):
        diff_list[i] = now_list[i] - prev_list[i]


def setIncrAndDect_Y(diff_list, incr_list, decr_list):
    for i, d in enumerate(diff_list):
        if d > 0:
            incr_list[i] = d
        elif d < 0:
            decr_list[i] = -1 * d
        else:
            pass


# グラフの色を人数ごとに設定
def setGraphColor(now_list):
    for i, li in enumerate(now_list):
        # 　助教授の場合（定員２名）
        if i >= 13 and i < 17:
            if now_list[i] <= 1:
                cl_list[i] = cl_high
            elif now_list[i] == 2:
                cl_list[i] = cl_veryhigh
            elif now_list[i] > 2:
                cl_list[i] = cl_outzone
        # 教授の場合
        else:
            if now_list[i] <= 2:
                cl_list[i] = cl_low
            elif now_list[i] > 2 and now_list[i] <= 5:
                cl_list[i] = cl_middle
            elif now_list[i] > 5 and now_list[i] <= 8:
                cl_list[i] = cl_high
            elif now_list[i] > 8 and now_list[i] <= 11:
                cl_list[i] = cl_veryhigh
            else:
                cl_list[i] = cl_outzone


# グラフ描画
def drawGraph(prev_list, now_list, diff_list, incr_list, decr_list):
    # 　X軸　教師データ配列
    X = []
    for i, t in enumerate(data_teacher):
        X.append(i)
    X_teacher[len(data_teacher) - 1] = '(未定)\n' + str(now_list[len(data_teacher) - 1])

    # 　Y軸　生徒人数データ配列
    Y = []
    for i, li in enumerate(now_list):
        Y.append(now_list[i] - incr_list[i])

    # グラフ生成
    plt.figure(figsize=(15, 8))
    p1 = plt.bar(X, Y, color=cl_list, align="center")
    p2 = plt.bar(X, incr_list, bottom=Y, color=[1.0, 0.6, 0.6], align="center")
    p3 = plt.bar(X, decr_list, bottom=Y, color=[1.0, 1.0, 1.0], align="center")
    # plt.legend((p1[0], p2[0], p3[0]), ("graph", "increase", "decrease"))
    plt.legend((p2[0], p3[0]), ("increase", "decrease"))

    # 　グラフ上に数値表示
    num = 0
    for x, y in zip(X, Y):
        if diff_list[num] > 0:
            plt.text(x, y + diff_list[num], y + diff_list[num], ha='center', va='bottom')
        else:
            plt.text(x, y, y, ha='center', va='bottom')
        num += 1

    # グラフパラメータ設定
    plt.xlim(-1, len(X))
    plt.ylim(0, len(Y) + 1)
    plt.xlabel('teacher [17]')
    plt.ylabel('student [123]')
    plt.xticks(X, X_teacher, fontproperties=fp)
    plt.hlines(10, -1, len(Y), color=[1.0, 0.0, 0.0])
    plt.hlines(2, 12.6, len(Y) - 2.6, color=[1.0, 0.0, 0.0])

    # 　グラフ画像の保存
    figday = str(datetime.now()).replace("2016-", "").split(' ')[0]
    arr_time = str(datetime.now()).replace(" ", ",").replace(".", ",").split(',')[1].split(':')
    figtime = arr_time[0] + "h" + arr_time[1] + "m" + arr_time[2] + "s"
    # figname1 = "./"
    figname2 = ".png"

    # 　タイトル（日時）の作成
    # title = "=== 2016_Student_Deploy_Graph : " + figday + "(" + figtime + ") ==="
    title = "=== 2016_Student_Deploy_Graph ==="
    savename = THIS_DIRECTORY + figday + "(" + figtime + ")" + figname2
    plt.title(title)
    plt.savefig(savename)
    return savename


# 　実行時にグラフを表示する
# plt.show()

def changeValue(incr_list, decr_list):
    flag = False
    for i in incr_list:
        if i > 0:
            flag = True
    for j in decr_list:
        if j > 0:
            flag = True
    return flag


def main():
    prev_Y = []
    now_Y = []
    diff_Y = []
    incr_Y = []
    decr_Y = []
    for i in data_teacher:
        prev_Y.append(0)
        now_Y.append(0)
        diff_Y.append(0)
        incr_Y.append(0)
        decr_Y.append(0)

    # １つ前と現在のhtmlデータの入手関数
    prev_student_deploy_list = []
    student_deploy_list = []
    parseHtml(getPrevLog(THIS_DIRECTORY + 'log_student_deploy.txt'), prev_student_deploy_list)
    parseHtml(get_student_deploy.get_html(), student_deploy_list)

    # 　応募人数計算関数
    personNumber(prev_student_deploy_list, prev_Y)
    personNumber(student_deploy_list, now_Y)

    # 　１つ前と現在の差計算関数
    setDiff_Y(prev_Y, now_Y, diff_Y)
    setIncrAndDect_Y(diff_Y, incr_Y, decr_Y)

    # 　前回の数値が変化したか
    flag = changeValue(incr_Y, decr_Y)
    # print(flag)
    if flag == True:
        # 　各リストのデバッグ
        print("pre_person :", prev_Y)
        print("now_person :", now_Y)
        print("----> incr :", incr_Y)
        print("----> decr :", decr_Y)
        # 　グラフの色設定関数
        setGraphColor(now_Y)
        # 　グラフ描画関数
        savename = drawGraph(prev_Y, now_Y, diff_Y, incr_Y, decr_Y)
        tweet(savename)
    else:
        print("====>( No Change Value )")
    return


# 画像ツイート
def tweet(filename):
    import datetime
    tweet_text = "途中経過" + str(datetime.datetime.now() + datetime.timedelta(hours=9))
    media_id = _api.UploadMediaSimple(filename)
    _api.PostUpdate(tweet_text, media=media_id)


# 　メイン関数
if __name__ == "__main__":
    main()
