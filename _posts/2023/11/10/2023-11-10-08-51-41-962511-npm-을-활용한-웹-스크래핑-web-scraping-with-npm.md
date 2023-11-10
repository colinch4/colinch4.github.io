---
layout: post
title: "npm 을 활용한 웹 스크래핑 (Web scraping with npm)"
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

웹 스크래핑은 웹 페이지에서 데이터를 추출하는 기술입니다. 이 기술을 활용하면 인터넷에서 필요한 정보를 수집하고 분석할 수 있습니다. 그 중에서도 npm(Node Package Manager)을 이용하여 웹 스크래핑을 해보겠습니다.

## 1. Cheerio 소개

Cheerio는 jQuery 스타일의 문법을 사용하여 HTML 요소를 선택하고 조작할 수 있는 간편한 라이브러리입니다. Cheerio를 사용하면 서버 측에서 웹 페이지의 HTML을 가져올 수 있고, 원하는 데이터를 추출할 수 있습니다.

Cheerio는 npm을 통해 설치할 수 있습니다. 다음 명령어를 사용하여 Cheerio를 설치합니다:

```sh
npm install cheerio
```

## 2. 웹 페이지의 HTML 가져오기

먼저, 웹 스크래핑을 위해 웹 페이지의 HTML을 가져와야 합니다. 이를 위해서는 axios 또는 request 라이브러리를 사용할 수 있습니다. 이 예시에서는 axios를 사용하도록 하겠습니다.

먼저, axios를 설치합니다:

```sh
npm install axios
```

다음은 웹 페이지의 HTML을 가져오는 예시 코드입니다:

```javascript
const axios = require('axios');

axios.get('https://example.com')
  .then((response) => {
    const html = response.data;
    console.log(html);
  })
  .catch((error) => {
    console.error(error);
  });
```

위 코드에서는 axios를 사용하여 'https://example.com' 페이지의 HTML을 가져와서 콘솔에 출력합니다.

## 3. 데이터 추출하기

Cheerio를 사용하여 원하는 데이터를 추출할 수 있습니다. HTML에서 특정 요소를 선택하고 조작하기 위해 Cheerio의 문법을 사용합니다. 다음은 Cheerio를 사용하여 웹 페이지에서 제목 태그를 추출하는 예시 코드입니다:

```javascript
const axios = require('axios');
const cheerio = require('cheerio');

axios.get('https://example.com')
  .then((response) => {
    const html = response.data;
    const $ = cheerio.load(html);
    const title = $('h1').text();
    console.log(title);
  })
  .catch((error) => {
    console.error(error);
  });
```

위 코드에서는 'https://example.com' 페이지의 HTML을 가져와서 Cheerio를 사용하여 제목 태그(h1)의 텍스트를 추출합니다.

## 4. 데이터 저장 및 활용하기

데이터 추출이 완료되면 원하는 방식으로 저장하거나 활용할 수 있습니다. 데이터베이스에 저장하거나 파일로 저장하는 등의 다양한 방법이 있습니다. 이 예시에서는 추출한 데이터를 콘솔에 출력하는 것으로 대체하도록 하겠습니다.

```javascript
const axios = require('axios');
const cheerio = require('cheerio');

axios.get('https://example.com')
  .then((response) => {
    const html = response.data;
    const $ = cheerio.load(html);
    const title = $('h1').text();
    const description = $('p').text();
    console.log('Title:', title);
    console.log('Description:', description);
  })
  .catch((error) => {
    console.error(error);
  });
```

위 코드에서는 'https://example.com' 페이지의 HTML을 가져와서 Cheerio를 사용하여 제목 태그(h1)의 텍스트와 설명 태그(p)의 텍스트를 추출하여 콘솔에 출력합니다.

## 5. 마무리

이제 npm과 Cheerio를 사용하여 웹 스크래핑을 수행하는 방법에 대해 알아보았습니다. 웹 스크래핑은 다양한 분야에서 유용하게 활용될 수 있으며, 데이터 분석, 정보 수집 등에 활용할 수 있습니다.

> #npm #web-scraping