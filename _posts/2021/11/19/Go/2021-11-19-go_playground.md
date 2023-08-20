---
layout: post
title: "[Go] Go Playground"
description: " "
date: 2021-11-19
tags: [Go]
comments: true
share: true
---

## Go Playground | Go 놀이터
Sandbox 내에서 실행되는 Go  
3rd Party의 패키지 import지원  
링크 : https://play.golang.org/


<img width="582" alt="Screen Shot 2020-01-21 at 2 06 21 PM" src="https://user-images.githubusercontent.com/48475824/72777236-4a538e80-3c58-11ea-87c9-8579d136d4e0.png">

### Buttons
* **Run :** 코드 실행  
출력결과와 에러가 Go 놀이터 하단에 표시됨. 

* **Format :** 코드 형식  
코드의 형식을 맞춰줌.

* **Imports**  
If checked --> Format 작업 수행시 Go Playground가 import 경로를 자동으로 상단에 추가해줌.

* **Share :** 코드 공유  
주어진 URL을 통해 'Go 놀이터'에서 작성해놓은 결과를 공유 할 수 있음. 

* **About :** About Playground  
Playground 에 관한 설명.


### Infrastructure
![overview](https://user-images.githubusercontent.com/48475824/72777538-525ffe00-3c59-11ea-9b32-3b110c7ad264.png)  
Playground는 세 부분으로 나뉨.
1. A back end  
Google's servers 에서 실행

2. A front end  
Google App Engine 에서 실행

3. A JavaScript client  
UI
