---
layout: post
title: "[c++] 이진 탐색 트리에서 k번째로 작은 요소(Kth Smallest Element in a BST)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

이진 탐색 트리(Binary Search Tree)에서 k번째로 작은 요소를 찾는 문제는 중위 순회(Inorder Traversal)를 활용하여 해결할 수 있습니다. 중위 순회는 트리를 왼쪽 서브트리, 루트 노드, 오른쪽 서브트리 순서로 방문하여 노드 값을 읽는 방식입니다. 중위 순회를 사용하면 노드들을 오름차순으로 방문할 수 있기 때문에 k번째로 작은 요소를 쉽게 찾을 수 있습니다.

## 문제 설명

주어진 이진 탐색 트리의 루트 노드와 자연수 k가 주어졌을 때, 해당 트리에서 k번째로 작은 요소를 찾아 반환하는 문제입니다.

## 중위 순회를 활용한 해결 방법

이 문제를 해결하기 위해 중위 순회로 BST를 순회하면서 순회한 노드의 값을 기록하고 k번째로 작은 값을 반환하면 됩니다.

다음은 C++로 작성된 중위 순회를 활용한 이진 탐색 트리에서 k번째로 작은 요소를 찾는 예제 코드입니다.

```cpp
// 이진 탐색 트리 노드 정의
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> s;
        TreeNode* p = root;
        int count = 0;
        
        while (p != NULL || !s.empty()) {
            if (p != NULL) {
                s.push(p);
                p = p->left;
            } else {
                p = s.top();
                s.pop();
                count++;
                if (count == k) {
                    return p->val;
                }
                p = p->right;
            }
        }
        
        return -1; // k번째로 작은 요소가 없을 경우 예외 처리
    }
};
```

이 코드는 중위 순회를 스택을 활용하여 구현한 예제로, BST를 순회하면서 k번째로 작은 요소를 반환합니다.

## 마치며

이와 같이 중위 순회를 활용하여 이진 탐색 트리에서 k번째로 작은 요소를 찾을 수 있습니다. 이러한 방식을 활용하여 효율적으로 BST를 탐색하고 원하는 요소를 찾아낼 수 있습니다.

참고 문헌: [LeetCode - Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)