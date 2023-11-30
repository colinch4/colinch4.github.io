---
layout: post
title: "[javascript] Marked를 사용하여 Markdown 파일에 타임라인(Timeline)을 추가하는 방법은?"
description: " "
date: 2023-11-30
tags: [javascript]
comments: true
share: true
---

1. Marked를 프로젝트에 설치합니다. NPM을 사용한다면, 아래 명령어를 실행하여 Marked를 설치할 수 있습니다:

```
npm install marked
```

2. HTML 파일에서 Marked를 import합니다:

```html
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
```

3. Markdown 파일에서 타임라인을 추가하고 싶은 위치에 다음과 같이 Markdown 문법으로 타임라인을 작성합니다:

```markdown
# My Timeline

<!-- 타임라인 시작 -->
---

### 2022

- 이벤트 1
    - 세부 정보 1
    - 세부 정보 2

- 이벤트 2
    - 세부 정보 3
    - 세부 정보 4

---

### 2021

- 이벤트 3
    - 세부 정보 5
    - 세부 정보 6

- 이벤트 4
    - 세부 정보 7
    - 세부 정보 8

<!-- 타임라인 종료 -->
```

4. JavaScript에서 Marked를 사용하여 Markdown 파일을 HTML로 변환하고, 변환된 HTML을 원하는 위치에 삽입합니다:

```javascript
const markdownContent = `
# My Timeline

<!-- 타임라인 시작 -->
---

### 2022

- 이벤트 1
    - 세부 정보 1
    - 세부 정보 2

- 이벤트 2
    - 세부 정보 3
    - 세부 정보 4

---

### 2021

- 이벤트 3
    - 세부 정보 5
    - 세부 정보 6

- 이벤트 4
    - 세부 정보 7
    - 세부 정보 8

<!-- 타임라인 종료 -->
`;

const htmlContent = marked(markdownContent);
const timelineElement = document.getElementById('timeline');
timelineElement.innerHTML = htmlContent;
```

위의 예시에서 `#timeline`은 타임라인을 삽입하려는 HTML 요소의 ID입니다. 해당 요소에 Marked로 변환된 HTML이 삽입됩니다.

이제 Marked를 사용하여 Markdown 파일에 타임라인을 추가할 수 있습니다. 타임라인의 스타일링은 CSS로 따로 지정하거나, 이미 존재하는 CSS 스타일을 활용할 수 있습니다.