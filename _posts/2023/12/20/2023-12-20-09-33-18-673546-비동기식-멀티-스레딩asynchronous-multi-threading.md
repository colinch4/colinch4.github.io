---
layout: post
title: "[c언어] 비동기식 멀티 스레딩(asynchronous multi-threading)"
description: " "
date: 2023-12-20
tags: [c언어]
comments: true
share: true
---

컴퓨터 프로그래밍에서 멀티 스레딩은 여러 작업을 동시에 실행할 수 있는 기술입니다. **비동기식 멀티 스레딩**은 이러한 멀티 스레딩을 실현하는 방법 중 하나입니다. 비동기식 멀티 스레딩은 동시에 여러 작업을 실행할 수 있는데, 각각의 작업은 서로 독립적으로 실행될 수 있습니다.

## 비동기식 멀티 스레딩의 장점

비동기식 멀티 스레딩을 사용하면 다음과 같은 장점을 얻을 수 있습니다:
- **성능 향상**: 여러 작업을 병렬로 실행하여 전체적인 성능을 향상시킬 수 있습니다.
- **응답성 향상**: 한 작업이 블록되어 있을 때에도, 다른 작업이 계속해서 실행될 수 있어 응답성이 향상됩니다.
- **자원 효율성**: 멀티 스레딩을 통해 자원을 효율적으로 활용할 수 있습니다.

## 비동기식 멀티 스레딩의 예제

```c
#include <stdio.h>
#include <pthread.h>

void *print_message(void *ptr) {
  char *message = (char *)ptr;
  printf("%s \n", message);
}

int main() {
  pthread_t thread1, thread2;
  char *message1 = "Thread 1";
  char *message2 = "Thread 2";
  
  pthread_create(&thread1, NULL, print_message, (void *)message1);
  pthread_create(&thread2, NULL, print_message, (void *)message2);

  pthread_join(thread1, NULL);
  pthread_join(thread2, NULL);
}
```

위 코드는 C 언어로 작성된 간단한 예제로, 두 개의 스레드를 생성하고 각각의 스레드에서 메시지를 출력하는 함수를 실행하는 것을 보여줍니다.

비동기식 멀티 스레딩은 병렬 처리를 통해 성능을 향상시키고, 프로그램의 응답성과 자원 효율성을 높일 수 있는 강력한 기술입니다.

## 참고 자료
- [GeeksforGeeks - Multi Threading in C](https://www.geeksforgeeks.org/multithreading-c-2/)
- [IBM Knowledge Center - Asynchronous Multithreading](https://www.ibm.com/support/knowledgecenter/en/ssw_aix_72/com.ibm.aix.performance/asynchronous_multithreading.htm)