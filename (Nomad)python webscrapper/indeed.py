import requests
from bs4 import BeautifulSoup

PAGE = 1
URL = f"https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon"
def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class":"paginate"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_indeed_toons(last_page):
    toons = []
    for page in range(last_page):
        result = requests.get(f"{URL}&page={(page+1) * PAGE}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("tr")
        for res in results:
            title = res.find("td", {"class": "title"})
            if not title is None:
                t = title.find("a").string
            date = res.find("td", {"class": "num"})
            if not date is None:
                d = date.string
            #print(f"{t},{d}")
    return toons