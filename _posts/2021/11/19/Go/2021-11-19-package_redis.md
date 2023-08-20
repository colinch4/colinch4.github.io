---
layout: post
title: "[Go] Package redis"
description: " "
date: 2021-11-19
tags: [Go]
comments: true
share: true
---

## Package redis

### Table of Contents
* redis 코드 열어보기
    * [reids.Options](#redis.options)

### redis.Options

```go
type Options struct {
  Network   string
  Addr      string
  Dialer    func(ctx context.Context, network, addr string) (net.Conn, error)
  OnConnect func(*Conn) error
  Password  string
  DB        int

  MaxRetries         int
  MinRetryBackoff    time.Duration
  MaxRetryBackoff    time.Duration
  DialTimeout        time.Duration
  ReadTimeout        time.Duration
  WriteTimeout       time.Duration
  MinIdleConns       int
  MaxConnAge         time.Duration
  PoolTimeout        time.Duration
  IdleTimeout        time.Duration
  IdleCheckFrequency time.Duration

  readOnly           bool
  TLSConfig          *tls.Config
  Limiter            Limiter
}
```
* Network
    * Network 타입을 정해줄 수 있다.
        * tcp
        * unix
    * Default 값은 tcp로 설정되어 있다.
* Addr
    * host 의 port 주소.
* Dialer
    * 새로운 network connection을 만든다.
    * network 와 addr 옵션을 정해줄 수 있다.
* OnConnect
* Password
    * 선택 사항.
* DB
    * 서버에 연결할 데이터 선택.
    * Redis는 16개의 DB를 제공. (0~15)
* MaxRetries
    * 몇 번 retry를 시도할 것인지 최대 횟수를 정한다.
    * Default 로는 실패시 retry 를 시도 하지 않도록 설정되어 있다.
* MinRetryBackoff
    * Default : 8 milliseconds
    * Disable 하려면 값을 -1 로 설정.
* MaxRetryBackoff
    * Default: 512 milliseconds
    * Disable 하려면 값을 -1 로 설정.
* DialTimeout
    * 새 connection 시 Dial timeout 설정.
    * 단위는 초
    * Default : 5 s
* ReadTimeout
    * Timeout for socket reads.
    * Timeout에 도달하게 되면 blocking 되는 대신 명령들은 실패로 종결된다.
    * Default : 3 s
    * Disable : -1
* WriteTimeout
    * Timeout for socket writes.
    * Timeout에 도달하게 되면 blocking 되는 대신 명령들은 실패로 종결된다.
    * Default : ReadTimeout
* PoolSize
    * socket connections의 최대 개수
* MinIdelConns
    * new connection 이 느릴때 유용하게 사용된다.
* MaxConnAge
    * Default : aged connections 를 닫지 않는다.
* PoolTimeout
    * 모든 Connections 이 busy 일 경우 error를 바로 리턴하기 전에 client에게 주는 대기시간.
    * Default : ReadTimeout + 1 s
* IdleTimeout
    * Default : 5 min
    * Disable : -1
* IdleCheckFrequency
    * Default : 1 min
    * Disable : -1
* readOnly
    * slave nodes의 read only 쿼리 설정 (on/off)
* TLSConfig
* Limiter

[↑ return to TOC](#table-of-contents)