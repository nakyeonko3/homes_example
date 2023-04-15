import requests
from bs4 import BeautifulSoup


URL = "https://dormitory.kangwon.ac.kr/bbs/board.php?bo_table=2_7"


def fetcher(url):
    with requests.get(url) as response:
        return response.text


HTML_TEXT = fetcher(URL)
soup = BeautifulSoup(HTML_TEXT, "html.parser")
# print(soup.prettify())

print(soup.select(" #sub_content > div > div > div > table > tbody > tr"))
