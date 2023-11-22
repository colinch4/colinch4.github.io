---
layout: post
title: "[javascript] Parcel에서 Hot Module Replacement(HMR)을 사용하는 방법은?"
description: " "
date: 2023-11-22
tags: [javascript]
comments: true
share: true
---

먼저, Parcel 프로젝트를 설정합니다. 프로젝트 디렉토리 안에 `index.html` 파일과 `index.js` 파일을 생성합니다. 그리고 다음과 같은 코드를 `index.html`에 추가합니다:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Parcel HMR Example</title>
</head>
<body>
  <script src="./index.js"></script>
</body>
</html>
```

`index.js` 파일에는 간단한 코드를 작성합니다:

```javascript
let count = 0;

function updateCount() {
  document.getElementById('count').textContent = count;
}

function incrementCount() {
  count++;
  updateCount();
}

document.getElementById('increment').addEventListener('click', incrementCount);

updateCount();
```

이제, Parcel과 HMR을 사용하여 개발 서버를 실행합니다. 터미널에서 다음 명령을 입력합니다:

```bash
parcel index.html
```

이렇게 하면 Parcel은 개발 서버를 시작하고 웹 브라우저에서 앱을 열어줍니다. 이제 브라우저를 열고 `localhost:1234` 또는 Parcel이 나타낸 포트로 이동하면 앱을 볼 수 있습니다.

이제 HMR을 사용하여 코드 변경을 확인해보겠습니다. `index.js` 파일을 열고 `count` 변수 값을 변경하고 저장하세요. 브라우저는 코드 변경을 감지하고 변경된 내용을 즉시 적용합니다. 내용이 변경된 화면을 볼 수 있습니다. 이를 통해 코드를 수정하고 페이지를 새로 고침할 필요가 없이 변경 내용을 확인할 수 있습니다.

이렇게 Parcel에서 HMR을 사용하여 코드 변경을 실시간으로 반영할 수 있습니다. HMR은 개발 과정을 훨씬 효율적으로 만드는 강력한 기능입니다. Parcel은 HMR을 자동으로 처리하기 때문에 구성할 필요가 없으며, 코드를 작성하고 저장하기만 하면 됩니다.

Parcel 공식 문서에서 Parcel과 HMR에 대한 자세한 내용을 참조할 수 있습니다. (https://v2.parceljs.org/features/hmr/)

**참고 자료:**
- Parcel 공식 문서: https://v2.parceljs.org/
- HMR 소개: https://parceljs.org/hmr.html