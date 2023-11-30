---
layout: post
title: "[java] Apache Commons Collections의 데이터 압축 및 암호화 기능"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 Java용 유용한 라이브러리 모음입니다. 이 라이브러리는 데이터 구조 및 다양한 유틸리티 기능을 제공하여 개발자가 더 효율적으로 작업할 수 있도록 도와줍니다. 이 중에서 데이터 압축과 암호화와 관련된 기능을 살펴보겠습니다.

## 1. 데이터 압축

Apache Commons Collections는 데이터 압축 기능을 제공하는 여러 클래스를 포함하고 있습니다. 한 가지 유용한 클래스는 `BZip2CompressorOutputStream`입니다. 이 클래스를 사용하면 BZip2 알고리즘을 사용하여 데이터를 압축할 수 있습니다.

다음은 `BZip2CompressorOutputStream`를 사용하여 텍스트 파일을 압축하는 간단한 예제 코드입니다.

```java
import org.apache.commons.compress.compressors.bzip2.BZip2CompressorOutputStream;

import java.io.*;

public class DataCompressionExample {
    public static void main(String[] args) {
        try {
            FileInputStream inputFile = new FileInputStream("input.txt");
            FileOutputStream compressedFile = new FileOutputStream("compressed.bz2");
            BZip2CompressorOutputStream compressorOutputStream = new BZip2CompressorOutputStream(compressedFile);

            byte[] buffer = new byte[1024];
            int len;
            while ((len = inputFile.read(buffer)) != -1) {
                compressorOutputStream.write(buffer, 0, len);
            }

            inputFile.close();
            compressorOutputStream.close();
            compressedFile.close();

            System.out.println("Compression complete.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

위의 예제 코드에서 `input.txt` 파일을 읽어와 `compressed.bz2` 파일로 BZip2 알고리즘을 사용하여 압축하고 있습니다.

## 2. 데이터 암호화

데이터 암호화는 개인 정보 보호 및 보안에 매우 중요한 역할을 합니다. Apache Commons Collections는 데이터 암호화 기능을 제공하는 `CipherOutputStream` 클래스를 포함하고 있습니다. 이 클래스를 사용하면 입출력 스트림을 암호화하여 데이터를 안전하게 전송할 수 있습니다.

다음은 `CipherOutputStream`를 사용하여 텍스트 파일을 AES 알고리즘을 사용하여 암호화하는 예제 코드입니다.

```java
import javax.crypto.Cipher;
import javax.crypto.CipherOutputStream;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.*;
import java.security.AlgorithmParameters;
import java.security.spec.KeySpec;

public class DataEncryptionExample {
    public static void main(String[] args) {
        try {
            String password = "mypassword";
            FileInputStream inputFile = new FileInputStream("input.txt");
            FileOutputStream encryptedFile = new FileOutputStream("encrypted.bin");

            // Generate key from password
            SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
            KeySpec spec = new PBEKeySpec(password.toCharArray(), "salt".getBytes(), 65536, 256);
            SecretKey secretKey = new SecretKeySpec(factory.generateSecret(spec).getEncoded(), "AES");

            // Initialize cipher
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            cipher.init(Cipher.ENCRYPT_MODE, secretKey);
            AlgorithmParameters params = cipher.getParameters();

            // Write initialization vector to encrypted file
            byte[] iv = params.getParameterSpec(javax.crypto.spec.IvParameterSpec.class).getIV();
            encryptedFile.write(iv);

            // Encrypt data and write to encrypted file
            CipherOutputStream cipherOutputStream = new CipherOutputStream(encryptedFile, cipher);
            byte[] buffer = new byte[1024];
            int len;
            while ((len = inputFile.read(buffer)) != -1) {
                cipherOutputStream.write(buffer, 0, len);
            }

            inputFile.close();
            cipherOutputStream.close();
            encryptedFile.close();

            System.out.println("Encryption complete.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위의 예제 코드에서는 `input.txt` 파일을 AES 암호화 알고리즘을 사용하여 `encrypted.bin` 파일로 암호화하고 있습니다. 암호화에 사용되는 키는 사용자의 비밀번호로부터 생성되며, 암호화에 사용되는 초기화 벡터 (IV)는 암호문과 함께 저장되어야 합니다.

## 결론

Apache Commons Collections를 사용하면 데이터 압축 및 암호화와 같은 중요한 작업을 쉽게 수행할 수 있습니다. 이러한 기능은 데이터의 안전한 전송 및 보호에 매우 유용하며, 개발자에게 시간과 노력을 절약할 수 있는 도구입니다.

참고 자료:
- Apache Commons Collections 공식 문서: [https://commons.apache.org/proper/commons-collections/](https://commons.apache.org/proper/commons-collections/)
- Oracle Java 문서: [https://docs.oracle.com/javase/8/docs/api/](https://docs.oracle.com/javase/8/docs/api/)