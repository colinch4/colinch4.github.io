---
layout: post
title: "[javascript] Marionette.js에서 사용되는 서버 사이드 템플릿(Server-side Template) 라이브러리와 엔진은 어떤 것들이 있는가?"
description: " "
date: 2023-11-29
tags: [javascript]
comments: true
share: true
---

1. Handlebars.js
   - Handlebars.js는 Marionette.js에서 가장 많이 사용되는 템플릿 엔진입니다.
   - 이 엔진을 사용하면 HTML 템플릿을 작성하고 템플릿에 데이터를 바인딩할 수 있습니다.
   - Handlebars.js는 간단하고 직관적인 문법을 가지며, 조건문, 반복문 등을 지원합니다.

2. Underscore.js
   - Marionette.js는 Underscore.js 라이브러리를 기반으로 동작합니다.
   - Underscore.js는 매우 강력한 템플릿 엔진이며, 템플릿 작성에 유용한 다양한 기능을 제공합니다.
   - 예를 들어, 조건문, 반복문, 변수 사용 등을 템플릿 안에서 실현할 수 있습니다.

3. Lodash
   - Lodash는 Underscore.js의 개선된 버전으로 Marionette.js에서도 사용할 수 있습니다.
   - Lodash는 전체적인 성능 향상과 다양한 기능 추가를 제공합니다.
   - 또한 Lodash의 템플릿 엔진 기능은 Marionette.js에서 사용하기 편리한 형태로 지원됩니다.

이 외에도 Marionette.js는 Dust.js, EJS, Hogan.js 등 다양한 템플릿 엔진을 사용할 수 있습니다. 선택하고자 하는 템플릿 엔진은 개발자의 선호도나 요구사항에 따라 다를 수 있습니다. 프로젝트의 특성에 맞는 템플릿 엔진을 선택하여 사용하면 됩니다.

참고 문서:
- [Marionette.js 공식 문서](https://marionettejs.com/)
- [Handlebars.js 문서](https://handlebarsjs.com/)
- [Underscore.js 문서](https://underscorejs.org/)
- [Lodash 문서](https://lodash.com/docs/4.17.15)