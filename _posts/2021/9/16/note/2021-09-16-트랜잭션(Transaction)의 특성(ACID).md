---
layout: post
title: "[용어정리] 트랜잭션(Transaction)의 특성(ACID)"
description: " "
date: 2021-09-16
tags: [용어정리]
comments: true
share: true
---

# 트랜잭션(Transaction)의 특성(ACID)

트랜잭션 : 여러 개의 오퍼레이션을 하나의 작업 단위로 묶어 주는 것

## 1. 원자성 (Automicity)

트랜잭션의 포함된 오퍼레이션(작업)들은 모두 수행되거나, 아니면 전혀 수행되지 않아야 한다.

## 2. 일관성(Consistency)

트랜잭션이 성공적인 경우에는 일관성있는 상태에 있어야 한다.

## 3. 고립성(Isolation)

각 트랜잭션은 다른 트랜잭션과 독립적으로 수행되는 것처럼 보여야 한다.

트랜잭션을 수행 시 다른 트랜잭션의 연산 작업이 끼어들지 못하도록 보장하는 것을 의미

## 4. 지속성(Durability)

성공적으로 수행된 트랜잭션의 결과는 지속성이 있어야 한다.

