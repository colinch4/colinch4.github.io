---
layout: post
title: "[안드로이드 기초] Android APK 빌드 과정"
description: " "
date: 2020-12-01
tags: [android]
comments: true
share: true
---


![](https://github.com/tkhwang/tkhwang-etc/raw/master/images/build.png)

1. AAPT (Asset Packaging Tool)
    - AndroidManifest.xml이나 액티비티를 위한 XML file 들과 같은 Application Resource Files를 컴파일하여 R.java를 생성하고 특정 resource id로 매핑 시킨다.
    - resource들을 하나로 묶어 resources.ap_라는 중간 파일로 생성해둔다.
2. aidl tool
    - .aidl interface를 java interface로 만들어 준다.
    - AIDL이란 Android Interface Definition Language로 원격 접속이 가능한 객체를 만들 때 사용하고 IPC를 구현할 때 사용할 수 있다. 안드로이드는 각 응용 프로그램이 사용하는 메모리가 아예 분리되어 있기 때문에 통상적인 방법으로는 인수를 넘기기가 힘들어 자바 수준에서 이를 정의하기가 힘들다. 따라서 안드로이드에서 AIDL이라는 별도의 언어 및 컴파일러를 제공한다.
3. Java Complier
    - AAPT로 생성된 R.java 파일과 aidl로 생성된 java interface, 소스코드를 컴파일하여 .class 파일로 만들어준다. 여기서 proguard 과정이 일어난다.
4. DEX (Dalvik Executable)
    - .class 파일들과 3rd party libraries 클래스 파일들을 모두 dalvik byte code를 위한 .dex파일로 만들어준다. (안드로이드 실행파일 포맷)
5. apkbuilder
    - AAPT가 생성한 resources.ap_라는 중간 파일과 .dex 파일을 하나로 묶어 .apk로 패키징한다.
6. jarsigner
    - debug 또는 release용 keystore로 signing을 한다.
    - JAR(Java Archive, 자바 아카이브)는 여러개의 자바 클래스 파일과, 클래스들이 이용하는 관련 리소스(텍스트, 그림 등) 및 메타데이터를 하나의 파일로 모아서 자바 플랫폼에 응용 소프트웨어나 라이브러리를 배포하기 위한 소프트웨어 패키지 파일 포맷이다.
7. zipalign (release mode)
    - Release mode로 sign하면 zipalign tool을 사용하여 align 시켜준다.
    - 최종 .apk를 aligning 하면 application이 device에서 running시에 memory usage를 감소시킨다.

**레퍼런스**

[https://androes.tistory.com/176](https://androes.tistory.com/176)

[https://eunplay.tistory.com/50](https://eunplay.tistory.com/50)

[https://developer.android.com/guide/components/aidl?hl=ko](https://developer.android.com/guide/components/aidl?hl=ko)

[https://fineworld.tistory.com/entry/AIDL-이란](https://fineworld.tistory.com/entry/AIDL-%EC%9D%B4%EB%9E%80)

[https://m.blog.naver.com/PostView.nhn?blogId=zoomen1004&logNo=110178388128&proxyReferer=https%3A%2F%2Fwww.google.com%2F](https://m.blog.naver.com/PostView.nhn?blogId=zoomen1004&logNo=110178388128&proxyReferer=https%3A%2F%2Fwww.google.com%2F)

[https://ko.wikipedia.org/wiki/JAR_(파일_포맷)](https://ko.wikipedia.org/wiki/JAR_(%ED%8C%8C%EC%9D%BC_%ED%8F%AC%EB%A7%B7))
