---
layout: post
title: "[python] Jupyter Notebook에서 웹 크롤링/스크레이핑 라이브러리 (beautifulsoup, scrapy 등) 사용하기"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

웹 크롤링 및 스크레이핑은 데이터 수집 및 분석을 위해 중요한 과정입니다. Python에서는 다양한 라이브러리를 활용하여 이를 수행할 수 있습니다. 이번 포스트에서는 Jupyter Notebook을 사용하여 웹 크롤링 및 스크레이핑을 위한 라이브러리인 Beautiful Soup와 Scrapy를 살펴보겠습니다.

## 1. Beautiful Soup를 활용한 웹 크롤링

Beautiful Soup는 HTML 및 XML 파일에서 데이터를 추출하는 파이썬 라이브러리로, 웹 스크레이핑을 위해 주로 사용됩니다. 다음은 Beautiful Soup를 사용하여 웹 페이지의 제목을 추출하는 간단한 예제입니다.

```python
from bs4 import BeautifulSoup
import requests

url = '웹페이지 URL'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.title.string
print(title)
```

위 코드에서 `bs4` 모듈에서 `BeautifulSoup`를 임포트하여 HTML을 파싱하고, `requests` 모듈을 사용하여 웹 페이지에 HTTP 요청을 보냅니다. 그 후에는 추출하고자 하는 데이터를 Beautiful Soup 객체를 사용하여 추출합니다.

## 2. Scrapy를 활용한 웹 크롤링

Scrapy는 빠르고 강력한 웹 크롤링 및 웹 스크레이핑 프레임워크로, 복잡한 웹 크롤링 작업에 적합합니다. 다음은 Scrapy를 사용하여 웹페이지에서 링크를 추출하는 예제입니다.

```python
import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['웹페이지 URL']

    def parse(self, response):
        for link in response.css('a::attr(href)'):
            print(link.extract())
```

위 코드에서는 Scrapy 모듈을 임포트하고, `Spider` 클래스를 상속받아 웹 페이지를 크롤링하고 원하는 데이터를 추출하고자 합니다. `start_urls`에서 크롤링을 시작할 웹 페이지의 URL을 지정하고, `parse` 메서드에서 원하는 데이터를 추출하는 작업을 수행합니다.

## 마무리

Jupyter Notebook을 사용하여 Beautiful Soup와 Scrapy를 활용하여 웹 크롤링 및 스크레이핑을 수행할 수 있습니다. 이를 통해 데이터 수집 및 분석에 필요한 데이터를 쉽게 얻을 수 있습니다.

*관련 문서:*
- Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Scrapy: https://scrapy.org/