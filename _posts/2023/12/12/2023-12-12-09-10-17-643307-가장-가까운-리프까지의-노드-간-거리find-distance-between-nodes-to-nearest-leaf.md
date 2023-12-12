---
layout: post
title: "[c++] 가장 가까운 리프까지의 노드 간 거리(Find Distance Between Nodes to Nearest Leaf)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

이번에는 이진 트리에서 두 노드 간의 거리를 계산하는 문제를 다루어 보겠습니다. 특히, 이진 트리의 루트 노드로부터 주어진 두 노드로 이뤄진 경로에서 가장 가까운 리프 노드까지의 거리를 구하는 문제입니다. 아래에서는 C++로 이를 해결하는 방법에 대해 소개하겠습니다.

## 문제 이해

먼저, 주어진 이진 트리의 구조를 이해해야 합니다. 이진 트리는 각 노드가 최대 두 개의 자식 노드를 가지는 트리 형태의 자료 구조입니다. 주어진 이진 트리에서 두 노드 P와 Q 간의 가장 가까운 리프까지의 거리를 계산해야 합니다.

## 코드 구현

이를 위해 아래와 같이 C++로 구현할 수 있습니다.

```c++
#include <iostream>
#include <algorithm>

// 이진 트리의 노드 구조 정의
struct Node {
    int val;
    Node* left;
    Node* right;
    Node(int x) : val(x), left(NULL), right(NULL) {}
};

// 트리의 높이를 계산하는 함수
int height(Node* root) {
    if (root == NULL) {
        return 0;
    } else {
        return 1 + std::min(height(root->left), height(root->right));
    }
}

// 노드 간의 거리를 계산하는 함수
int findDistanceToNearestLeaf(Node* root, int x) {
    if (root == NULL) {
        return 0;
    }
    
    if (root->val == x || (h := findDistanceToNearestLeaf(root->left, x)) > 0 || (h := findDistanceToNearestLeaf(root->right, x)) > 0) {
        int l = height(root->left);
        int r = height(root->right);
        return std::min(l, r) + 1;
    }
    
    return 0;
}
```

위 코드는 이진 트리의 각 노드를 나타내는 구조를 정의하고, 두 노드 간의 거리를 계산하는 `findDistanceToNearestLeaf` 함수를 구현한 것입니다.

## 예시

아래는 위 함수를 이용하여 거리를 계산하는 예시입니다.

```c++
Node* root = new Node(1);
root->left = new Node(2);
root->right = new Node(3);
root->left->left = new Node(4);
root->left->right = new Node(5);
root->right->left = new Node(6);
root->right->right = new Node(7);
  
int x = 4;
std::cout << "Distance to nearest leaf: " << findDistanceToNearestLeaf(root, x) << std::endl;
```

## 결론

위 예시에서는 C++을 사용하여 주어진 이진 트리에서 두 노드 간의 거리를 계산하는 방법을 알아보았습니다. 주어진 두 노드 P와 Q 간의 경로 중에서 가장 가까운 리프 노드까지의 거리를 찾는 문제는 전형적인 이진 트리 문제로, 트리의 구조와 재귀적인 방법을 사용하여 해결할 수 있습니다.

## 참고 자료

- GeeksforGeeks, "Find distance between two nodes of a Binary Tree", [링크](https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/)
- LeetCode, "Closest Leaf in a Binary Tree", [링크](https://leetcode.com/problems/closest-leaf-in-a-binary-tree/)
- C++ Reference, "std::min", [링크](https://en.cppreference.com/w/cpp/algorithm/min)