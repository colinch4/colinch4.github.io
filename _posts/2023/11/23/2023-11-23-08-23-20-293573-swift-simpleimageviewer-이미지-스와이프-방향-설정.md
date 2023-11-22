---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 스와이프 방향 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift SimpleImageViewer는 사용자에게 이미지를 간편하게 보여주는 기능을 제공하는 라이브러리입니다. 이 라이브러리를 사용하면 이미지를 스와이프하여 전환할 수 있습니다. 그러나 기본적으로 스와이프 동작은 수평으로 설정되어 있습니다. 이번 기사에서는 SimpleImageViewer에서 이미지 스와이프 방향을 설정하는 방법에 대해 알아보겠습니다.

### 이미지 스와이프 방향 설정하기

SimpleImageViewer에서 이미지 스와이프 방향을 설정하려면 `allowVerticalSwiping` 속성을 사용하면 됩니다. 이 속성을 `true`로 설정하면 이미지 스와이프가 수직 방향으로도 가능하게 됩니다.

다음은 `allowVerticalSwiping` 속성을 활성화하는 예시입니다.

```swift
let imageViewer = SimpleImageViewer()
imageViewer.allowVerticalSwiping = true
```

위 예시에서는 `SimpleImageViewer()`로 객체를 생성한 후, `allowVerticalSwiping` 속성을 `true`로 설정하여 수직 스와이프를 가능하게 합니다.

### 참고 자료

- [SimpleImageViewer GitHub 페이지](https://github.com/jonalbright/SimpleImageViewer)

위의 참고 자료는 SimpleImageViewer의 공식 GitHub 페이지로 가이드와 예제 코드를 제공하고 있습니다.

이제 SimpleImageViewer에서 이미지 스와이프 방향을 설정하는 방법에 대해 알게 되었습니다. 이를 통해 사용자에게 더 편리한 이미지 뷰어를 제공할 수 있습니다.