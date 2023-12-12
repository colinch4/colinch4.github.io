---
layout: post
title: "[c++] 이진 검색 트리에서 두 노드 간의 거리(Find Distance Between Two Nodes in BST)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

이진 검색 트리(Binary Search Tree, 이하 BST)는 노드들이 정렬되어 있는 트리 구조이다. BST에서 두 노드 간의 거리를 계산하는 문제는 주어진 두 노드의 공통 조상을 찾고, 공통 조상을 기준으로 두 노드까지의 거리를 계산하는 것을 포함한다. 이 문제는 보편적으로 이진 트리를 사용하여 해결된다.

## 이진 검색 트리에서 노드 간의 거리 계산 알고리즘

이진 검색 트리에서 두 노드 `node1`과 `node2` 간의 거리를 계산하기 위해서 다음과 같은 단계를 따른다:

1. BST에서 공통 조상을 찾는다.
2. `node1`과 `node2`까지의 거리를 계산한다.

### 공통 조상 찾기

두 노드 간의 거리를 계산하려면 먼저 두 노드의 공통 조상을 찾아야 한다. 공통 조상을 찾는 가장 일반적인 방법은 다음과 같다:

```c++
Node* findLCA(Node* root, int n1, int n2) {
    if (root == NULL) return NULL;

    if (root->data > n1 && root->data > n2) {
        return findLCA(root->left, n1, n2);
    }
    if (root->data < n1 && root->data < n2) {
        return findLCA(root->right, n1, n2);
    }

    return root;
}
```

### 노드까지의 거리 계산하기

두 노드 간의 거리를 계산하기 위해서는 경로의 길이를 측정해야 한다. 이를 위해 다음과 같은 방법을 사용할 수 있다:

```c++
int findLevel(Node* root, int k, int level) {
    if (root == NULL) return -1;
    if (root->data == k) return level;
    int left = findLevel(root->left, k, level + 1);
    if (left == -1) return findLevel(root->right, k, level + 1);
    return left;
}

int findDistance(Node* root, int n1, int n2) {
    Node* lca = findLCA(root, n1, n2);
    int d1 = findLevel(lca, n1, 0);
    int d2 = findLevel(lca, n2, 0);

    return d1 + d2;
}
```

이제 두 노드 간의 거리를 계산할 수 있다.

## 마치며

이진 검색 트리에서 두 노드 간의 거리를 계산하는 문제는 공통 조상을 찾고, 그것을 활용하여 노드까지의 거리를 계산하는 것으로 해결된다. 위의 알고리즘을 통해 효율적으로 문제를 해결할 수 있으며, 다른 BST 문제에도 응용 가능하다.

참고문헌:
- GeeksforGeeks. "Find distance between two nodes of a Binary Tree"