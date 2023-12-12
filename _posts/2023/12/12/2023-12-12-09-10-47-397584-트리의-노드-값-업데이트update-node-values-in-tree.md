---
layout: post
title: "[c++] 트리의 노드 값 업데이트(Update Node Values in Tree)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

이번에는 C++를 사용하여 트리의 노드 값을 업데이트하는 방법에 대해 알아보겠습니다. 이를 위해, 트리의 구조를 이해하고, 노드 값을 업데이트하는 방법을 살펴보겠습니다.

## 트리(Tree)란 무엇인가?

트리는 계층적인 데이터 구조로, 여러 개의 노드가 간선(edge)으로 연결된 구조를 말합니다. 트리에는 부모 노드와 자식 노드가 있으며, 각 노드는 여러 개의 자식을 가질 수 있습니다. 트리는 데이터를 계층적으로 표현할 때 유용하게 사용됩니다.

## 트리 노드의 값 업데이트하기

트리의 노드의 값을 업데이트하는 방법에는 여러 가지가 있습니다. 가장 일반적인 방법 중 하나는 깊이 우선 탐색(DFS, Depth-First Search) 또는 너비 우선 탐색(BFS, Breadth-First Search)을 사용하여 트리를 순회하면서 원하는 노드를 찾고 값을 업데이트하는 것입니다.

아래는 간단한 예제 코드입니다.

```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int value;
    vector<Node*> children;
};

void updateNodeValue(Node* root, int targetValue, int newValue) {
    if (root == NULL) {
        return;
    }

    if (root->value == targetValue) {
        root->value = newValue;
    }

    for (Node* child : root->children) {
        updateNodeValue(child, targetValue, newValue);
    }
}

int main() {
    // 트리 생성 및 초기화
    Node* root = new Node{1, {}};
    Node* child1 = new Node{2, {}};
    Node* child2 = new Node{3, {}};
    root->children.push_back(child1);
    root->children.push_back(child2);

    // 노드 값 업데이트
    updateNodeValue(root, 2, 10);

    // 업데이트된 값 출력
    cout << root->children[0]->value; // 출력: 10
    return 0;
}
```

이 예제 코드는 구조체를 사용하여 간단한 트리를 구현하고, `updateNodeValue` 함수를 통해 트리의 노드 값을 업데이트하는 방법을 보여줍니다.

## 결론

이상으로 C++를 사용하여 트리의 노드 값을 업데이트하는 방법에 대해 알아보았습니다. 트리는 데이터를 효율적으로 표현하고 조작할 수 있는 중요한 자료 구조이므로, 노드 값을 업데이트하는 방법을 잘 숙지하는 것이 중요합니다.