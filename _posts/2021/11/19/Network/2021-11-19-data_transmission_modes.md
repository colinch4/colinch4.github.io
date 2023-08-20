---
layout: post
title: "[Network] Data Transmission Modes"
description: " "
date: 2021-11-19
tags: [Network]
comments: true
share: true
---

## Data Transmission Modes

`데이터 전송 방식`은 총 세가지로 나뉘는데, 이는 데이터가 전송되는 방향을 기준으로 나눈 것이다.

1. 단(单)방향 통신 `Simplex`
1. 반（半）이중 통신 `Half-Duplex`
1. 전（全）이중 통신 `Full-Duplex`

### Table of Contents
* [Simplex](#simplex)
* [Half-Duplex](#half-duplex)
* [Full-Duplex](#full-duplex)

## Simplex
Simplex 는 단방향 통신으로 데이터는 한가지 방향으로만 움직인다.  
- Simplex : Simple, Single

Transmitter 와 Receiver 가 명확히 구분되어 Transmitter 는 송신만 Receiver 는 수신만 가능하다.  

![Simplex](https://user-images.githubusercontent.com/48475824/120071589-0f266280-c0cb-11eb-91cf-24be2a3e185d.gif)

- T : Transmitter
- R : Receiver

### Examples
- Keyboard
- Monitor
- Mouse
- Radio
- TV-Station

## Half-Duplex  
Half-Duplex 는 Semi-Duplex 라고도 불리운다.  
Transmitter 는 Receiver 가 되기도 Receiver 는 Transmitter 가 되기도 한다. 하지만 전송이 이루어지는 동안 한 방향으로만 이루어 져야 한다. 즉, 데이터가 전송될 동안 한쪽은 Receiver 이든 Transmitter 이든 한 역할만 담당해야 한다.  

이를 시각화 하자면 아래와 같다.  

![Half-Duplex](https://user-images.githubusercontent.com/48475824/120071838-e5217000-c0cb-11eb-9f16-871146b6af9f.gif)

### Examples
- Internet Browser
- Walkie-Talkies

## Full-Duplex  
Full-Duplex(양방향 통신)는 양쪽에서 동시에(simultaneously) 송수신이 가능한 방식이다.  

![Full-Duplex](https://user-images.githubusercontent.com/48475824/120072129-223a3200-c0cd-11eb-84e8-4c00f428b0fa.gif)

### Example
- Telephone


[↑ return to TOC](#table-of-contents)