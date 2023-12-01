---
layout: post
title: "[python] Requests-HTML와 Beautiful Soup을 함께 사용하는 방법"
description: " "
date: 2023-12-01
tags: [python]
comments: true
share: true
---

## 소개
Requests-HTML은 웹 페이지에서 데이터를 가져오고 파싱하는 데 사용하는 인기 있는 Python 라이브러리입니다. Beautiful Soup은 HTML과 XML 문서를 파싱하는 동시에 데이터를 추출하는 용도로 사용됩니다. 이 글에서는 이 두 라이브러리를 함께 사용하여 웹 페이지에서 데이터를 스크래핑하는 방법을 알아보겠습니다.

## 설치
먼저 Requests-HTML과 Beautiful Soup을 설치해야 합니다. 아래의 명령어를 사용하여 설치할 수 있습니다.

```python
pip install requests-html beautifulsoup4
```

## 사용 예시
사용 예시를 보기 위해 아래의 HTML 코드를 예시로 사용하겠습니다.

```html
<!DOCTYPE html>
<html>
<head>
<title>Example Page</title>
</head>
<body>
<h1>Welcome</h1>
<p>This is an example paragraph.</p>
<ul>
<li>Item 1</li>
<li>Item 2</li>
<li>Item 3</li>
</ul>
</body>
</html>
```

이제 Python 스크립트에서 Requests-HTML과 Beautiful Soup을 사용하여 이 HTML 문서에서 데이터를 추출해 보겠습니다.

```python
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# 웹 페이지 가져오기
session = HTMLSession()
response = session.get('https://example.com')
response.html.render()

# HTML 파싱하기
soup = BeautifulSoup(response.html.html, 'html.parser')

# 데이터 추출하기
title = soup.find('title').text
heading = soup.find('h1').text
paragraph = soup.find('p').text
items = [item.text for item in soup.find_all('li')]

# 결과 출력하기
print(f'Title: {title}')
print(f'Heading: {heading}')
print(f'Paragraph: {paragraph}')
print(f'Items: {items}')
```

위의 코드를 실행하면 다음과 같은 결과가 출력됩니다.

```
Title: Example Page
Heading: Welcome
Paragraph: This is an example paragraph.
Items: ['Item 1', 'Item 2', 'Item 3']
```

Requests-HTML은 웹 페이지를 가져와서 JavaScript를 실행한 후에 HTML을 파싱할 수 있도록 해줍니다. 따라서 `response.html.render()` 메서드를 사용하여 JavaScript를 실행시켜야 파싱이 가능합니다.

## 결론
Requests-HTML과 Beautiful Soup을 함께 사용하면 웹 페이지에서 데이터를 쉽게 스크래핑할 수 있습니다. Requests-HTML을 사용하여 웹 페이지를 가져오고 JavaScript를 실행한 후에 Beautiful Soup을 사용하여 HTML을 파싱하고 데이터를 추출하는 방법을 알아보았습니다. 이 방법을 사용하여 데이터를 스크래핑하면서 다양한 웹 사이트에서 유용한 정보를 얻을 수 있습니다.

## 참고 자료
- [Requests-HTML 공식 문서](https://html.python-requests.org/)
- [Beautiful Soup 공식 문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)