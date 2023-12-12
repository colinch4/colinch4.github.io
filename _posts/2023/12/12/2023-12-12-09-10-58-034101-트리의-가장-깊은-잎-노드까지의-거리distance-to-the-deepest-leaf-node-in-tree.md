---
layout: post
title: "[c++] 트리의 가장 깊은 잎 노드까지의 거리(Distance to the Deepest Leaf Node in Tree)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

트리(Tree) 자료 구조에서 가장 깊은 잎 노드까지의 거리를 찾는 문제는 깊이 우선 탐색(DFS, Depth-First Search)을 사용하여 해결할 수 있습니다.

## 문제 설명

주어진 루트 노드로부터 가장 깊은 잎 노드까지의 거리를 계산합니다. 이를 위해 다음과 같은 단계를 따릅니다:

1. DFS를 사용하여 루트 노드부터 각 노드까지의 깊이를 계산합니다.
2. 루트 노드부터 시작하여 각 노드마다 자식 노드까지의 거리를 계산하여 최대 거리를 저장합니다.

이러한 방식으로 모든 노드에 대해 거리를 계산하고, 그 중 최대 거리가 가장 깊은 잎 노드까지의 거리가 됩니다.

## 예시

다음은 C++로 작성된 예시 코드입니다:

```c++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    vector<TreeNode*> children;
    TreeNode(int x) : val(x) {}
};

int maxDistance = 0;

int calculateDepth(TreeNode* root) {
    if (root == NULL) {
        return 0;
    }

    int maxDepth = 0;
    for (TreeNode* child : root->children) {
        maxDepth = max(maxDepth, calculateDepth(child));
    }

    return 1 + maxDepth;
}

void calculateDistance(TreeNode* root, int depth) {
    if (root == NULL) {
        return;
    }

    maxDistance = max(maxDistance, depth);
    for (TreeNode* child : root->children) {
        calculateDistance(child, depth + 1);
    }
}

int main() {
    TreeNode* root = new TreeNode(1);
    TreeNode* child1 = new TreeNode(2);
    TreeNode* child2 = new TreeNode(3);
    TreeNode* grandchild = new TreeNode(4);
    root->children.push_back(child1);
    root->children.push_back(child2);
    child2->children.push_back(grandchild);

    int depth = calculateDepth(root); // calculate the depth of the tree
    calculateDistance(root, 0); // calculate the distance to the deepest leaf node

    cout << "Distance to the deepest leaf node: " << maxDistance << endl;

    return 0;
}
```

위의 코드는 주어진 트리 구조에서 루트 노드로부터 가장 깊은 잎 노드까지의 거리를 계산하는 방법을 보여줍니다.

이러한 방법으로 트리의 가장 깊은 잎 노드까지의 거리를 효과적으로 찾을 수 있습니다.

## 결론

깊이 우선 탐색을 사용하여 트리의 가장 깊은 잎 노드까지의 거리를 계산할 수 있습니다. 이는 트리 자료 구조에서 자주 발생하는 문제 중 하나이며, 효율적인 알고리즘을 사용하여 해결할 수 있습니다.