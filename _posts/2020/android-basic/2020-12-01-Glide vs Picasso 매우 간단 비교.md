---
layout: post
title: "[안드로이드 기초] Glide vs Picasso 매우 간단 비교"
description: " "
date: 2020-12-01
tags: [android]
comments: true
share: true
---


- Picasso는 Bitmap포맷을 ARGB_8888로 사용하고 Glide는 Bitmap포맷을 RGB_565를 사용한다.
- RGB_565는 ARGB_8888에 비해서 화질은 떨어지지만 메모리 용량을 50% 적게 사용한다.
- Picasso는 1920x1080크기의 원본 이미지를 메모리로 가져와서 GPU에서 실시간으로 리사이징해서 768x432의 ImageView에 할당한다. 하지만 Glide는 바로 768x432크기로 메모리에 가져와서 ImageView로 할당 시키기때문에 메모리 사용량이 적다.
- 만약 1920x1080 이미지를 다시 384x216크기의 ImageView로 로드한다고 할 경우 Picasso는 이미 원본 이미지를 그대로 가지고 있지만 Glide는 또하나의 384x216 크기의 이미지파일을 캐시하게 된다.
- Glide는 같은 이미지를 다른 크기의 ImageView에 로드한다는 이유로 2번의 이미지 다운로드와 리사이징 작업이 필요하게 된다.
- OutOfMemoryError Glide가 더 많이 해결
