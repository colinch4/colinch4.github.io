---
layout: post
title: "[파이썬] PyCharm 구동시 에러 해결"
description: " "
date: 2021-06-17
tags: [python]
comments: true
share: true
---


## PyCharm 구동시 에러 해결

오늘 (2019.12.08 현재) 갑자기 JetBrains 계열 프로그램이 모두 구동이 되지 않는 문제가 있었다. 대수롭지 않게 생각하고 있었는데, 리부팅을 해도 해결이 되지 않고, 설정파일을 지우고 새롭게 만들기도 하고, PyCharm를 새로 설치하기도 하였지만 문제가 해결되지 않았다.

툴이 필요한 시점에 툴이 말썽을 부리니 여간 신경이 쓰였다. 다행히 아래 해결방법이 통하여 문제를 해결할 수 있었다. JetBrains 계열 제품들은 미리 통신 포트를 점유하고 있는 모양인데, 이 포트를 다른 프로그램에서 미리 점유하고 있을 경우 생기는 문제 같았다. 해결법은 네트워크를 초기화하는 방법이었다. 프롬프트에서 실행하면 되고, 당연하게도 관리자 권한이 필요하다. 실행 후 리부팅하고, 문제가 해결되었다.

```cmd
netsh winsock reset
```

주기적으로 이 문제가 반복되고 있다.

> To lock the folders IDE is starting a server on localhost, it tries to bind on the first available port between 6942 and 6991, this exception is thrown if IDE was not able to bind on any of the ports in this range. All 50 ports are unlikely to be already used on a machine, so it appears to be a networking issue or some security software which doesn't permit the IDE to bind on any port in this range even on the localhost interface.

해당포트가 비어있긴 한데, 오에스에서 재활용하지 않고, 계속 뒷번호를 주는 것 같긴 하다. 어쨌거나 최선의 해결책은 위와 같이 네트워크 설정을 초기화한 후, 리부팅이라고 하니, 여간 귀찮은 게 아니다.

* [Critical Internal Error on Startup of IntelliJ IDEA: "Cannot Lock System Folders"](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360004973960-Critical-Internal-Error-on-Startup-of-IntelliJ-IDEA-Cannot-Lock-System-Folders-)
* [Start Failed, Internal error: recovering IDE to the working state after the critical startup error](https://intellij-support.jetbrains.com/hc/en-us/articles/360007568559)

<vue-disqus/>
