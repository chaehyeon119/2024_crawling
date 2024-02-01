import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword = input("검색어를 입력하세요: ")


url = url  + keyword
print(url)


#개발자 도구 > 네트워크 > www.naver.com > 요청 헤더 > user-gent
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")


# 게시물별 view 구역
total_area = soup.select(".view_wrap")

rank_num= 1
for area in total_area:
    
    ad = area.select_one(".link_ad")
    if ad:
        # print("광고입니다.")
        continue
    print(f"<<<{rank_num}>>>")

    title = area.select_one(".title_area")
    name = area.select_one(".name")
    href = area.select_one(".title_link")

    print(title.text)
    print(name.text)
    # print(title["href"])
    print(href["href"])
    print()
    rank_num += 1
    