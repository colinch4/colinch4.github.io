---
layout: post
title: "[iOS] UserDefaults"
description: " "
date: 2021-05-14
tags: [iOS]
comments: true
share: true
---

# UserDefaults
- key : value 형태로 저장하는 사용자 기본 데이터베이스에 대한 인터페이스
- 사용자 설정이나 환경설정 값에 사용하기 적합하다.(ex: 모바일데이터 사용 on/off, 백그라운드 재생 on/off)

## 사용법
- UserDefaults.standard 뒤에 원하는 데이터 타입을 적으면 된다.

- 값을 저장할 때
```Swift
// bool
let flag = true
UserDefaults.standard.set(flag, forKey: "someBool")

// String
let str = "test"
UserDefaults.standard.set(str, forKey: "someStr")
```

- 값을 가져올 때
```Swift
// bool
UserDefaults.standard.bool(forKey: "someBool")

// String
UserDefaults.standard.string(forKey: someStr)
```
