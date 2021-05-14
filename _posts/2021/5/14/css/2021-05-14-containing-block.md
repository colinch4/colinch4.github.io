---
layout: post
title: "[css] Containing Block"
description: " "
date: 2021-05-14
tags: [css]
comments: true
share: true
---


# Containing Block
Containing Block은 어떤 element의 Position과 Size를 식별하는 기준이 된다.

****일반적으로**** Containing Block은 부모의 Content 영역이다.

아래의 코드를 보자.

```css
.*container* {
  width: 100px;
  height: 100px;
  background-color: lime;
}
.*item* {
  width: 80%;
  height: 80%;
  background-color: red;
}
```

위의 코드의 경우 container 영역의 content 영역의 사이즈의 80%인 80px를 너비와 높이로 갖게 된다.

Containing Block은 box-sizing과 상관이 없다.  
아래의 코드는 width : 100px 에 content + padding + border가 합산된 결과가 들어가는데,  
padding에 의해서 content 영역은 80x80 이다. 따라서 item은 64x64가 된다.

```css
* {
  box-sizing: border-box;
}
.*container* {
  width: 100px;
  height: 100px;
  padding: 10px;
  background-color: lime;
}
.*item* {
  width: 80%;
  height: 80%;
  background-color: red;
}
```

## Containing Block 식별

Containing Blockdmf 식별하는 방법은 해당 element의 position 속성에 따라 다르다.

`position: static/relative/sticky`  
위와 같은 position을 가지고 있는 경우에는 가장 가까운 조상 element 중에 Block Container 또는 Formatting Context element 이다.

`postion: absolute`  
가장 가까운 조상 중에서 position: static이 아닌 요소를 Containing Block으로 삼는다.

`position : fixed`  
: viewport를 Containig block으로 삼는다.

## Size

offset properties, box-model properties는 `%` 단위를 사용하는 경우에는 Containing Block에 의해서 기준(100%)가 정해진다.

- offset properties : top/bottom/left/right
- box-model properties : height/width/padding/margin

height/top/bottom -> 이 properties는 Containing Block의 height의 값에 따라 결정된다.

width/left/right/paddsing/margin -> Containing Block의 width의 값에 따라 결정된다.

****주의할점****  
padding-top/bottom, margin-top/bottom의 경우에도 width를 기준으로 `%`가 계산된다.

```css
.*container* {
  width: 100px;
  height: 100px;
  background-color: lime;
}
.*item* {
  width: 80%;
  height: 80%;
  background-color: red;
}
```


#CSS/Containing-block