---
layout: post
title: "자바스크립트 엔진의 AST(Abstract Syntax Tree) 분석 및 조작 방법"
description: " "
date: 2023-11-09
tags: []
comments: true
share: true
---

자바스크립트는 동적인 언어이기 때문에 코드를 실행하기 전에 인터프리터가 소스 코드를 분석하고 실행할 수 있는 형태로 변환해야 합니다. 이때, 자바스크립트 엔진은 소스 코드의 추상 구문 트리(Abstract Syntax Tree, AST)를 생성합니다. AST는 소스 코드의 구문과 의미를 표현하는 계층적인 구조입니다. 이러한 AST를 분석하고 조작하는 것은 자바스크립트 엔진을 이해하고 코드를 최적화하는 데 도움이 됩니다.

## AST 분석

AST를 분석하는 방법은 여러 가지가 있지만, 가장 일반적인 방법은 AST 순회(Traversal)입니다. AST 순회를 통해 각 노드를 방문하고, 노드의 종류에 따라 필요한 작업을 수행할 수 있습니다. AST 노드는 다양한 종류가 있으며, 예를 들어 변수 선언, 함수 선언, 조건문 등의 노드가 있습니다.

```javascript
// 예시 JavaScript 코드
function add(a, b) {
  return a + b;
}

const result = add(3, 4);
```

위 코드의 AST는 다음과 같이 표현될 수 있습니다:

```javascript
{
  "type": "Program",
  "body": [
    {
      "type": "FunctionDeclaration",
      "id": {
        "type": "Identifier",
        "name": "add"
      },
      "params": [
        {
          "type": "Identifier",
          "name": "a"
        },
        {
          "type": "Identifier",
          "name": "b"
        }
      ],
      "body": {
        "type": "BlockStatement",
        "body": [
          {
            "type": "ReturnStatement",
            "argument": {
              "type": "BinaryExpression",
              "operator": "+",
              "left": {
                "type": "Identifier",
                "name": "a"
              },
              "right": {
                "type": "Identifier",
                "name": "b"
              }
            }
          }
        ]
      }
    },
    {
      "type": "VariableDeclaration",
      "declarations": [
        {
          "type": "VariableDeclarator",
          "id": {
            "type": "Identifier",
            "name": "result"
          },
          "init": {
            "type": "CallExpression",
            "callee": {
              "type": "Identifier",
              "name": "add"
            },
            "arguments": [
              {
                "type": "Literal",
                "value": 3
              },
              {
                "type": "Literal",
                "value": 4
              }
            ]
          }
        }
      ],
      "kind": "const"
    }
  ],
  "sourceType": "module"
}
```

## AST 조작

AST를 조작하는 방법은 AST 노드의 속성을 변경하거나 새로운 노드를 추가하는 것입니다. 이를 통해 코드를 변환하거나 최적화할 수 있습니다. AST를 직접 조작할 수도 있지만, 보다 편리하게 조작할 수 있는 도구들이 있습니다. 예를 들어, [Babel](https://babeljs.io/)은 자바스크립트 코드를 변환하는 데에 널리 사용되는 도구입니다. Babel은 AST를 분석하고 조작함으로써 ES6+ 코드를 ES5 코드로 변환하는 작업을 수행합니다.

AST를 조작하는 예시로는 변수 이름 변경, 코드 제거, 새로운 코드 삽입 등이 있습니다. 이러한 작업은 AST 노드의 타입과 속성을 이해하고, 원하는 결과를 얻기 위해 필요한 조작을 수행하는 것에 달려있습니다.

## 결론

AST 분석 및 조작은 자바스크립트 엔진의 동작을 이해하고 코드를 최적화하는 데 도움이 됩니다. AST를 분석하고 조작하는 방법에 대해 학습하면, 코드의 동작을 파악하고 개선하는 데 유용하게 활용할 수 있습니다.