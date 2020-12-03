---
layout: post
title: "[안드로이드] RecyclerView 란"
description: " "
date: 2020-11-25
tags: [Android]
comments: true
share: true
---

  
  
  리스트 뷰의 장단점을 보완한 고급 위젯이다. 
  
  한정된 수의 뷰를 유지하여 매우 효율적으로 스크롤 할 수 있는 큰 데이터 세트를 표시하기 위한 컨테이너
  
  
## RecyclerView 클래스
  
  리사이클러 뷰 클래스에는 서브클래스인 LayoutManager, ItemDecoration, ItemAnimation 세가지 클래스가 있다.
  
  LayoutManager를 이용하여 뷰에 있는 아이템을 배치하고 관리하며, Adapter클래스를 이용하여 데이터 세트에 맞는 ViewHolder 클래스를 구현할 수 있다.
  
  ItemDecoration 과 ItemAnimation 서브클래스를 이용하여 뷰를 제어할 수 있다.
  

## Adapter 클래스
  
  어댑터 클래스는 ViewHolder 클래스를 이요한 데이터 세트의 정의에 따라 UI를 선택하여 보여줍니다.
  
  ListView 클래스는 데이터의 종류에 따라 베이스 어댑터를 상속한 어댑터를 이용하지만, 리사이클러 뷰 클래스는 뷰홀더 클래스의 정의에 따라 UI를 선택하고
  
  데이터를 처리해야한다. 
  
  다음 3가지 메서드를 구현해야한다!
  
  - onCreateViewHolder : 뷰홀더를 생성하고, 뷰를 붙여주는 부분
  - onBindViewHolder : 재활용하는 뷰를 호출하여 실행하는 메서드. 데이터를 뷰에 결합한다.
  - getItemCount : 데이터의 개수를 반환합니다.
  
  
## LayoutManager 클래스
  
  뷰를 그리는 방법을 정의합니다. 리스트 뷰는 수직형태의 리스트만 지원하지만, 리사이클러 뷰는 수직뿐만 아니라 다양한 리스트 형태를 지원합니다.
  
  - LinearLayoutManager : 수직 또는 수평 방향의 리스트로 나타낸다.
  - GridLayoutManager : 그리드 형식으로 항목을 표시
  - StaggeredGridLayoutManager : 지그재그 그리드형태로 항목을 표시 
  

## ItemAnimator 클래스
  
  사용자가 직접 정의할 수 있는 애니매이션 효과 클래스
  
  RecyclerView.ItemAnimator 를 상속한 클래스에서 setItemAnimator 메서드를 오버라이딩하면 된다.


## ItemDecoration 클래스
  
  리사이클러 뷰 내의 아이템을 꾸밀 수 있는 클래스
  
  동적으로 리스트에 디바이더를 추가할 수 있다. 각 아이템 사이의 간격을 조정할 수 있음.
  
  RecyclerView.ItemDecoration 을 상속한 클래스에서 getItemOffset 메서드를 오버라이딩하면 된다.
