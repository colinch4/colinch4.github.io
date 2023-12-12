---
layout: post
title: "[c++] 레드-블랙 트리의 삽입(Red-Black Tree Insertion)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

레드-블랙 트리는 이진 검색 트리(binary search tree)이며, 삽입(insertion) 연산을 수행할 때 균형을 유지하는 효율적인 자료구조입니다. 레드-블랙 트리의 삽입 알고리즘은 새 요소를 적절한 위치에 추가한 후, 트리의 속성을 만족하도록 조정하는 과정으로 구성됩니다.

## 삽입 알고리즘

레드-블랙 트리에 새로운 노드를 삽입하는 과정은 다음과 같습니다.

1. 이진 검색 트리의 삽입 연산을 수행하여 새 노드를 추가합니다.
2. 추가된 새 노드의 색상을 레드로 설정합니다.
3. 추가된 노드가 루트 노드이거나 부모 노드의 색상이 블랙인 경우에는 추가 조치가 필요하지 않습니다. 이 경우 트리의 레드-블랙 속성을 위배하지 않습니다.
4. 추가된 노드의 부모 노드가 루트 노드가 아니고 부모 노드의 색상이 레드인 경우, 재귀적으로 조정을 수행합니다.

## 재귀적 조정

레드-블랙 트리의 삽입 과정에서 재귀적으로 구조를 조정하는 과정은 다음과 같습니다.

1. 추가된 노드의 삼촌 노드가 레드인 경우: 부모 노드와 삼촌 노드의 색상을 변경하여, 삼촌 노드와 부모 노드를 블랙으로 만들고 부모의 부모 노드를 레드로 만듭니다.
2. 추가된 노드의 삼촌 노드가 블랙이거나 NULL인 경우: 회전 및 색상 변경을 통해 트리의 구조를 조정합니다.

## 예시

```c++
// 삽입 알고리즘 예시
void RBTree::insertFixup(Node* node) {
    while (node != root && node->parent->color == RED) {
        if (node->parent == node->parent->parent->left) {
            Node* uncle = node->parent->parent->right;

            // Case 1
            if (uncle->color == RED) {
                node->parent->color = BLACK;
                uncle->color = BLACK;
                node->parent->parent->color = RED;
                node = node->parent->parent;
            } else {
                // Case 2
                if (node == node->parent->right) {
                    node = node->parent;
                    leftRotate(node);
                }

                // Case 3
                node->parent->color = BLACK;
                node->parent->parent->color = RED;
                rightRotate(node->parent->parent);
            }
        }
        else {
            // symmetric cases
        }
    }
    root->color = BLACK;
}
```

위 예시는 삽입 연산을 수행한 후 레드-블랙 트리의 속성을 유지하기 위해 조정하는 알고리즘의 예시입니다.

## 마치며

레드-블랙 트리는 삽입 연산 후에도 균형을 유지하기 위해 조정이 필요한 자료구조입니다. 삽입 알고리즘은 트리의 구조를 조정하고, 색상을 변경하여 트리가 레드-블랙 속성을 만족하도록 보장합니다.