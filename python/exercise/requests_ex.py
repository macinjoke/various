import requests
from pprint import pprint

r = requests.get(
    'http://api-atcolor.cps.im.dendai.ac.jp/v1/q/7',
    headers={'Authorization': '42:a6T83FjQKkKxrKySsexk'},
    data={'page': 2},
    params={}
)

print('STATUS CODE: ' + str(r.status_code))
print('HEADERS: ' + str(r.headers))
print('DATA: ')
pprint(r.json())


