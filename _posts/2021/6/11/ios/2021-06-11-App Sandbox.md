---
layout: post
title: "[ios] App Sandbox"
description: " "
date: 2021-06-11
tags: [ios]
comments: true
share: true
---

## App Sandbox

[iOS Swift입문 - Sandbox](https://programmers.co.kr/learn/courses/4/lessons/214#)

⇒ 해당 영상 정리합니다.

## 샌드박스의 도입 이유를 이해한다

- unix - chroot : chroot 환경에서 실행되는 프로그램은 현재의 디렉토리를 root로 인식한다.
- 따라서 앱은 sandbox 디렉토리를 root 디렉토리로 인식하므로 sandbox 디렉토리 이외의 외부 파일에 앱이 접근 할 수 없다. (chroot jail)
- 따라서 사용자 데이터는 모두 앱 외부에 있으므로 **각 앱은 사용자 데이터에 접근 불가**하다.
- 따라서 어플리케이션들이 사용자 데이터에 함부로 접근 불가하므로 **iOS 는 다른 OS에 비해 상대적으로 보안상 안전하다.**

## 샌드박스 환경에서의 제약 사항들을 안다

- 따라서 사용자 데이터를 접근하기 위해 **API를 이용**해야 한다.
- API 의 예로는 PhotoKit(사진 관련), EventKit(달력 관련), Address Book(연락처 관련) 등이 있다.

 

[[iOS] 앱 샌드박스(App Sandbox)와 Container Directory](https://jinshine.github.io/2018/07/02/iOS/%EC%95%B1%20%EC%83%8C%EB%93%9C%EB%B0%95%EC%8A%A4(App%20Sandbox)%EC%99%80%20Container%20Directory/)

⇒ 해당 글 정리합니다.

![Container](https://user-images.githubusercontent.com/38216027/99878880-c4bfb700-2c4b-11eb-87a9-dc658fd54303.png)

> 샌드박스에는 해당 앱만 접근할 수 있는 미리 만들어진 Bundle Container, Data Container, iCloud Container 가 있다. (Container가 곧 디렉토리)

## Bundle Container

- 앱 자체, 실행 가능(Executable)파일, info.plist, Resources(이미지, 사운드, strings 등)등을 함께 그룹화한다.
- 읽기 전용이므로, 수정이 필요한 경우 데이터 컨테이너로 옮겨서 작업한다.

## Data Container

- 기본 디렉토리 - Document, Library, tmp, SystemData
- Document : user data
- Library: non-user data
- tmp: used to store very short lived data that does not need to be persisted across launches.