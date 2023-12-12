---
layout: post
title: "[c++] 이진 트리 노드의 수준 순회(Level Order Traversal in Binary Tree)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

이진 트리를 노드의 수준 순서대로 방문하는 방법을 수준 순회(또는 레벨 순회)라고 합니다. 이 방법은 각 노드를 해당 레벨에 따라 방문하며, 동일한 레벨에 있는 노드들을 왼쪽에서 오른쪽 순서로 방문합니다. 이 방법을 사용하여 트리를 탐색하면, 루트 노드부터 시작하여 각 레벨에 따라 노드를 방문하게 됩니다.

## 이진 트리 노드의 수준 순회 구현

```c++
#include <iostream>
#include <queue>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

void levelOrderTraversal(Node* root) {
    if (root == nullptr) {
        return;
    }

    queue<Node*> q;
    q.push(root);

    while (!q.empty()) {
        Node* current = q.front();
        q.pop();
        cout << current->data << " ";

        if (current->left) {
            q.push(current->left);
        }
        if (current->right) {
            q.push(current->right);
        }
    }
}

int main() {
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);

    cout << "Level Order Traversal: ";
    levelOrderTraversal(root);

    return 0;
}
```

위의 코드는 C++을 사용하여 이진 트리를 노드의 수준 순서대로 탐색하는 방법을 보여줍니다. `levelOrderTraversal` 함수는 루트 노드부터 시작하여 각 레벨에 따라 노드를 방문합니다. 이를 위해 큐를 사용하여 노드를 순서대로 저장하고 방문하는 방식을 사용합니다.

## 결론

이진 트리의 노드를 수준 순서대로 방문하는 방법은 큐를 이용하여 각 레벨에 있는 노드를 순서대로 처리함으로써 구현할 수 있습니다. 수준 순회는 트리의 구조를 탐색하거나 트리의 높이를 계산하는 등 다양한 문제에 유용하게 활용될 수 있습니다.

## 참고 자료
- GeeksforGeeks: [Level Order Traversal](https://www.geeksforgeeks.org/level-order-tree-traversal/)