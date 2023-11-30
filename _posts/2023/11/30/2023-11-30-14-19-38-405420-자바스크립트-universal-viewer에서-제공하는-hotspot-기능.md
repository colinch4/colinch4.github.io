---
layout: post
title: "[javascript] 자바스크립트 Universal Viewer에서 제공하는 Hotspot 기능"
description: " "
date: 2023-11-30
tags: [javascript]
comments: true
share: true
---

JavaScript Universal Viewer는 풍부한 기능을 제공하는 오픈 소스 라이브러리입니다. 이 라이브러리의 중요한 기능 중 하나는 Hotspot 기능입니다. Hotspot은 웹 페이지의 이미지나 동영상에서 특정한 지점을 강조하는 기능으로, 사용자들이 주의를 집중할 수 있도록 도와줍니다.

## Hotspot 기능 사용하기

Hotspot 기능을 사용하기 위해서는 Universal Viewer 라이브러리를 먼저 웹 페이지에 추가해야 합니다. 아래는 Universal Viewer 라이브러리를 추가하는 코드의 예시입니다.

```javascript
<script src="universal-viewer.js"></script>
<link rel="stylesheet" href="universal-viewer.css">
```

Universal Viewer를 초기화한 후 Hotspot을 추가하는 방법은 다음과 같습니다.

1. 원하는 이미지나 동영상을 Universal Viewer에 로드합니다.
2. Hotspot을 생성하고 위치를 설정합니다.
3. Hotspot을 Universal Viewer에 추가합니다.

아래는 Hotspot을 추가하는 예시 코드입니다.

```javascript
// Universal Viewer 초기화
var viewer = new UniversalViewer({
    container: "#viewer",
    // 기타 옵션 설정
});

// Hotspot 생성 및 추가
var hotspot = new Hotspot({
    position: {
        x: 100, // X 좌표
        y: 200 // Y 좌표
    },
    size: {
        width: 50, // 가로 길이
        height: 50 // 세로 길이
    },
    // 기타 옵션 설정
});

viewer.addHotspot(hotspot);
```

Hotspot 생성 시 위치, 크기 등을 지정할 수 있으며, 추가적인 옵션을 설정할 수도 있습니다. Universal Viewer에 Hotspot을 추가하기 위해 `addHotspot` 메서드를 사용합니다.

## Hotspot 관련 이벤트

Hotspot을 클릭하거나 마우스 오버할 때와 같은 상호작용에 대응하기 위해, Universal Viewer에서는 Hotspot 관련 이벤트를 지원합니다. 예를 들어, Hotspot을 클릭했을 때 특정 동작을 실행하고자 할 때 다음과 같은 코드를 사용할 수 있습니다.

```javascript
hotspot.on("click", function() {
    // 클릭 이벤트 발생 시 실행할 동작
});
```

위 코드에서 `"click"`은 Hotspot의 클릭 이벤트를 의미합니다. 마우스 오버, 마우스 아웃 등 다양한 이벤트에 대해서도 유사한 방식으로 처리할 수 있습니다.

## Hotspot 사용 예시

Hotspot은 다양한 방식으로 활용될 수 있습니다. 예를 들어, 이미지에서 특정 객체나 지점을 강조할 때, 동영상에서 특정 장면을 강조할 때 등에 사용할 수 있습니다. 또한, Hotspot에 이미지나 텍스트를 추가하여 추가 정보를 제공할 수도 있습니다.

아래는 Hotspot을 사용한 예시입니다.

![Hotspot Example](example.png)

이 예시에서는 이미지의 특정 지점에 Hotspot을 추가하고, Hotspot을 클릭하면 해당 지점에 대한 자세한 설명이 표시됩니다.

## 결론

JavaScript Universal Viewer의 Hotspot 기능은 웹 페이지에서 이미지나 동영상의 특정 지점을 강조하기 위해 사용됩니다. Hotspot을 추가하고 관련 이벤트를 처리하는 것은 비교적 간단하며, 다양한 상황에서 활용할 수 있습니다. 더 많은 기능과 옵션에 대해서는 Universal Viewer의 공식 문서를 참조하시기 바랍니다.

---

## 참조

- [Universal Viewer 공식 사이트](https://universalviewer.io/)
- [Universal Viewer GitHub 저장소](https://github.com/universalviewer/universalviewer)