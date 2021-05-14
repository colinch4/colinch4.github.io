---
layout: post
title: "[iOS] Notification"
description: " "
date: 2021-05-14
tags: [iOS]
comments: true
share: true
---

# Notification

**1. User Notification 사용을 위한 import**

![f0](https://user-images.githubusercontent.com/45002556/108618874-e0ae4100-7464-11eb-8b88-2785131fc3f7.png)

**2. 사용자에게 알림 권한을 얻는다**

<img width="344" alt="f1" src="https://user-images.githubusercontent.com/45002556/108619183-59fa6380-7466-11eb-8452-d69e52a9503b.png">

![f2](https://user-images.githubusercontent.com/45002556/108618907-0f2c1c00-7465-11eb-8bdb-f33a596f0d08.png)       

권한을 요청하기 위한 코드로 requestAuthorization 메소드를 사용. 위에 option에서 badge를 제거하면 아래 그림과 같이 앱 위에 뜨는 숫자를 안나오게 할 수 있다. 

<img width="103" alt="F3" src="https://user-images.githubusercontent.com/45002556/108618918-2539dc80-7465-11eb-897e-0859fb0cb6a8.png">

**3. 알람 메세지 설정**
![f4](https://user-images.githubusercontent.com/45002556/108618944-3aaf0680-7465-11eb-9e9c-a1793dd39a77.png)

위에 그림과 같이 알람 메세지에는 제목과 내용으로 메세지가 구성되어 있다. 따라서 위와 같이 어떤 내용을 전달해 줄지 코드를 작성.

![f5](https://user-images.githubusercontent.com/45002556/108618957-54504e00-7465-11eb-9ebf-a5b7b88fede4.png)

내용을 도와주는 클래스는 UNMutableNotificationContent입니다. 이 객체를 만들어 content를 설정. 이 외에도 subtitle 변수를 사용하여 부제목을 설정할 수도 있다.

**4. 알림 트리거 지정**     
알림이 언제 전송 될지 알려주기 위해서 특정시간, 시간간격, 위치변경을 기반으로 트리거를 설정할 수 있다.   
![f6](https://user-images.githubusercontent.com/45002556/108618989-8366bf80-7465-11eb-891c-d590e60703f8.png)

위 사진처럼 애플 문서에 트리거의 종류가 나와 있다.

![f7](https://user-images.githubusercontent.com/45002556/108619050-98dbe980-7465-11eb-919e-17cd248617f6.png)

위에 사진처럼 저는 TimeInteverNotificationTrigger를 사용하여 특정 시간 이후에 알림이 오도록 트리거를 설정. 트리거를 만들고 UNNotificationRequest를 통해 식별자를 설정하고 전달할 메세지와 트리거를 넘겨 준다.

<img width="376" alt="f8" src="https://user-images.githubusercontent.com/45002556/108619055-a42f1500-7465-11eb-9a04-1c913fff2835.png">


가운데 버튼을 누르면 다음과 같이 알람이 오도록 간단하게 push 알림 앱을 구현.

<img width="371" alt="f9" src="https://user-images.githubusercontent.com/45002556/108619060-b1e49a80-7465-11eb-9546-677b54d29c20.png">

