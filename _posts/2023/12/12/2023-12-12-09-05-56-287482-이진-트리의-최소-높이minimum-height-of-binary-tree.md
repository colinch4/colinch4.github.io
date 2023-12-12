---
layout: post
title: "[c++] 이진 트리의 최소 높이(Minimum Height of Binary Tree)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

주어진 이진 트리의 최소 높이를 찾기 위해서는 균형 잡힌 트리를 생성하는 알고리즘이 필요합니다. 균형 잡힌 트리란 모든 리프 노드까지의 거리가 가능한 한 동일한 트리를 의미합니다.

이진 트리의 최소 높이를 찾기 위한 관련 코드는 아래와 같습니다.

```c++
#include <iostream>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

int calculateHeight(TreeNode* root) {
    if (root == NULL) {
        return 0;
    }
    
    return 1 + max(calculateHeight(root->left), calculateHeight(root->right));
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    
    int minHeight = calculateHeight(root);
    cout << "Minimum height of the binary tree: " << minHeight << endl;
    
    return 0;
}
```

위 코드는 이진 트리의 최소 높이를 구하는 방법을 보여줍니다. calculateHeight 함수는 주어진 노드를 루트로 하는 서브트리의 높이를 계산하고, 이를 통해 균형을 맞춘 트리의 최소 높이를 구할 수 있습니다.

이 외에도 이진 트리의 최소 높이를 찾는 다른 방법이 있을 수 있으며, 실제 상황에 적합한 알고리즘을 선택하는 것이 중요합니다.

참고 문헌:
- https://leetcode.com/problems/minimum-height-tree/
- https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/