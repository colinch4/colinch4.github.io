---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 위치 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 앱에서 간단하고 매력적인 로딩 애니메이션을 구현하는 데 사용되는 라이브러리입니다. 이 라이브러리는 액티비티 인디케이터를 나타내고 애니메이션을 관리하는 데 도움이 됩니다.

NVActivityIndicatorView의 기본 동작은 화면 중앙에 위치한 로딩 인디케이터를 표시하는 것입니다. 그러나 때로는 화면의 다른 위치에 로딩 인디케이터가 표시되길 원할 수도 있습니다. 이번 블로그에서는 Swift에서 NVActivityIndicatorView의 위치를 설정하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView 위치 설정하기

NVActivityIndicatorView의 위치를 설정하려면 먼저 해당 애니메이션 뷰를 만들고 화면에 추가해야 합니다. 그런 다음 위치를 설정할 수 있습니다.

```swift
import NVActivityIndicatorView

// 위치를 설정할 컨테이너 뷰 생성
let containerView = UIView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
containerView.center = view.center

// NVActivityIndicatorView 추가
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
activityIndicatorView.center = containerView.center
containerView.addSubview(activityIndicatorView)

// 위치 설정
activityIndicatorView.translatesAutoresizingMaskIntoConstraints = false
activityIndicatorView.centerXAnchor.constraint(equalTo: containerView.centerXAnchor).isActive = true
activityIndicatorView.centerYAnchor.constraint(equalTo: containerView.centerYAnchor).isActive = true

// 애니메이션 시작
activityIndicatorView.startAnimating()
```

위의 코드에서, 우리는 `containerView`라는 컨테이너 뷰를 만들고 실제 로딩 애니메이션을 포함하는 `activityIndicatorView`를 추가합니다. 그런 다음, `activityIndicatorView`의 위치를 설정하기 위해 AutoLayout을 사용합니다.

위 코드에서 주목해야 할 부분은 다음과 같습니다:

- `activityIndicatorView.translatesAutoresizingMaskIntoConstraints = false`: 이를 설정하면 코드로 제약 조건을 추가할 수 있습니다.
- `activityIndicatorView.centerXAnchor.constraint(equalTo: containerView.centerXAnchor).isActive = true`: 애니메이션 뷰의 가로 위치를 컨테이너 뷰의 중앙에 맞춥니다.
- `activityIndicatorView.centerYAnchor.constraint(equalTo: containerView.centerYAnchor).isActive = true`: 애니메이션 뷰의 세로 위치를 컨테이너 뷰의 중앙에 맞춥니다.

위의 코드를 실행하면 NVActivityIndicatorView 로딩 애니메이션은 컨테이너 뷰의 중앙에 정렬되어 표시됩니다.

이제 당신은 Swift에서 NVActivityIndicatorView의 위치를 커스터마이즈하는 방법을 알게 되었습니다. 필요에 따라 뷰의 위치를 조정하여 앱의 디자인에 맞게 설정할 수 있습니다.

## 참고자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)