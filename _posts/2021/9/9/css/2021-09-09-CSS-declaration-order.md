---
layout: post
title: "[css] CSS 선언 순서"
description: " "
date: 2021-09-09
tags: [css]
comments: true
share: true
---

## CSS 선언 순서

## NHN 코딩 컨벤션

속성을 선언할 때는 그 쓰임새가 레이아웃과 관련이 큰 것에서 시작하여 레이아웃과 무관한 것 순서로 선언한다. 관련 속성은 대표되는 속성 다음으로 선언하며, 아래에 표기된 순서대로 선언한다.

1. 레이아웃
   1. display
   2. visibility
   3. overflow
   4. float
   5. clear
   6. position
   7. top
   8. right
   9. bottom
   10. left
   11. zindex
2. Box
   1. width
   2. height
   3. margin
   4. padding
   5. border
3. 배경
   1. background
4. 폰트
   1. font,color
   2. etter-spacing
   3. text-align
   4. text-decoration
   5. text-indent
   6. verticalalign
   7. white-space 
5. 기타
   1. 위에 언급되지 않은 나머지 속성들로 폰트의 관련 속성 이후에 선언하며, 기타 속성 내의 선언 순서는 무관함
   2. 밴더속성과 핵속성은 해당 속성 뒤에 선언

## Web Standards Darum

1. display (표시)
2. overflow (넘침)
3. float (흐름)
4. position (위치)
5. width&height (크기)
6. padding&margin (간격)
7. border (테두리)
8. background (배경)
9. color/font (글꼴)
10. animation
11. 기타

## Code Guide - CSS Declaration order

관련 속성 선언은 다음 순서로 그룹핑한다.

1. Positioning (포지셔닝)
2. Box model (박스 모델)
3. Typographic (타이포그라피)
4. Visual (시각 효과)
5. Misc (기타)

문서의 정상적인 흐름에서 엘리먼트를 없앨 수 있고, 박스 모델 관련 스타일들을 재정의할 수 있기 때문에 포지션 관련 선언이 가장 먼저 온다. 박스 모델이 그 다음에 오며 해당 엘리먼트의 크기와 위치를 지정한다.

나머지는 이전의 두 섹션에 영향을 주지 않거나 엘리먼트의 내부에서만 필요한 내용이기 때문에 마지막에 온다.

전체 속성 목록과 순서는 [Bootstrap property order for Stylelint](https://github.com/twbs/stylelint-config-twbs-bootstrap/blob/master/css/index.js) 를 참조하라.

## Wrap up

 구글링을 통해 얻을 수 있는 다른 CSS 선언 순서도 유사한 형태를 띄고 있다. 정리하자면 밖에서부터 안쪽의 순서로 선언하길 권장하고 있다. 엘리먼트의 폰트 컬러, 배경 색상을 지정해뒀다 하더라도 화면에 보일것이냐 보이지 않을것이냐가 더욱 중요한 사항이기 때문일 것이다.

 작업할 때는 구조와 스타일을 분리하기 때문에 위치 선정, 사이즈, 색상 디테일까지 하나의 엘리먼트에 선언하는 경우는 거의 없다. 그래도 CSS를 선언할 때 최소한의 순서를 숙지해두면 작성과 유지보수에 모두 도움을 줄 수 있을것이다.



## 📖 Reference

* [NHN 마크업 코딩 컨벤션](https://nuli.navercorp.com/sharing/fe/coding)
* [Web Standard Darum](http://darum.daum.net/convention/css/css_convention)
* [Code Guide by Mark Otto](https://codeguide.co/#css-declaration-order)
* [CSS property order](https://gist.github.com/awkale/ad46e2ade70e833fa178#file-css-order-md)

