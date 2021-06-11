---
layout: post
title: " DNS - Name Resolution"
description: " "
date: 2021-06-11
tags: [cs]
comments: true
share: true
---

# DNS - Name Resolution

* Two types of name resolution mechanism 
  * Recursive queries
  * Iterative(non-recursive) queries

=> 쿼리의 유형을 무엇으로 할 건지는 DNS query의 하나의 비트를 통해 결정된다. 
 
## Recursive query (by default) example

![recursive](https://user-images.githubusercontent.com/38216027/71319900-af945280-24e7-11ea-9536-2ebec154fa27.png)

1. Requesting host 는 상대방의 도메인은 알지만 ip는 모르는 상태로 주변에 있는 Local DNS server 에게 쿼리 메시지를 보낸다. 

2. 만약 Local DNS server가 상대방에 대한 ip address 를 캐싱한 상태라면 바로 응답을 하겠지만, 그게 아니라면 Root DNS server에게 쿼리 메시지를 보낸다. 

3. Root DNS server는 resolution을 해주지 않고 상대방 도메인과 관련된 TLD DNS server에 쿼리 메시지를 보낸다. 

4. 만약 TLD DNS server가 상대방에 대한 ip address를 캐싱한 상태라면 바로 응답을 Root DNS server에 하겠지만, 그게 아니라면 Authoritative DNS server에게 쿼리 메시지를 보낸다.

5. 해당 Authoritative DNS server 는 상대방에 대한 정보를 가지고 있으므로 상대방의 ip address 를 TLD DNS server에 보낸다. 

6. TLD DNS server는 상대방 ip address 를 Root DNS server 에 보낸다. 

7. Root DNS server는 상대방 ip address 를 Local DNS server 에 보낸다. 

8. Local DNS server는 상대방 ip address 를 Requesting host 에 보낸다.

> 장점 

1. 일관성을 높인다. 
2. 캐싱이 되있다면 빠른 방법이다. 

> 단점 

1. 캐싱이 안되어 있으면 느리다. 

## Iterative query example 

1. Requesting host 는 상대방의 도메인은 알지만 ip는 모르는 상태로 주변에 있는 Local DNS server 에게 쿼리 메시지를 보낸다. 

2. 만약 Local DNS server 가 상대방에 대한 ip address 를 캐싱한 상태라면 바로 응답을 하겠지만, 그게 아니라면 Root DNS server에게 쿼리 메시지를 보낸다. 

3. Root DNS server는 resoulution을 해주지 않고 상대방 도메인과 관련된 TLD DNS server의 주소를 Local DNS server에게 보낸다. 

4. Local DNS server는 관련 TLD DNS server에게 쿼리 메시지를 보낸다.  

5. 만약 TLD DNS server가 상대방에 대한 ip address 를 캐싱한 상태라면 바로 응답을 Local DNS server에 하겠지만, 그게 아니라면 상대방 도메인과 관련된 Authoritative DNS server의 Local DNS server에게 보낸다.

6. Local DNS server는 관련 Authoritative DNS server에게 쿼리 메시지를 보낸다.  

7. 해당 Authoritative DNS server는 상대방에 대한 정보를 가지고 있으므로 상대방의 ip address 를 Local DNS server에 보낸다. 

8. Local DNS server는 상대방 ip address 를 Requesting host 에 보낸다.

![iterative](https://user-images.githubusercontent.com/38216027/71319932-f2eec100-24e7-11ea-960e-04e3758da385.png)

> 장점 

1. 바로 Local DNS server 로 응답을 할 수 있기 때문에 빠르다. 

> 단점 

1. 상대적으로 recursive 방식보다 iterative 방식이 응답을 많이 받기 때문에,
<br>: 큰 규모의 Local DNS 서버에서만 iterative 를 쓴다. 
<br>: default는 recursive query

2. 또한 일관적이지 않다.  