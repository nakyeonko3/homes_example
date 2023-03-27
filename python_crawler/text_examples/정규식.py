import re

text = "9°Celsius (월요일) 오전 11:00 이후의 글자들"
result = re.search("\(.*", text)


print(result.group())
