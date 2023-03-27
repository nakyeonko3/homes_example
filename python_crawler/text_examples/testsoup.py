from bs4 import BeautifulSoup

html_doc = """
<div>
<svg>
  <text style="font: bold 11px arial; text-anchor: middle; display: none;">Hello World!</text>
</svg>
</div>

"""

soup = BeautifulSoup(html_doc, "html.parser")
text = soup.find(
    "text", style="font: bold 11px arial; text-anchor: middle; display: none;"
)
print(text.text)
