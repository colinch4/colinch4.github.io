---
layout: post
title: "[css] aspect ratio image"
description: " "
date: 2021-05-14
tags: [css]
comments: true
share: true
---

# aspect ratio image
이미지를 특정 비율로 만드는 방법.

padding과 margin property는 `%` 값이  containing block의 `width`에 의해서 계산된다.

즉,
block 속성의 element에 padding-bottom을 60%라고 명시를 하는 경우, width의 40% 크기의 height를 가지게 됨.

height: 0; 으로 추가적으로 설정하면 컨텐츠의 영역은 없고 해당 패딩 영역만 가지기 때문에, padding-top에 명시한 비율의 크기를 가지는 elment가 생김.

```html
<div class="container">
 
</div>
```


```css
.container {
  background-color: red;
  width: 100%;
  padding-top: 100%; /* 1:1 Aspect Ratio */
  position: relative; /* If you want text inside of it */
}

.container {
  padding-top: 56.25%; /* 16:9 Aspect Ratio (divide 9 by 16 = 0.5625) */
}

.container {
  padding-top: 75%; /* 4:3 Aspect Ratio (divide 3 by 4 = 0.75) */
}
```


카드를 만들때, 썸네일 영역을 만들고 싶을때 이러한 방식을 사용할 수 있다.


```css
.card {
	.thumbnail {
		height: 0;
		padding-top: 75%;
		background-image: url('');
		// .. background 속성 ..
	}
}

```


#CSS