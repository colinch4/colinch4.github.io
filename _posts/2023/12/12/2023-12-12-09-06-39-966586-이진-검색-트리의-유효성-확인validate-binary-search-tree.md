---
layout: post
title: "[c++] 이진 검색 트리의 유효성 확인(Validate Binary Search Tree)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

이번에는 이진 검색 트리의 유효성을 확인하는 방법에 대해 알아보겠습니다. 이진 검색 트리(Binary Search Tree, BST)는 왼쪽 서브트리의 모든 노드가 현재 노드보다 작고, 오른쪽 서브트리의 모든 노드가 현재 노드보다 큰 조건을 만족하는 이진 트리입니다. 따라서 주어진 트리가 유효한 BST인지를 확인하는 문제는 일반적인 코딩 인터뷰나 알고리즘 문제에서 자주 등장하는 주제입니다.

## 문제 설명

주어진 이진 검색 트리가 유효한지를 확인하는 문제는 주어진 트리가 유효한 BST의 조건을 만족하는지를 확인하는 것입니다. 즉, 모든 노드의 왼쪽 자식 노드는 현재 노드보다 작고, 모든 오른쪽 자식 노드는 현재 노드보다 큰 값을 가져야 합니다.

## 해결 방법

주어진 이진 검색 트리가 유효한 BST인지를 확인하는 방법은 여러 가지가 있습니다. 가장 간단한 방법은 inorder traversal(중위 순회)을 이용하여 노드들을 방문하는 것입니다. 이때, 이전 노드의 값을 저장하고 현재 노드와 비교하여 BST의 조건을 만족하는지 확인할 수 있습니다.

다음은 C++로 작성된 예시 코드입니다.

```cpp
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        stack<TreeNode*> st;
        TreeNode* prev = nullptr;
        
        while (root != nullptr || !st.empty()) {
            while (root != nullptr) {
                st.push(root);
                root = root->left;
            }
            
            root = st.top();
            st.pop();
            if (prev != nullptr && prev->val >= root->val) {
                return false;
            }
            
            prev = root;
            root = root->right;
        }
        
        return true;
    }
};
```

위에서 설명한 방법은 BST의 조건을 만족하는지 확인하는 효율적인 방법 중 하나입니다.

## 결론

이진 검색 트리의 유효성 확인은 BST의 조건을 만족하는지를 확인하는 문제로, 중위 순회를 이용하여 노드를 방문하며 BST의 조건을 만족하는지 확인할 수 있습니다. 위에서 제시한 예시 코드를 참고하여 문제를 해결해보시기 바랍니다.