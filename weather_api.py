import requests
from bs4 import BeautifulSoup
def getTemp():
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hRtnPlp0J14ssSxI7E4ssssstso-403575"
    response=requests.get(url)

    naver_html = response.text
    soup = BeautifulSoup(naver_html,'html.parser')

    temp= soup.select_one(".todaytemp")
    return temp.text

