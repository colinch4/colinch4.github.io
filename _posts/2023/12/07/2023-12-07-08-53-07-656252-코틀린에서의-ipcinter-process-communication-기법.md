---
layout: post
title: "[kotlin] 코틀린에서의 IPC(Inter-Process Communication) 기법"
description: " "
date: 2023-12-07
tags: [kotlin]
comments: true
share: true
---

IPC(Inter-Process Communication)는 여러 개의 프로세스 간에 데이터를 주고받는 기법을 의미합니다. 이는 애플리케이션들 간의 상호작용을 가능하게 해주는 중요한 개념입니다. 이번에는 코틀린에서의 IPC 기법에 대해 알아보도록 하겠습니다.

## 1. 프로세스 간 통신 방법

코틀린에서는 다양한 방법으로 IPC를 구현할 수 있습니다. 주로 사용되는 방법은 다음과 같습니다.

### 1.1. 파일을 통한 통신

파일을 통한 통신은 가장 기본적이고 간단한 IPC 방법입니다. 한 프로세스에서 파일에 데이터를 쓰고, 다른 프로세스에서 이 파일을 읽어오는 방식입니다. 코틀린에서는 파일을 다루기 위해 `java.io` 라이브러리를 사용할 수 있습니다.

### 1.2. 소켓을 통한 통신

소켓을 통한 통신은 네트워크를 통해 프로세스 간 데이터를 주고받는 방식입니다. 코틀린에서는 `java.net` 라이브러리를 사용하여 소켓 통신을 구현할 수 있습니다. TCP 소켓 또는 UDP 소켓을 사용할 수 있으며, 각각의 특성에 맞게 선택하여 사용할 수 있습니다.

### 1.3. 파이프를 통한 통신

파이프를 통한 통신은 운영체제에서 제공하는 파이프라인을 활용하여 프로세스 간 데이터를 주고받는 방식입니다. 파이프를 사용하기 위해서는 운영체제의 API를 사용해야 하므로, 코틀린에서 직접적으로 구현하기보다는 JNI를 통해 C나 C++로 작성된 코드를 호출하는 방식을 주로 사용합니다.

## 2. 예제 코드

### 2.1. 파일을 통한 통신 예제

```kotlin
import java.io.File

fun main() {
    // 데이터를 쓰는 프로세스
    val file = File("data.txt")
    file.writeText("Hello, IPC!")

    // 데이터를 읽는 프로세스
    val content = file.readText()
    println(content)
}
```

### 2.2. 소켓을 통한 통신 예제

```kotlin
import java.net.Socket

fun main() {
    // 클라이언트 프로세스
    val socket = Socket("localhost", 8080)
    val outputStream = socket.getOutputStream()
    outputStream.write("Hello, IPC!".toByteArray())
    outputStream.flush()
    socket.close()

    // 서버 프로세스
    val serverSocket = ServerSocket(8080)
    val clientSocket = serverSocket.accept()
    val inputStream = clientSocket.getInputStream()
    val buffer = ByteArray(1024)
    val bytesRead = inputStream.read(buffer)
    val content = String(buffer, 0, bytesRead)
    println(content)
    clientSocket.close()
    serverSocket.close()
}
```

### 2.3. 파이프를 통한 통신 예제

```kotlin
// Native code
#include <jni.h>

JNIEXPORT jstring JNICALL Java_com_example_NativeUtils_readPipe(JNIEnv* env, jclass clazz) {
    FILE* pipe = popen("command", "r");
    if (!pipe) return NULL;

    char buffer[128];
    std::string result = "";
    while (!feof(pipe)) {
        if (fgets(buffer, 128, pipe) != NULL)
            result += buffer;
    }

    pclose(pipe);
    return env->NewStringUTF(result.c_str());
}

// Kotlin code
class NativeUtils {
    external fun readPipe(): String

    companion object {
        init {
            System.loadLibrary("native-lib")
        }
    }
}

fun main() {
    val result = NativeUtils().readPipe()
    println(result)
}
```

## 3. 결론

코틀린에서는 파일, 소켓, 파이프 등 다양한 IPC 기법을 활용하여 프로세스 간의 통신을 구현할 수 있습니다. 각각의 특성에 맞춰 선택하여 적절한 IPC 방법을 사용하면 프로세스 간의 데이터 교환을 효율적으로 처리할 수 있습니다.