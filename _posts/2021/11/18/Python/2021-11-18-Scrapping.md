---
layout: post
title: "[파이썬] Scrapping"
description: " "
date: 2021-11-18
tags: [python]
comments: true
share: true
---

Web Scrapping
---
[siori](https://advenoh.tistory.com/2)

* **Web Scraping**
웹 사이트의 내용을 가져와 원하는 형태로 가공하는 것을 의미      

* **Web Crawling**
자동화 봇(bot)인 웹 크롤러가 정해진 규칙에 따라 복수 개의 웹 페이지를 가져오는 하는 행위       

#### Web Scrapping 3 Steps

> Scraping - 데이터 가져오기       
> Parsing - 데이터 파씽       
> Manipulation - 데이터 가공  

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)      

~~~~~Python
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get
("https://www.indeed.com/jpbs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

print(indeed_soup)
~~~~~


~~~~python
import requests
from bs4 import BeautifulSoup

indeed_result=requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")

indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

pagination = indeed_soup.find("div",{"class":"pagination"})

links = pagination.find_all('a')
pages = []
for link in links[:-1]:
  pages.append(int(link.string))
print(pages)



---result
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

~~~~~


INDEED Practic  
~~~~Python
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'

def extract_indeed_pages():
  result = requests.get(URL)

  soup = BeautifulSoup(result.text, 'html.parser')

  pagination = soup.find('div', {'class':'pagination'})

  links = pagination.find_all('a')
  pages = []
  for link in links[:-1] :
    pages.append(int(link.string))

  max_page = pages[-1]
  return max_page

def extract_indeed_jobs(last_page):
  #for page in range(last_page):
  jobs=[]
  result = requests.get(f"{URL}&start={0*LIMIT}")

  soup=BeautifulSoup(result.text,"html.parser")

  results=soup.find_all("div",{"class":"jobsearch-SerpJobCard"})

  for result in results:
    title=result.find("h2",{"class":"title"}).find("a")["title"]

  print(title)  // get Title

  return jobs

~~~~

~~~~Python
def extract_indeed_jobs(last_page):
  jobs = []
  #for page in range(last_page):
  result = requests.get(f'{URL}&start={0 * LIMIT}')
  soup = BeautifulSoup(result.text, 'html.parser')
  results = soup.find_all('div', {"class" : 'jobsearch-SerpJobCard'})
  for result in results :

   company = result.find("span", {"class":"company"})

   // get company
   if company.find("a") is not None :
     print(company.find("a").string)
   else :
     print (company.string)

  return jobs
~~~~
