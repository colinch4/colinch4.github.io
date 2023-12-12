---
layout: post
title: "[c++] 트라이(Trie) 구조의 삽입과 검색(Trie Insertion and Search)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

트라이(Trie)는 문자열 검색과 관련된 데이터 구조로, 문자열의 삽입과 검색에 효과적으로 사용됩니다. 이번 포스트에서는 C++로 트라이를 구현하고, 문자열의 삽입과 검색을 어떻게 수행하는지에 대해 알아보겠습니다.

## 트라이 구조

트라이는 각 노드가 알파벳 문자 하나를 나타내는 트리 구조입니다. 루트 노드는 빈 문자열을 나타내며, 다음 레벨의 각 노드는 문자열의 첫 번째 문자부터 순서대로 나타냅니다. 각 노드는 자식 노드들과 연결되어 있고, 문자열의 끝을 나타내는 특별한 마크를 갖고 있습니다.

## 삽입(Insertion)

아래는 C++로 트라이에 문자열을 삽입하는 코드입니다.

```cpp
class TrieNode {
public:
    bool isEnd;
    TrieNode* children[26];

    TrieNode() {
        isEnd = false;
        for (int i = 0; i < 26; i++) {
            children[i] = nullptr;
        }
    }
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children[c - 'a']) {
                node->children[c - 'a'] = new TrieNode();
            }
            node = node->children[c - 'a'];
        }
        node->isEnd = true;
    }
};
```

위 코드에서는 삽입 연산을 수행하는 `insert` 메소드가 구현되어 있습니다. 문자열을 한 글자씩 탐색하여 각 문자에 해당하는 자식 노드를 만들고, 마지막 글자의 노드에는 `isEnd`를 true로 설정하여 문자열의 끝을 나타냅니다.

## 검색(Search)

이제 C++로 트라이에서 문자열을 검색하는 방법을 알아보겠습니다.

```cpp
class Trie {
    // (이전과 동일)

    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children[c - 'a']) {
                return false;
            }
            node = node->children[c - 'a'];
        }
        return node && node->isEnd;
    }
};
```

위 코드에서는 검색 연산을 수행하는 `search` 메소드가 구현되어 있습니다. 문자열을 한 글자씩 탐색하면서 각 문자에 해당하는 자식 노드들을 찾고, 마지막 노드에서는 `isEnd`가 true인지를 확인하여 문자열의 존재 여부를 판단합니다.

이렇게 C++로 트라이 구조의 삽입과 검색을 구현할 수 있습니다.

## 결론

이번 포스트에서는 C++로 트라이 구조를 사용하여 문자열의 삽입과 검색을 구현하는 방법에 대해 알아보았습니다. 트라이는 문자열 검색에 효과적이며, 삽입과 검색 연산을 효율적으로 수행할 수 있습니다.

참고 문헌:
- https://en.wikipedia.org/wiki/Trie