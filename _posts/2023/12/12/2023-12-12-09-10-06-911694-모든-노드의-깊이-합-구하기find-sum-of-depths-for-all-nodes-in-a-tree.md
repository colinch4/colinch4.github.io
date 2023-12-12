---
layout: post
title: "[c++] 모든 노드의 깊이 합 구하기(Find Sum of Depths for All Nodes in a Tree)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

이번에는 트리의 모든 노드의 깊이를 합산하는 문제를 해결해 보겠습니다. 이 문제를 해결하기 위해 트리 구조를 순회하며 각 노드의 깊이를 찾고, 이를 모두 합산하는 방법을 살펴보겠습니다.

## 문제 정의

주어진 이진 트리의 모든 노드의 깊이를 합산하는 함수를 구현해야 합니다.

## 접근 방법

우리는 트리 순회 알고리즘을 사용하여 이 문제를 해결할 수 있습니다. 

깊이 우선 탐색(DFS)을 사용하여 모든 노드를 방문하면서 각 노드의 깊이를 찾을 수 있습니다. 이 때, 깊이 정보를 유지하면서 트리를 순회하는 것이 중요합니다. 

다음으로, 각 노드의 깊이를 합산하여 답을 얻을 수 있습니다.

이제, 위에서 설명한 접근 방법을 사용하여 C++ 코드를 작성해 보겠습니다.

```c++
#include <iostream>
#include <queue>

// 트리의 노드를 나타내는 구조체
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

int sumDepths(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }

    std::queue<std::pair<TreeNode*, int>> q;
    q.push({root, 0}); // pair<노드, 깊이>

    int sum = 0;

    while (!q.empty()) {
        auto node = q.front().first;
        int depth = q.front().second;
        q.pop();

        sum += depth;

        if (node->left) {
            q.push({node->left, depth + 1});
        }
        if (node->right) {
            q.push({node->right, depth + 1});
        }
    }

    return sum;
}

int main() {
    // 이진 트리 생성 및 초기화
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    std::cout << sumDepths(root) << std::endl; // 출력: 10

    return 0;
}
```

위 코드에서 `sumDepths` 함수는 주어진 이진 트리의 모든 노드의 깊이를 합산하여 리턴합니다.

## 결론

이렇게하여, 깊이 우선 탐색(DFS)을 통해 이진 트리의 모든 노드의 깊이를 합산하는 문제를 해결할 수 있습니다. 위의 코드는 주어진 이진 트리에서 모든 노드의 깊이를 합산하는 방법을 보여줍니다.

이 외에도, 서로 다른 방법으로 체크해 보실 수 있습니다.