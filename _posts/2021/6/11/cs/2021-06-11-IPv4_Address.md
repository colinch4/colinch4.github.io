---
layout: post
title: "IPv4 Address "
description: " "
date: 2021-06-11
tags: [cs]
comments: true
share: true
---

# IPv4 Address 

* Classful 
* CIDR(Classess Inter-Domain Routing)

# Classful IPv4 Address 

![classful](https://user-images.githubusercontent.com/38216027/71251485-d88cda00-2365-11ea-99fd-ff475643a499.png)

* 처음엔 클래스를 나눠 IP address 를 구분하곤 했다. 하지만 지금은 classless한 addressing ( 바로 CIDR ) 을 사용한다.  
* IP address는 두 부분으로 나눠진다 - network and host

* 클래스는 다섯 개의 클래스를 가지고 있다 - A, B, C, D 그리고 E
  * A, B, C 는 보편적인 unicast 할때 사용하는 addressing
  * D는 multicast(IPTV) 할 때의 addressing, E 는 future use 할 때의 addressing 

> classful 하게 나눈 이유 

![classful_address](https://user-images.githubusercontent.com/38216027/71251966-0a527080-2367-11ea-8ce0-04be31aeee8b.png)

지역마다 노드(컴퓨터)의 수가 많은 곳도 있고 적은 곳도 있을 것이다. 가령 서울은 인구 수가 많고 적어도 1대의 컴퓨터는 가정마다 있으므로 host의 수가 굉장히 많을 것이고 , 시골의 경우에는 컴퓨터가 적으므로 host의 수가 적을 것이다.
<br>따라서 하나의 라우터가 담당하는 호스트의 범위가 도시의 경우에는 많게 하고 , 시골의 경우에는 적게 하는 것이 효율적이므로 ip의 주소를 여러 클래스로 나누게 된 것이다. 

* 맨 앞에 0이면 class A 이고 따라서 network의 수는 남은 7개의 bit인 128개(2^7)이다. host 수는 24개의 bit인 16,777,216개로 하나의 네트워크당 16,777,216개의 host를 커버할 수 있다는 것이다. 이 경우는 대도시에 적합하다.

* 맨 앞에 10이면 class B 이고 네트워크의 수는 16,384(2^14)개, 하나의 네트워크가 가지는 host의 개수는 65,536(2^16)이다.

* 맨 앞에 110이면 class B 이고 네트워크의 수는 2,097,152(2^21)개, 하나의 네트워크가 가지는 host의 개수는 256(2^8)이다. 

# CIDR(Classess Inter-Domain Routing)

* 인터넷의 현재 address assignment strategy (RFC(Request For Comments)가 4632번)

* IP address의 네트워크 부분이 임의적인 길이를 가진다. 그러니깐 classful 하지 않다는 뜻.

![cidr](https://user-images.githubusercontent.com/38216027/71252707-12abab00-2369-11ea-90fd-6795af41cba8.png)

=> NIC address 가 200.23.19.5/21 인데 subnet mask 와 AND 연산을 해 subnet address 를 구한다. subnet mask는 길이가 21로 AND 연산을 하면 
subnet address 는 200.23.16.0/21 이 된다. 

# Address Aggregation ( or Supernetting) 

* 또한 route aggreagtion 이나 route summarization 으로 불린다. 

* 한 기관은 전형적으로 연속적인 주소들의 한 블록으로 할당된다.
  * 공통 prefix 가 있는 주소 범위   

* 다수의 네트워크의 한 블록 주소들은 하나의 prefix로 외부에 알려질 수 있다. (can be advertised by) 


> Before aggregation example 

![before_aggregation](https://user-images.githubusercontent.com/38216027/71256074-1e9c6a80-2373-11ea-865d-f124953b9a55.png)

=> aggregation이 되지 않아 라우터의 table에 여러 개의 네트워크 주소를 적어야만 한다. 이는 라우터의 성능을 낮춘다.     
> Address aggregation example 

![aggregation](https://user-images.githubusercontent.com/38216027/71256102-307e0d80-2373-11ea-9653-4e9d4ad9c192.png)
**200.23.16.0/20**

=> aggregation 되어 여러개의 네트워크 주소를 라우터의 table에 하나의 네트워크 주소로 통합하여 기록할 수 있다. 이는 통신할 때 라우터의 성능을 높여 더 빠르게 보낼 수 있다. 

