---
layout: post
title: "[c++] 트리의 노드 수 세기(Count the Number of Nodes in a Tree)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

이번에는 C++로 이진 트리의 노드 수를 세는 방법에 대해 알아보겠습니다.

## 이진 트리 클래스 정의

먼저 이진 트리를 표현하는 클래스를 정의합니다.

```c++
class TreeNode {
public:
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
```

이진 트리의 각 노드는 정수 값을 저장하는 `val` 멤버와 좌측 자식 노드를 가리키는 `left` 멤버, 우측 자식 노드를 가리키는 `right` 멤버를 가지고 있습니다.

## 트리의 노드 수 세는 함수 구현

이제 이진 트리의 노드 수를 세는 함수를 구현해보겠습니다.

```c++
int countNodes(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }
    return 1 + countNodes(root->left) + countNodes(root->right);
}
```

이 함수는 재귀적으로 트리의 각 노드를 방문하면서 노드 수를 누적합니다. 노드가 없는 경우에는 0을 반환하고, 노드가 있는 경우에는 좌측과 우측 서브트리의 노드 수를 더한 후 1을 더하여 반환합니다.

## 예제

이제 이진 트리를 생성하고 노드 수를 세는 예제를 살펴보겠습니다.

```c++
int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    int nodeCount = countNodes(root);
    std::cout << "노드 수: " << nodeCount << std::endl;

    return 0;
}
```

이 예제에서는 1을 루트로 갖는 이진 트리를 생성하고, `countNodes` 함수를 사용하여 이 트리의 노드 수를 구합니다.

이상으로 C++를 사용하여 이진 트리의 노드 수를 세는 방법에 대해 알아보았습니다.

## 참고 자료

- [GeeksforGeeks - Count the number of nodes in a binary tree](https://www.geeksforgeeks.org/count-the-number-of-nodes-in-a-binary-tree/)