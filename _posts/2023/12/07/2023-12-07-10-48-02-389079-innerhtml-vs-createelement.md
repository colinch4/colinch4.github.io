---
layout: post
title: "[javascript] innerHTML vs createElement"
description: " "
date: 2023-12-07
tags: [javascript]
comments: true
share: true
---

자바스크립트로 HTML 요소를 동적으로 생성하는 방법은 여러 가지가 있습니다. 그 중에서도 가장 일반적으로 사용되는 방법은 `innerHTML` 속성을 사용하는 것과 `createElement` 함수를 사용하는 것입니다. 이 두 가지 방법 간에는 몇 가지 차이점이 있습니다.

## innerHTML

`innerHTML` 속성은 요소의 내부 HTML 코드를 변경하는 데 사용됩니다. 

```javascript
let container = document.getElementById('container');
container.innerHTML = "<p>Hello, world!</p>";
```

위의 예제에서는 id가 "container"인 요소의 내부 HTML을 `<p>Hello, world!</p>`로 변경하고 있습니다. `innerHTML` 속성을 이용하면 HTML 코드를 문자열로 작성하여 간편하게 요소의 내용을 변경할 수 있습니다.

하지만 `innerHTML`을 사용하는 것은 요소의 내용을 변경하는 것뿐만 아니라, 해당 요소의 자식 요소들을 모두 제거하고 다시 생성하는 과정이 함께 진행됩니다. 이는 성능상의 이슈를 유발할 수 있으므로 요소의 내용을 변경해야할 때에는 적절히 사용해야 합니다.

## createElement

`createElement` 함수를 사용하여 새로운 요소를 동적으로 생성할 수 있습니다.

```javascript
let paragraph = document.createElement('p');
paragraph.textContent = "Hello, world!";
```

위의 예제에서는 새로운 `<p>` 요소를 생성하고 그 내부 텍스트를 설정하는 것을 볼 수 있습니다. 이렇게 생성된 요소는 아직 문서에 추가되기 전이므로, 원하는 위치로 추가해야 합니다.

```javascript
let container = document.getElementById('container');
container.appendChild(paragraph);
```

위의 예제처럼 `appendChild` 메소드를 사용하여 생성된 요소를 다른 요소의 자식으로 추가할 수 있습니다. `createElement` 함수를 사용하면 자식 요소를 다시 생성하지 않고도, 기존 요소의 내용을 보존하면서 동적으로 새로운 요소를 추가할 수 있습니다. 이로써 성능상의 이점을 얻을 수 있습니다.

## 결론

`innerHTML`과 `createElement`는 HTML 요소를 동적으로 생성하고 변경하는 데에 사용됩니다. `innerHTML`은 내부 HTML 코드를 문자열로 작성하여 요소의 내용을 변경하는 반면, `createElement`은 새로운 요소를 생성하여 기존 요소의 자식으로 추가합니다. `innerHTML`은 내부적으로 요소의 자식 요소들을 모두 제거하고 다시 생성하는 과정이 있어 성능상의 이슈가 있을 수 있으므로, 요소의 내용을 변경해야할 때에는 적절한 상황에서 사용해야 합니다.

## 참고 자료

- [MDN Web Docs - innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)
- [MDN Web Docs - createElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)