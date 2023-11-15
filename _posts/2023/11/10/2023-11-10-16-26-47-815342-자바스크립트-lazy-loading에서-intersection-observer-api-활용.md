---
layout: post
title: "자바스크립트 Lazy Loading에서 Intersection Observer API 활용"
description: " "
date: 2023-11-10
tags: [javascript]
comments: true
share: true
---

최근 웹 페이지의 성능을 향상시키기 위해 이미지나 동영상 등의 리소스를 지연로딩하는 방법이 주목받고 있습니다. 이러한 기술을 구현하기 위해 Intersection Observer API를 사용하는 것이 효과적입니다. 이번 블로그 포스트에서는 자바스크립트 Lazy Loading에서 Intersection Observer API를 활용하는 방법에 대해 알아보겠습니다.

## Intersection Observer API란?

Intersection Observer API는 HTML 요소와 뷰포트(화면) 사이의 교차(intersection)를 관찰(observe)하는 API입니다. 이 API를 사용하면 특정 요소가 뷰포트에 진입하거나 뷰포트를 벗어나는 등의 교차 이벤트를 감지할 수 있습니다. 이를 활용하여 특정 요소가 뷰포트에 진입할 때 리소스를 로딩하고, 뷰포트를 벗어날 때 리소스를 해제하는 등의 작업을 할 수 있습니다.

## Intersection Observer API를 사용한 Lazy Loading 구현 방법

1. Intersection Observer 객체 생성

   ```javascript
   const options = {
     root: null, // 기본값인 뷰포트를 기준으로 설정
     rootMargin: '0px', // 교차 이벤트를 감지할 뷰포트 영역의 마진
     threshold: 0.5 // 교차 이벤트를 감지할 요소 비율 (0~1)
   };

   const observer = new IntersectionObserver(callback, options);
   ```

2. Target 요소 관찰 시작

   ```javascript
   const target = document.querySelector('.lazy-image');

   observer.observe(target);
   ```

3. Callback 함수 정의

   ```javascript
   const callback = (entries, observer) => {
     entries.forEach((entry) => {
       if (entry.isIntersecting) {
         // 교차 이벤트 발생 시 리소스 로딩 등 필요한 작업 수행
         const lazyImg = entry.target;
         lazyImg.setAttribute('src', lazyImg.dataset.src);

         // 교차 이벤트를 더 이상 감지하지 않도록 관찰 중지
         observer.unobserve(entry.target);
       }
     });
   };
   ```

위의 방법을 사용하여 Intersection Observer API를 활용한 자바스크립트 Lazy Loading을 구현할 수 있습니다. 이렇게 하면 페이지의 리소스를 필요할 때만 로딩해서 성능을 향상시킬 수 있습니다.

더 자세한 내용은 [Intersection Observer API](https://developer.mozilla.org/ko/docs/Web/API/Intersection_Observer_API) 문서를 참고하시기 바랍니다.

#webdevelopment #javascript