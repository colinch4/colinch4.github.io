---
layout: post
title: "[c++] 트리의 잎 노드 수 세기(Count the Number of Leaf Nodes in a Tree)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

이번에는 C++로 작성된 이진 트리(Binary Tree)에서 잎 노드(Leaf Node)의 수를 세는 방법에 대해 알아보겠습니다.

```cpp
#include <iostream>
using namespace std;

// 이진 트리 노드를 나타내는 구조체
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// 이진 트리의 잎 노드 수를 세는 재귀 함수
int countLeafNodes(Node* root) {
    if (root == nullptr) {
        return 0;
    } else if (root->left == nullptr && root->right == nullptr) {
        return 1;
    } else {
        return countLeafNodes(root->left) + countLeafNodes(root->right);
    }
}

int main() {
    // 이진 트리 생성
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);

    // 잎 노드 수 출력
    cout << "잎 노드 수: " << countLeafNodes(root) << endl;

    return 0;
}
```

위 코드는 이진 트리를 구현하고, 재귀 함수를 사용하여 잎 노드의 수를 계산하는 예제입니다. 재귀 함수 `countLeafNodes`는 트리의 각 노드를 순회하면서 잎 노드인지 확인하고, 잎 노드일 경우에만 카운트를 증가시킵니다.

이 코드를 실행하면 잎 노드의 수가 출력됩니다.

이러한 방식으로 C++에서 이진 트리의 잎 노드 수를 세는 기본적인 방법을 구현할 수 있습니다.

## 참고 자료
- [GeeksforGeeks: Count Leaf Nodes in a Binary Tree](https://www.geeksforgeeks.org/write-a-c-program-to-get-count-of-leaf-nodes-in-a-binary-tree/)
- [cplusplus.com](http://www.cplusplus.com/)