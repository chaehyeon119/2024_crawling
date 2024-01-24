import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword = input("검색어를 입력하세요")


url = url  + keyword
print(url)


#개발자 도구 > 네트워크 > www.naver.com > 요청 헤더 > user-gent
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
req = requests.get(url, headers=headers)


print(req.request.headers)

# print(req.raise_for_status)
# print(dir(req))
# print(dir(req.request.headers))

#네이버의 html이 출력됨
html = req.text

#print(html)

#BeautifulSoup이라는 클래스를 사용해 html을 html.parser라는 것으로 분석을 한 것을 soup으로 부르겠다.
soup = BeautifulSoup(html, "html.parser")

# 클래스는 앞에 .을 붙이고, id는 앞에 #을 붙임
logo = soup.select_one(".imgsvg ico_naver")

# 24.01.23. 현재 기준으로는 네이버 로고가 사라져서 none으로 뜸
#
#print(logo)

#클래스니까 점 붙이기
result = soup.select(".title_link _cross_trigger")
 
