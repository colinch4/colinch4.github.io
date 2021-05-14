---
layout: post
title: "[iOS] iOS 실제 화면 크기의 서브 뷰 추가"
description: " "
date: 2021-05-14
tags: [iOS]
comments: true
share: true
---

# iOS 실제 화면 크기의 서브 뷰 추가

```swift
// 디바이스의 실제 화면 크기
var frame = UIScreen.main.bounds
frame.origin.y = -frame.size.height

// 디바이스 크기만큼 뷰를 생성
let view = UIView(frame: frame)
view.backgroundColor = color

// 현재 뷰에 새로 만든 뷰를 추가
self.addSubview(view)
```
