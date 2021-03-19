import requests
from bs4 import BeautifulSoup

custom_header = {
    'referer' : "http://www.naver.com",
    
    
}

for num in range(950, 955):
    url = "https://search.daum.net/search?w=tot&DA=LOT&rtmaxcoll=LOT&&q="+str(num)+"회차%로또"
    req = requests.get(url)

    if req.status_code == requests.codes.ok:
        html = BeautifulSoup(req.text, "html.parser")
        numbers = html.select("div.lottonum , img_lotto")
        for number in numbers [ :6]:
            print(number.text, end = " ")

else:
    print("접속 실패")
