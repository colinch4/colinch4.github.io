---
layout: post
title: "[c++] 가장 가까운 잎 노드까지의 거리(Distance to the Nearest Leaf Node)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

이 문제는 이진 트리에서 주어진 노드에서 가장 가까운 잎 노드까지의 거리를 찾는 문제입니다.

## 문제 설명

주어진 이진 트리에서 노드의 값을 나타내는 정수가 주어집니다. 이때, 각 노드에서 가장 가까운 잎 노드까지의 거리를 찾아 반환해야 합니다.

## 알고리즘 설명

가장 가까운 잎 노드까지의 거리를 찾기 위해 우선적으로 최단 거리를 갱신할 변수를 초기화합니다. 그 후에 깊이 우선 탐색(DFS)을 통해 현재 노드에서 잎 노드까지의 거리를 찾습니다. 이 때, 왼쪽 서브트리와 오른쪽 서브트리에 대해서도 같은 과정을 반복하여 가장 가까운 잎 노드까지의 거리를 찾아냅니다.

아래는 C++로 작성된 가장 가까운 잎 노드까지의 거리를 구하는 예시 코드입니다.

```cpp
#include <iostream>
#include <algorithm>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

int distanceToNearestLeaf(TreeNode* root) {
    if (!root) return 0;

    if (!root->left && !root->right) return 1;

    int leftDistance = distanceToNearestLeaf(root->left);
    int rightDistance = distanceToNearestLeaf(root->right);

    return std::min(leftDistance, rightDistance) + 1;
}
```

## 마무리

이 문제를 해결하기 위해 기본적인 이진 트리 구조와 DFS 알고리즘을 활용해 가장 가까운 잎 노드까지의 거리를 구할 수 있었습니다. 위의 예시 코드를 활용하여 트리 구조에서 가장 가까운 잎 노드까지의 거리를 쉽게 구할 수 있습니다.

## 참고 자료
- [GeeksforGeeks](https://www.geeksforgeeks.org/distance-nearest-leaf-node-binary-tree/)
- [LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/)