import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.google.com'
response = requests.get(url)
print(response.text)
print(response.status_code)

raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')

if top_jobs_heading is not None:
    article = top_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())
