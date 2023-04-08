from bs4 import BeautifulSoup
from selenium import webdriver

# 초기화
URL = "https://www.google.com/search?q=%EB%82%A0%EC%94%A8"
driver = webdriver.Chrome(executable_path="chromedriver")  # 드라이버 인스턴스 생성
driver.get(url=URL)  # URL 초기화
HTML = driver.page_source
soup = BeautifulSoup(HTML, "html.parser")

# 요소들 추출
주소 = soup.select_one("#oFNiHe > div > div > div > div.eKPi4 > span.BBwThe")
현재_날씨 = soup.select_one("#wob_dc")
현재_시간 = soup.select_one("#wob_dts")
현재_온도 = soup.select_one("#wob_tm")


print(f"주소:{주소.text}")
print(f"현재_날씨: {현재_날씨.text}")
print(f"현재_온도: {현재_온도.text}C")
print(f"현재_시간: {현재_시간.text}")
