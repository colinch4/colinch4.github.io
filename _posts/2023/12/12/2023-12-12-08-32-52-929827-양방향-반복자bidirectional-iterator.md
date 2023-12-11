---
layout: post
title: "[c++] 양방향 반복자(bidirectional iterator)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

양방향 반복자는 일부 컨테이너, 예를 들어 리스트(List)와 덱(Deque)에서 사용됩니다. 이러한 반복자를 사용하여 컨테이너의 요소를 순회하고 조작할 수 있습니다. 양방향 반복자를 사용하면 리스트와 같은 구조에서 요소를 삽입, 삭제, 역순으로 탐색하는 등 다양한 작업을 수행할 수 있습니다.

다음은 양방향 반복자의 간단한 예시입니다.

```c++
#include <iostream>
#include <list>

int main() {
    std::list<int> numbers = {1, 2, 3, 4, 5};

    // 양방향 반복자를 사용한 순차적인 순회
    std::list<int>::iterator it;
    for (it = numbers.begin(); it != numbers.end(); ++it) {
        std::cout << *it << " ";
    }

    // 양방향 반복자를 사용한 역방향 순회
    std::list<int>::reverse_iterator rit;
    for (rit = numbers.rbegin(); rit != numbers.rend(); ++rit) {
        std::cout << *rit << " ";
    }

    return 0;
}
```

양방향 반복자를 사용하여 리스트를 순차적으로 탐색하고, 역순으로 탐색하는 예제입니다.

양방향 반복자는 컨테이너의 구조를 변경하지 않고도 순차적으로 탐색하고 조작할 수 있는 강력한 도구입니다. 이를 통해 프로그래머는 다양한 상황에서 유연하고 효율적으로 컨테이너를 다룰 수 있습니다.

더 자세한 내용은 [C++ 양방향 반복자](https://en.cppreference.com/w/cpp/named_req/BidirectionalIterator)를 참고하세요.