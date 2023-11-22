---
layout: post
title: "[lib] SwiftLint란?"
description: " "
date: 2021-05-14
tags: [swift]
comments: true
share: true
---


## SwiftLint
- 코드 정리 및 일관된 코드를 작성하게 해주는 라이브러리

**사용법**

1. Podfile에 pod 'SwiftLint' 추가
2. Target > build phase > new run script phase
3. run script에 ${PODS_ROOT}/SwiftLint/swiftlint를 추가

**예외처리 방법**   

프로젝트에 empty 파일 생성    
<img width="853" alt="f1" src="https://user-images.githubusercontent.com/45002556/108619878-279f3500-746b-11eb-9db1-fd51622d71b3.png">

파일 이름은 무조건 .swiftlint.yml로 지정       

<img width="740" alt="f2" src="https://user-images.githubusercontent.com/45002556/108619881-2a9a2580-746b-11eb-8b41-532d9d302d29.png">

disabled_rules: 사용하지 않을 규칙   
included: 포함할 파일 정의       
excluded: 포함하지 않을 파일 정의     

**예시**   
disabled_rules:
- trailing_whitespace
- file_length
- identifier_name
- unused_closure_parameter

excluded:
- Pods
- smartlearning.ios/Player
- smartlearning.ios/KollusSDK
- smartlearning.iosTests
- AppDelegate.swift
- SceneDelegate.swift

## SwiftLint git 주소     
https://github.com/realm/SwiftLint
