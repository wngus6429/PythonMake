import requests
from bs4 import BeautifulSoup

indeed_resu = requests.get("https://jp.indeed.com/%E6%B1%82%E4%BA%BA?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")

indeed_soup = BeautifulSoup(indeed_resu.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all('a')

spans = []

for page in pages:
  spans.append(page.find("span"))

print(spans[:-1])