---
layout: post
title: "[java] ARIA (Advanced Encryption Standard + Round Key Addition) 암호화 알고리즘"
description: " "
date: 2023-12-11
tags: [java]
comments: true
share: true
---

ARIA(Advanced Encryption Standard + Round Key Addition)는 대한민국의 과학기술정보통신부와 국가암호평가위원회(NIS)에 의해 국가 보안 강도 수준의 국내 표준으로 지정된 **블록 암호화** 알고리즘입니다.

## ARIA 특징

ARIA는 **128비트** 블록 크기를 가지며, **128, 192, 256** 비트의 키 길이를 지원합니다. 이런 특징 때문에 다양한 보안 요구 사항에 맞추어 사용될 수 있습니다.

ARIA는 **128비트 블록 암호**로, **128, 192, 256 비트**의 키 길이를 가지므로, 총 3개의 라운드 제어 키를 생성합니다.

## ARIA 알고리즘 단계

ARIA는 다음과 같은 단계로 암호화를 수행합니다:
1. **라운드 키 확장 (Round Key Expansion)** - 입력된 키를 확장하여 라운드 키를 생성합니다.
2. **라운드 함수 (Round Function)** - 라운드 함수는 입력으로 들어온 텍스트에 라운드 키를 추가합니다.
3. **라운드 변환 (Round Transformation)** - 라운드 변환은 바이트 단위의 비선형 변환과 카이퍼 변환을 수행합니다.
4. **라운드 키 추가 (Round Key Addition)** - 라운드 키를 암호문에 더합니다.

```java
// ARIA 암호화 예제
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;

public class ARIAEncryptionExample {
    public static void main(String[] args) throws Exception {
        // 1. 키 생성
        KeyGenerator keyGen = KeyGenerator.getInstance("ARIA");
        keyGen.init(256);
        SecretKey secretKey = keyGen.generateKey();

        // 2. 암호화
        Cipher cipher = Cipher.getInstance("ARIA");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        byte[] input = "ARIA Encryption Example".getBytes();
        byte[] encrypted = cipher.doFinal(input);
        System.out.println("암호화된 메시지: " + new String(encrypted));
    }
}
```

ARIA 알고리즘은 현재 국내 정보보안 분야에서 널리 사용되고 있으며, 안전하고 신뢰할 수 있는 암호화 알고리즘으로 인정받고 있습니다.

이상으로 ARIA 암호화 알고리즘에 대한 간략한 설명을 마치겠습니다.

## 참고 자료
- [국가암호평가위원회(NIS)](https://www.nis.go.kr/)
- "ARIA (An Algorithm for Cryptographic Message Syntax)" 논문: [https://tools.ietf.org/html/rfc5794](https://tools.ietf.org/html/rfc5794)