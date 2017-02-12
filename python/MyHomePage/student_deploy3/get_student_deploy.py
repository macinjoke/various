import urllib.request
from MyHomePage import settings

THIS_DIRECTORY = settings.BASE_DIR + "/student_deploy3/"

def get_html():
    url = 'https://www.mlab.im.dendai.ac.jp/bthesis2017/StudentDeploy.jsp?displayOrder=2'
    payload = {
        'id': '14fi099',
        'code': 'shsh0528',
        'func': 'authByRadius'
    }
    data = urllib.parse.urlencode(payload)
    binary_data = data.encode('ascii')
    text = []
    req = urllib.request.Request(url, binary_data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        text = page.decode("utf-8").split("\n")
    student_deploy_list = []
    strlist = ""
    for i in text:
        if i.find("<tr><td>") != -1 and i.find("テストユーザ") == -1:
            student_deploy_list.append(i)
            strlist += i
            strlist += '\n'
    f = open(THIS_DIRECTORY + "log_student_deploy.txt", "w", encoding="utf-8")
    f.write(strlist)
    f.close()

    return student_deploy_list
