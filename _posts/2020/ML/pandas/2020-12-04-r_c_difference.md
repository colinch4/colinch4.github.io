---
layout: post
title: "[pandas] DataFrame row와 column 차이"
description: " "
date: 2020-12-04
tags: [pandas]
comments: true
share: true
---


# DataFrame row와 column 차이

|    추출 방법     | row(행) | column(열) |
| :--------------: | :-----: | :--------: |
|    단일 추출     |    O    |     X      |
|     Slicing      |    X    |     O      |
|  Fancy indexing  |    O    |     X      |
| boolean indexing |    O    |     X      |

