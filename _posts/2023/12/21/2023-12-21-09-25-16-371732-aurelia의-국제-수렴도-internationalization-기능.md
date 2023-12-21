---
layout: post
title: "[javascript] Aurelia의 국제 수렴도 (internationalization) 기능"
description: " "
date: 2023-12-21
tags: [javascript]
comments: true
share: true
---

Aurelia는 국제 수렴도 (Internationalization) 기능을 통해 다국어 지원을 손쉽게 구현할 수 있습니다. 이 기능을 사용하면 애플리케이션을 여러 언어로 번역하여 사용자에게 본국어 또는 선호하는 언어로 표시할 수 있습니다.

## Aurelia 국제 수렴도 (Internationalization) 플러그인

Aurelia 애플리케이션에서 국제 수렴도를 구현하려면 `i18n` 플러그인을 사용해야 합니다. 이 플러그인을 사용하면 다국어 지원을 간단하게 추가할 수 있습니다.

```javascript
import { I18N } from 'aurelia-i18n';
```

## 텍스트 번역

Aurelia에서 텍스트를 번역하려면 `t`나 `t.bind` 바인딩을 사용하여 표시할 텍스트를 지정합니다.

```javascript
<span>${"welcomeMessage" & t}</span>
<p t.bind="description"></p>
```

## 번역 파일

각 언어별로 텍스트를 관리하기 위해 `locales` 폴더에 언어별 JSON 파일을 만들어야 합니다.

```json
// en.json
{
  "welcomeMessage": "Welcome to our app!",
  "description": "This is the description."
}
```
```json
// es.json
{
  "welcomeMessage": "¡Bienvenido a nuestra aplicación!",
  "description": "Esta es la descripción."
}
```

## 사용자 언어 변경

사용자가 언어를 변경하려면 `i18n` 객체를 사용하여 언어를 설정합니다.

```javascript
this.i18n.setLocale('es');
```

Aurelia의 국제 수렴도 기능을 사용하면 애플리케이션을 전 세계 사용자에게 손쉽게 제공할 수 있습니다.

## 참고 자료
- [Aurelia i18n Plugin Documentation](https://aurelia.io/docs/plugins/i18n)
- [Aurelia i18n Github Repository](https://github.com/aurelia/i18n)