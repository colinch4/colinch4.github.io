---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 로딩 인디케이터의 속도 조절 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

로딩 인디케이터는 사용자에게 애플리케이션이 작업을 수행 중임을 시각적으로 표시하는 데 사용되는 중요한 요소입니다. NVActivityIndicatorView는 Swift에서 로딩 인디케이터를 만들고 제어하는데 도움이 되는 강력한 라이브러리입니다. 

기본적으로 NVActivityIndicatorView는 일정한 속도로 회전하는 원 모양의 로딩 인디케이터를 제공합니다. 그러나 때로는 이 속도를 조절할 필요가 있을 수 있습니다. 이러한 경우에 NVActivityIndicatorView의 속도를 조절하는 방법을 알아보겠습니다.

## NVActivityIndicatorView 속도 조절 방법

NVActivityIndicatorView의 속도를 조절하려면 기본값으로 설정된 `animationDuration` 속성을 변경하면 됩니다. 이 속성은 로딩 인디케이터가 전체 회전을 완료하는 데 걸리는 시간을 나타내는 부동 소수점 값입니다.

아래의 예시 코드를 통해 속도 조절 방법을 보여드리겠습니다.

```swift
// NVActivityIndicatorView 인스턴스 생성
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .circleStrokeSpin, color: .gray, padding: nil)

// 기본 속도 확인
print("기본 속도:", activityIndicatorView.animationDuration)

// 1초로 속도 변경
activityIndicatorView.animationDuration = 1.0

// 변경된 속도 확인
print("변경된 속도:", activityIndicatorView.animationDuration)
```

위의 코드에서는 `NVActivityIndicatorView` 인스턴스를 생성하고, `animationDuration` 속성을 사용하여 기존 속도를 출력한 후, `animationDuration`을 1.0로 설정하여 속도를 변경하고 출력합니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)

위에서 설명한 방법으로 NVActivityIndicatorView의 로딩 인디케이터 속도를 조절할 수 있습니다. NVActivityIndicatorView 라이브러리의 공식 GitHub 페이지에는 더 많은 정보와 사용 가능한 속성들을 확인할 수 있으니 참고하시기 바랍니다.