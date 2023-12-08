---
layout: post
title: "[java] NAT(Network Address Translation)와 포트 포워딩"
description: " "
date: 2023-12-08
tags: [java]
comments: true
share: true
---

이번 글에서는 NAT(Network Address Translation)과 포트 포워딩에 대해 알아볼 것입니다.

## NAT(Network Address Translation)

NAT(Network Address Translation)은 사설 네트워크에서 공인 IP 주소를 공유하기 위해 사용되는 기술입니다. 이를 통해 여러 사설 IP 주소를 하나의 공인 IP 주소로 변환하여 외부와 통신할 수 있게 됩니다. NAT는 주로 가정이나 회사와 같은 내부 네트워크에서 사용되어 인터넷에 연결하는 데 사용됩니다.

## 포트 포워딩

포트 포워딩은 공인 IP 주소와 사설 IP 주소 간의 연결을 활성화하는 데 사용됩니다. 포트 포워딩을 설정하면 공인 IP 주소로 들어오는 특정 포트의 요청을 사설 IP 주소로 전달함으로써 외부에서 내부로의 연결을 가능하게 합니다. 예를 들어, 웹 서버를 내부 네트워크에 운영하고자 하는 경우, 공인 IP 주소로 들어오는 80번 포트에 대한 요청을 내부 웹 서버의 사설 IP 주소로 전달함으로써 외부에서 해당 서버에 접속할 수 있게 됩니다.

## 예시

아래는 NAT와 포트 포워딩이 적용된 예시입니다.

**NAT 설정**

```java
ip nat inside source static 192.168.1.2 203.0.113.5
```

**포트 포워딩 설정**

```java
ip nat inside source static tcp 192.168.1.3 80 interface Ethernet0 80
```

많은 고객이 인터넷을 이용하기 위해 NAT와 포트 포워딩을 사용하고 있습니다. 이를 통해 효율적으로 네트워크를 관리하고 보안을 유지할 수 있습니다.

자세한 내용은 다음 참고 자료를 확인하시기 바랍니다.

[Understanding NAT, PAT, and Basic NAT Configuration](https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/26704-nat-faq-00.html)

[Port Forwarding Explained](https://www.howtogeek.com/66214/how-to-forward-ports-on-your-router/)

이상으로 NAT와 포트 포워딩에 대한 이해를 마치겠습니다. 감사합니다.