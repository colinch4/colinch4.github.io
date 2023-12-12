---
layout: post
title: "[c++] 서브트리에 속하는 트리 모든 노드의 합(Sum of All Nodes in a Subtree)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

우리는 각 노드의 값과 해당 노드의 자식 노드들을 저장하는 이진 트리 자료구조를 가정합니다. 다음은 C++로 작성된 트리의 각 노드에 대한 클래스 정의입니다.

```c++
class TreeNode {
public:
    int val;
    vector<TreeNode*> children;
};
```

이제 각 노드를 루트로 하는 서브트리의 합을 계산하기 위한 재귀 함수를 작성할 수 있습니다. 다음은 C++로 작성된 예시 코드입니다.

```c++
int sumSubtree(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }

    int sum = root->val;
    for (auto child : root->children) {
        sum += sumSubtree(child);
    }

    return sum;
}
```

위의 코드는 각 노드를 루트로 하는 서브트리의 합을 재귀적으로 계산합니다. 빈 서브트리는 0을 반환하고, 그렇지 않은 경우 해당 노드의 값과 모든 자식 노드들을 루트로 하는 서브트리의 합을 더하여 반환합니다.

우리는 이제 이 코드를 사용하여 주어진 트리의 모든 노드에 대한 서브트리의 합을 찾을 수 있습니다.