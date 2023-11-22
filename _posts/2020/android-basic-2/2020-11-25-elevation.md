---
layout: post
title: "[안드로이드] elevation 란"
description: " "
date: 2020-11-25
tags: [android]
comments: true
share: true
---

  
  뷰의 테두리에 그림자 효과를 주는 xml 속성
  
  api 21 이상부터 적용되는 구글의 머테리얼 디자인이다.
  
  해당 뷰를 z축으로 이동시켜 그림자 효과를 줄 수 있다.
  
  단순히 xml에서 뷰의 elevation 속성에 값을 주면 된다.
  
  ```
  android:elevation="8dp"
  ```

## 설정 했으나 안보이는 경우
  
  1. 뷰의 background가 투명인경우. -> 색을 설정해 준다.
  
  2. 뷰 주위에 영역이 없는 경우 -> 상위 뷰에 paddding을 주거나, 뷰에 margin을 줘서 영역을 확보한다!
  
  
#### padding과 margin을 이용하여 뷰의 일부분만 그림자가 보이도록 할 수도 있다!
  
  
