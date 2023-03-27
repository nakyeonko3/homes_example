from bs4 import BeautifulSoup
from selenium import webdriver
import re


# 초기화
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
URL = "https://www.google.com/search?q=%EB%82%A0%EC%94%A8"
driver = webdriver.Chrome(
    executable_path="chromedriver", options=options
)  # 드라이버 인스턴스 생성

driver.get(url=URL)  # URL 초기화
HTML = driver.page_source
soup = BeautifulSoup(HTML, "html.parser")


SVG_TEMP_GRAPH = soup.select("#wob_gsvg > text")


def is_temp_text(element):
    """온도가 적힌 html 테그인지 확인하는 함수"""
    return (
        element["style"] == "font:bold 11px arial;text-anchor:middle"
        and element.text != ""
    )


def extract_date(text):
    """날짜만 추출하는 정규식 함수"""
    return re.search(r"\(.*", text).group()


def extract_dayoftheweek(text):
    """요일만 추출하는 정규식 함수"""
    return re.search(r"\((.*?)\)", text).group(1)


def extract_oneweektemperature():
    """일주일 온도와 날짜를 출력함"""
    for element in filter(is_temp_text, SVG_TEMP_GRAPH):
        print(f'날짜: { extract_date(element["aria-label"]) }')
        print(f"요일: { extract_dayoftheweek(element['aria-label']) }")
        print(f"온도: {element.text}")
        # print(element["style"])


extract_oneweektemperature()
driver.quit()
