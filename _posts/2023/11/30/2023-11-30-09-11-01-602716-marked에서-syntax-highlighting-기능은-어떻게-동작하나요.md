---
layout: post
title: "[javascript] Marked에서 Syntax Highlighting 기능은 어떻게 동작하나요?"
description: " "
date: 2023-11-30
tags: [javascript]
comments: true
share: true
---

Marked에서 Syntax Highlighting을 사용하려면, 지원되는 언어에 대한 Syntax Highlighting 스타일을 제공하는 외부 라이브러리를 추가로 설치해야 합니다. 대표적인 라이브러리로는 Prism, Highlight.js, CodeMirror 등이 있습니다. 

Marked는 프리셋으로 지정된 Marked Renderer 객체의 highlight 속성을 사용하여 Syntax Highlighting을 구현합니다. 외부 라이브러리에서 제공하는 기능을 이용하여 코드 블록에 해당하는 HTML 요소를 생성하고, 생성된 요소를 렌더링 결과에 적용합니다.

아래는 Prism 라이브러리를 사용하여 Marked에서 Syntax Highlighting을 적용하는 예제 코드입니다.

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs/themes/prism.css" />
  <script src="https://cdn.jsdelivr.net/npm/prismjs/prism.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
</head>
<body>
  <div id="content"></div>

  <script>
    const renderer = new marked.Renderer();
    renderer.code = function (code, language) {
      const highlightedCode = Prism.highlight(code, Prism.languages[language], language);
      return `<pre><code class="language-${language}">${highlightedCode}</code></pre>`;
    };

    const text = '```javascript\nconsole.log("Hello, world!");\n```';
    const result = marked(text, { renderer });

    document.getElementById('content').innerHTML = result;
  </script>
</body>
</html>
```

이 예제에서는 Prism 라이브러리를 사용하여 Syntax Highlighting을 수행합니다. 해당 라이브러리를 HTML 파일에 추가한 뒤, Marked Renderer 객체의 highlight 속성을 재정의하여 Prism의 highlight 함수를 호출하여 Syntax Highlighting을 적용합니다. 이후 Markdown 텍스트를 Marked로 렌더링하면 코드 블록이 Syntax Highlighting된 결과를 얻을 수 있습니다.

참고문헌:
- [Marked 공식 문서](https://marked.js.org/)
- [Prism 공식 문서](https://prismjs.com/)
- [Highlight.js 공식 문서](https://highlightjs.org/)
- [CodeMirror 공식 문서](https://codemirror.net/)