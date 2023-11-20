---
layout: post
title: "[JAVA] Encryption"
description: " "
date: 2021-11-18
tags: [java]
comments: true
share: true
---

AES 128
----
[Online Encryption](https://www.devglan.com/online-tools/aes-encryption-decryption)

Error Solve - [Base64 Error](https://qastack.kr/programming/13109588/encoding-as-base64-in-java)
~~~~java
import java.util.Base64;

//Base64의 정적메소드 이용
byte[] encodedBytes = Base64.getEncoder().encode("Test".getBytes());
System.out.println("encodedBytes " + new String(encodedBytes));
byte[] decodedBytes = Base64.getDecoder().decode(encodedBytes);
System.out.println("decodedBytes " + new String(decodedBytes));

//문자열로 직접 출력
String encodeBytes = Base64.getEncoder().encodeToString((userName + ":" + password).getBytes());
~~~~


Sample Code
~~~java
public Key getAESKey() throws Exception {
    String iv;
    Key keySpec;

    String key = "1234567890123456";
    iv = key.substring(0, 16);
    byte[] keyBytes = new byte[16];
    byte[] b = key.getBytes("UTF-8");

    int len = b.length;
    if (len > keyBytes.length) {
       len = keyBytes.length;
    }

    System.arraycopy(b, 0, keyBytes, 0, len);
    keySpec = new SecretKeySpec(keyBytes, "AES");

    return keySpec;
}

// 암호화
public String encAES(String str) throws Exception {
    Key keySpec = getAESKey();
    Cipher c = Cipher.getInstance("AES/CBC/PKCS5Padding");
    c.init(Cipher.ENCRYPT_MODE, keySpec);
    byte[] encrypted = c.doFinal(str.getBytes("UTF-8"));
    String enStr = new String(Base64.encodeBase64(encrypted));

    return enStr;
}

// 복호화
public String decAES(String enStr) throws Exception {
    Key keySpec = getAESKey();
    Cipher c = Cipher.getInstance("AES/CBC/PKCS5Padding");
    c.init(Cipher.DECRYPT_MODE, keySpec);
    byte[] byteStr = Base64.decodeBase64(enStr.getBytes("UTF-8"));
    String decStr = new String(c.doFinal(byteStr), "UTF-8");

    return decStr;
}
~~~
