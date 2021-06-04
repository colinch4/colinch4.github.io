---
layout: post
title: "[android] Android Architecture Components"
description: " "
date: 2021-06-04
tags: [android]
comments: true
share: true
---

# Android Architecture Components



![img](https://miro.medium.com/max/1400/1*-yY0l4XD3kLcZz0rO1sfRA.png)

*구글에서 권장하는 앱 아키택쳐 가이드의 링크.*
https://developer.android.com/jetpack/docs/guide?hl=ko

위 아키택쳐 가이드대로라면 LiveData는 ViewModel에서 이용되며, Repository가 Room Database에서 가져온 데이터를 객체형식으로 보유하고 있습니다.

아키택쳐 가이드의 핵심은 **각 구성요소가 한 수준 아래의 구성 요소에만 종속되는것** 이며, 오로지 Repository만이 여러개의 하위 구성요소를 가질 수 있습니다

1. [LifeCycle](https://developer.android.com/topic/libraries/architecture/lifecycle)

\- 엑티비티나 프래그먼트의 생명주기를 감지하고 이에 따른 작업을 수행할 수 있게 도와줍니다.

2, [LiveData](https://developer.android.com/topic/libraries/architecture/livedata)

\- 지속적으로 변할 수 있는 값을 생명주기에 맞게 전달할 수 있도록 해줍니다.

3. [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel)

\- 생명주기 변화에 맞서 UI 표시에 필요한 데이터를 관리할 수 있도록 해줍니다.

4. [Room](https://developer.android.com/training/data-storage/room/)

\- SQLite 데이터베이스와 관련된 작업을 간편하게 사용할 수 있도록 해줍니다.



## ViewModel

*공식문서:* https://developer.android.com/topic/libraries/architecture/viewmodel?hl=ko

SOC(Separation of conerns,관심사 분리)의 개념이 강하게 들어간 MVVM에서 ViewModel의 역할은 view에서 필요한 데이터를 model에게 요청하여 응답받은 데이터를 가공항 view에 다시 보내주는 역할



AAC의 ViewModel을 이용하기 위해서는 다음과 같은 gradle세팅이 필요

```xml
//생명주기를 공유하기 위한 라이브러리
implementation "androidx.appcompat:appcompat:1.0.2"
//LiveData를 사용하기 위한 라이브러리
implementation "androidx.lifecycle:lifecycle-viewmodel:2.0.0"
```

