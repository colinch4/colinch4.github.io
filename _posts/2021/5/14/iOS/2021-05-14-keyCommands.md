---
layout: post
title: "[iOS] UIKeyCommands"
description: " "
date: 2021-05-14
tags: [ios]
comments: true
share: true
---


## UIKeyCommands
- iOS에서 외부 키보드 입력을 감지할 때 사용           

## 사용법     
```swift
self.addKeyCommand(.init(input: "\r",
                         modifierFlags: [],
                         action: #selector(loginBtnDidTapped))
)
```     

```swift
.init(input: "\u{8}", modifierFlags: [], action: #selector(loginBtnDidTapped)
.init(input: "\1", modifierFlags: [], action: #selector(loginBtnDidTapped)
.init(input: UIKeyCommand.inputUpArrow, modifierFlags: [], action: #selector(loginBtnDidTapped)
```      
위와 같은 방법들이 있다     
