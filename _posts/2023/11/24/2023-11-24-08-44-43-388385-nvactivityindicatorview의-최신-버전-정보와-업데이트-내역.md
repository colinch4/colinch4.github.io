---
layout: post
title: "[swift] NVActivityIndicatorView의 최신 버전 정보와 업데이트 내역"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 소개

NVActivityIndicatorView는 Swift로 작성된 iOS 앱을 위한 활발한 인디케이터 뷰를 제공하는 라이브러리입니다. 이 라이브러리는 네이버 개발자센터에서 개발된 것으로, 다양한 타입과 색상의 인디케이터를 제공하여 앱에 다양한 로딩 효과를 적용할 수 있습니다.

## 최신 버전 정보

현재 NVActivityIndicatorView의 최신 버전은 5.0.0입니다. 이 버전은 2021년 9월 9일에 릴리스되었습니다. 최신 버전을 사용하는 것을 권장합니다.

## 업데이트 내역

### 5.0.0 - 2021년 9월 9일

- iOS 15와의 호환성 업데이트
- Swift 5.5와의 호환성 업데이트
- 새로운 인디케이터 타입 추가
- 버그 수정 및 성능 향상

### 4.0.0 - 2020년 8월 12일

- Swift 5.3와의 호환성 업데이트
- iOS 14와의 호환성 업데이트
- 버그 수정 및 성능 향상

### 3.0.0 - 2019년 10월 28일

- Swift 5.1과의 호환성 업데이트
- iOS 13과의 호환성 업데이트
- 새로운 인디케이터 타입 추가
- 버그 수정 및 성능 향상

## 사용 예시

```swift
import NVActivityIndicatorView

// 인디케이터 뷰 생성
let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
let activityIndicatorView = NVActivityIndicatorView(frame: frame)

// 인디케이터 속성 설정
activityIndicatorView.type = .ballSpinFadeLoader
activityIndicatorView.color = UIColor.red

// 인디케이터 시작
activityIndicatorView.startAnimating()

// 인디케이터 정지
activityIndicatorView.stopAnimating()
```

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 문서](https://ninjaprox.github.io/NVActivityIndicatorView)
- [NVActivityIndicatorView 샘플 앱](https://github.com/ninjaprox/NVActivityIndicatorView/tree/master/Example)