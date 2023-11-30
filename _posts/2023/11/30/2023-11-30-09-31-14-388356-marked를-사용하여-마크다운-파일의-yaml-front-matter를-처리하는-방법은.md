---
layout: post
title: "[javascript] Marked를 사용하여 마크다운 파일의 YAML Front Matter를 처리하는 방법은?"
description: " "
date: 2023-11-30
tags: [javascript]
comments: true
share: true
---

YAML Front Matter는 마크다운 파일의 맨 위에 위치하며, 파일의 메타데이터를 정의하는 블록입니다. 일반적으로 파일의 제목, 작성자, 생성일 등의 정보를 YAML 형식으로 표현합니다.

Marked에서 YAML Front Matter를 처리하기 위해서는 다음과 같은 단계를 따릅니다:

1. Marked를 설치합니다. 다음과 같이 npm을 통해 설치할 수 있습니다:

```shell
npm install marked
```

2. 파일에서 마크다운을 읽어옵니다. 파일을 읽어오는 방법은 사용하는 환경에 따라 다를 수 있습니다. 여기에서는 Node.js의 `fs` 모듈을 사용하여 파일을 읽어온다고 가정하겠습니다.

```javascript
const fs = require('fs');
const filePath = 'example.md';
const content = fs.readFileSync(filePath, 'utf-8');
```

3. Marked를 사용하여 마크다운을 HTML로 변환합니다. YAML Front Matter는 `meta` 객체로 반환됩니다.

```javascript
const marked = require('marked');
const renderer = new marked.Renderer();

let meta = {};

renderer.frontmatter = function(data) {
  meta = yaml.safeLoad(data);
};

const html = marked(content, { renderer });

console.log(meta); // YAML Front Matter 객체 출력
console.log(html); // HTML 변환된 마크다운 내용 출력
```

이렇게 하면 마크다운 파일의 YAML Front Matter를 손쉽게 처리할 수 있습니다. YAML Front Matter를 가져와서 후속 작업에 활용할 수 있습니다.