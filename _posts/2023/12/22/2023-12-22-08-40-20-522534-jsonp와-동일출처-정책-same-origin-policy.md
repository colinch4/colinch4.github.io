---
layout: post
title: "[jQuery] JSONP와 동일출처 정책 (Same-Origin Policy)"
description: " "
date: 2023-12-22
tags: [jQuery]
comments: true
share: true
---

이번 글에서는 **JSONP**와 **동일출처 정책(Same-Origin Policy)**에 대해 알아보겠습니다. 먼저, 각각의 개념을 간단히 설명한 후, 두 가지의 차이점과 사용 시 주의점에 대해 설명하겠습니다.

## 동일출처 정책 (Same-Origin Policy)
동일출처 정책은 웹 보안 모델의 기본 원칙 중 하나로, 웹 페이지에서 온 리소스 요청을 특정 출처로 제한하는 보안 방식입니다. 이는 다른 출처에서 온 리소스로부터 웹페이지를 보호하여 중요한 정보가 유출되는 것을 방지합니다.

## JSONP (JSON with Padding)
JSONP는 Ajax 요청을 사용하여, 다른 도메인에 위치한 JSON 데이터에 접근하는 기술입니다. 이 방법은 동일출처 정책을 우회하기 위해 사용되며, script 태그를 이용하여 외부 도메인의 자원을 불러옵니다. JSONP는 JSON 데이터를 즉시 사용할 수 있도록패딩(padding)된 콜백 함수를 이용하여 데이터를 반환합니다.

## JSONP와 동일출처 정책 차이점
JSONP는 동일출처 정책을 우회하기 위해 사용되는 방법으로, 외부 도메인에서 데이터를 불러올 수 있습니다. 반면, 동일출처 정책은 웹 보안을 위해 다른 출처에서 오는 리소스 요청을 제한하는 보안 방식입니다.

## JSONP 사용 시 주의사항
JSONP를 사용할 때에는 보안상의 이유로 안전하지 않을 수 있으므로, 신뢰할 수 있는 출처에서만 JSONP 요청을 보내도록 주의해야 합니다.

이상으로 **JSONP**와 **동일출처 정책**에 대한 간단한 설명을 마치겠습니다. JSONP를 사용할 때에는 보안 상의 주의가 필요함을 잊지말아야 합니다.