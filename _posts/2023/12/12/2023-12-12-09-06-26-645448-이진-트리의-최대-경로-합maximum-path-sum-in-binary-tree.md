---
layout: post
title: "[c++] 이진 트리의 최대 경로 합(Maximum Path Sum in Binary Tree)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

이진 트리(Binary Tree)에서 최대 경로 합(Maximum Path Sum)을 구하는 문제는 코딩 인터뷰나 알고리즘 문제 해결과정에서 자주 등장하는 문제 중 하나입니다. 주어진 이진 트리에서 가장 큰 합을 갖는 경로를 찾는 문제로, 동적 프로그래밍(Dynamic Programming)이나 재귀 알고리즘(Recursion)을 활용하여 해결할 수 있습니다.

### 문제 설명

주어진 이진 트리에서 최대 경로 합을 찾는 문제는 아래와 같은 요구 사항을 가집니다.

- 이진 트리의 각 노드는 정수값을 포함하고 있습니다.
- 이진 트리의 루트 노드부터 잎 노드까지 이어진 경로 중, 합이 가장 큰 경로를 찾아야 합니다.

### 문제 해결 방법

주어진 이진 트리에서 최대 경로 합을 찾는 문제는 재귀적인 방법을 통해 해결할 수 있습니다. 아래의 두가지 방법을 이용하여 문제를 해결할 수 있습니다.

1. **하향식(Divide and Conquer) 방법**:
   - 각 노드에서부터 시작하는 최대 경로 합을 계산하여 루트 노드를 포함한 경로의 합을 찾습니다.

2. **상향식(Bottom-up) 방법**:
   - 각 노드의 하위 트리에서 가능한 최대 경로 합을 계산하여 루트 노드까지 올라가며 최대 경로 합을 찾습니다.

아래는 C++로 작성된 이진 트리의 최대 경로 합을 구하는 코드 예제 입니다.

```c++
#include <iostream>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int max_sum = INT_MIN;
        max_sum = std::max(max_sum, findMaxPath(root, max_sum));
        return max_sum;
    }

    int findMaxPath(TreeNode* node, int& max_sum) {
        if (node == nullptr) {
            return 0;
        }
        int left = std::max(findMaxPath(node->left, max_sum), 0);
        int right = std::max(findMaxPath(node->right, max_sum), 0);
        int curr_sum = node->val + left + right;
        max_sum = std::max(max_sum, curr_sum);
        return node->val + std::max(left, right);
    }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);

    Solution sol;
    std::cout << "Maximum path sum: " << sol.maxPathSum(root) << std::endl;

    delete root->left;
    delete root->right;
    delete root;

    return 0;
}
```

위의 코드 예제는 `TreeNode` 구조체를 이용하여 이진 트리를 정의하고, `Solution` 클래스에서 `maxPathSum` 함수를 통해 최대 경로 합을 구하는 방법을 보여줍니다.

### 마치며

이진 트리의 최대 경로 합을 구하는 문제는 동적 프로그래밍이나 재귀 알고리즘을 활용하여 효과적으로 해결 가능합니다. 위의 예제 코드를 통해 해당 문제에 대한 해결 방법을 이해할 수 있으며, 실제로 알고리즘 문제 해결이나 코딩 인터뷰에서 유용하게 활용될 수 있습니다.