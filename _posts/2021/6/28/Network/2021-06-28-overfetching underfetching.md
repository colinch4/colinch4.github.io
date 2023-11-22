---
layout: post
title: "[네트워크] overfetching underfetching"
description: " "
date: 2021-06-28
tags: [network]
comments: true
share: true
---


## overfetching

너무 많은 데이터를 가져오는 것을 의미한다. 즉 어떤 endpoint에 요청을 보내고 그 응답을 받았을 때 내가 원하는 데이터에 비해 큰 데이터가 오기 때문에 낭비가 발생하는 부분을 의미한다.

## underfetching

한 번의 한 endpoint로의 요청은 내가 원하는 데이터를 충분히 가져올 수 없기 때문에 그 다음의 요청을 보낼 수 밖에 없다.

## background

완벽한 세계, 즉 처음부터 모든걸 계획하여 적절한 endpoint에 api를 제대로 만들어 놨다면 위의 두 용어는 필요하지 않다.

하지만 어플리케이션을 확장할 때 위 두가지 용어가 생기는데. 예를들면 개발자가 예상한 대역폭(bandwidth)를 넘어서거나, 예상한 request보다 많은 api를 만들어야 하는 상황에서다.
