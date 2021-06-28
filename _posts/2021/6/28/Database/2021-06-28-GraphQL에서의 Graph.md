---
layout: post
title: "[DB] GraphGL에서의 Graph"
description: " "
date: 2021-06-28
tags: [DB]
comments: true
share: true
---

```
번역:https://dev.to/bogdanned/the-graph-in-graphql-1l99?fbclid=IwAR0HCuEsDXA9h_MVdSmxKf-nIQh5OAaiIlT5sDdnFnpjUEXM8ztePlE_gPU
```

#### Graph란

그래프는 mental model을 구축하고, 개념을 연관시키는 자연스러운 방법과 유사한 데이터 구조다. 그래프에서 관계는 개체 자체와 관련이 있다.

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--HeRdqMxu--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://www.bogdanned.com/media/randomGraph.jpg">

그래프는 보통 노드, 정점이라고 부르는 추상 객체로 이루어져있다. 두 노드 사이의 선은 edge(엣지)라고 부르며 우리는 특정한 순서에 의해 엣지를 따라 그래프를 재귀적으로 탐색할 수 있다.

#### A-Cyclical Directed Graphs (순환 지시 그래프)

노드와 엣지의 배열 방식에 따라 다양한 유형의 그래프가 있다. 우리는 여기서는 순환 지시 그래프를 확인해볼 건데 이는 GraphQL 내부에서 찾을 수 있는 방식이기 때문이다.

한쪽을 향하는 엣지는 시작과 끝을 갖고 있으며 이 방향을 통해서만 탐색이 가능하다. 이렇게 엣지에 방향을 추가하는 것은 노드 사이의 관계를 표시함과 동시에 계층 관계를 표현하기도 한다.

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--qyBJ4A0w--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://www.bogdanned.com/media/simpleDirectedGraph.jpg">

예를들어 채무관계를 그래프로 표시해본다면 모든 엣지는 돈을 빌려주는 부분을 표시할 것이고 돈을 빌려주는 사람으로부터 빌리는 사람으로 가는 돈의 흐름을 나타낼 것이다.

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--x6f3iotU--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://www.bogdanned.com/media/money_borrow.jpg">

#### From a Graph to a Tree(그래프에서 트리로)

그래프는 어떤 조건이 부여됨에 따라 다른 자료 구조로 변할 수가 있다. 그래프 사이클, 순회는 마지막 엣지가 첫 엣지인 자료의 집합인데, 이때 그래프에 순회가 없다면 이를 A-Cyclical graph라고 부른다. 그리고 위에서 설명한 directional graph는 일종의 A-Cyclical graph이다. 그리고 이는 Tree라고 불리기도 한다.

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--eTTXrpWL--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://www.bogdanned.com/media/graphVersusTree.jpg">

트리구조는 재귀라는 특징으로 인해 몇가지 장점을 가지고 있다.

트리를 구성하는 기본 요소에는 하나의 루트노드와 하나 혹은 여러개의 칠드런 노드들이 있다. 우리가 그래프를 활용하여 일정한 제약 조건 하에서 데이터 모델링을 작성할 때 트리의 속성을 활용할 수 있다. 일반적으로 노드에 어떤 작업들이 부여되야 할 때 트리 전체를 가로질러서 작업을 진행하는 것이 노드별로 작업을 진행하는 것 보다 훨씬 쉬우므로, 읽기 쓰기 작업이 루트 노드에서부터 재귀적으로 실행됨으로써 하위 칠드런 노드까지 전체적으로 작업이 수행될 수 있다.

#### Modeling with Graph(QL)

GraphQL은 schema를 활용하여 비즈니스 영역을 나타낸다. 스키마는 각각의 다른 개체를 나타내는 type으로 구성되어 있는 그래프를 나타낸다. 타입들은 도메인을 기반으로 해당 도메인에서 필요한 개체를 나타내며 각 개체는 다른 필드들을 가지고 있을 수 있고 모든 필드는 다른 타입을 가리킨다.

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--RzzUIVha--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://www.bogdanned.com/media/extractingGraphQLType.jpg">

위 사진에서 처럼 lastname, firstname, emal은 scalar의 string을 가리킨다. scalar 타입은 하위 필드를 가질 수 없기 때문에 이때 필드들은 단순히 query tree의 잎(leaves)을 나타낸다.

type과 type 내부의 field의 관계는 단방향 엣지로 이루어지며 스키마를 구성하는 요소이다. 이 관계가 GraphQL 스키마를 비순환 그래프로 만들게 된다. 위에서 비순환 그래프는 트리구조와 같이 각각의 노드를 돌면서 읽기를 수행할 수 있다고 했는데 이 과정을 tre traversal이라고 한다.

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--8Mk4rRaY--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://www.bogdanned.com/media/schema%26query.jpg">

GraphQL의 query는 root type에서 부터 서브 필드들을 가지고 있지 않은 scalar 타입에 닿기 까지의 그래프 내부에서의 길을 뜻한다. 결과적으로 쿼리는 graphQL의 특정 서브셋을 트리로 투영한 것이다. 백엔드 측에서는 타입의 모든 필드는 쿼리 할 때의 해당 값을 반환하는 리졸버 함수에 매핑된다.

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--lSRgHvNI--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://www.bogdanned.com/media/resolvers.jpg">

query의 결과는 스키마에서 추출된 모든 필드에 대해 리졸버 함수실행 결과를 병합하여 만들어진다. 그러나 graphQL은 여기서 멈추지 않는다. 트리 속성과 재귀 함수는 데이터를 모델링 할뿐만 아니라 주로 해당 스키마에서 쿼리를 확인하고 실행하는 데 사용된다.

#### Schema parsing

graphQL 서버는 실행시 스키마 문서를 파싱한다(구문분석한다). 타입들은 내부 필드들과 typeMap이라고 불리는 dictionary에 존재하는 resolver 함수들을 참조하며 순수 자바스크립트 Object로 추출, 저장된다. 필드에서 쿼리를 통해 값을 가져오는 과정이 시작될 때 실행 알고리즘은 dictonary에 존재하는 필드를 찾고 리졸버 함수와 하위 타입에 대한 참조를 사용하여 값을 확립한다.

```
// Simplified structure of the type map
let typeMap = {
  rootType: {
    fields: { // array with the fields of the root ype
      user: {
        type: {
          fields: {
            lastname: {...},
            settings: {...},
          }
        },
        resolve: () => ({})  // points to a resolve function for the type
      },
      settings: {
        type: {
          fields: {
            membership: {...},
          }
        },
        resolve: () => ({})  // points to a resolve function for the type
      }
    }
  },
};
```

모든 타입은 해당 타입에 대한 resolver 함수의 참조를 포함하고 있고, 전체 스키마에 대해 아래 세가지 스텝을 반복함으로써 resolve를 수행한다.

1. typeMap 사전에서 해당 type을 찾는다.
2. 해당 타입의 resolver 함수를 수행한다.
3. 해당 타입의 필드들에 1,2 를 동일하게 수행한다.

정리하면,

graphQL 스키마는 서버에서 파싱된다. 파싱이 진행되는 동안 type들은 그에 대한 typeMap에 저장되어 있는 resolver 함수에 대한 참조와 함께 추출, 저장된다.

#### Query Parsing

graphQL query 서버는 문자열의 쿼리를 Abstract Syntax Tree(AST)로 파싱한다. AST는 특정 언어의 소스코드 구문을 트리로 표현한 것이다. 트리의 모든 노드는 유형, 인수 및 위치를 포함하여 쿼리의 명령문을 나타낸다.

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--7q8NyBuh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://www.bogdanned.com/media/AbstractSyntaxTree.jpg">

AST는 컴파일러에 대한 일반적인 추상화이며 의미 분석이라는 프로세스에서 구문 정확성을 검증하는데 사용된다.

AST는 트리구조와 비슷한 자료 구조를 가지고 있기 때문에 프로세스와 해석을 재귀함수에 의해 반복한다.

#### Query Execution

쿼리 연산자가 AST로 변환한 뒤에 해당 구조가 유효하다면 우리는 query를 실행하기 위해 tree의 속성을 사용할 수 있다. 이 실행 알고리즘의 코어는 AST의 모든 노드에 대해 DFS를 따르는 재귀함수의 실행이다.

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--0Cr0JMG9--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://www.bogdanned.com/media/QueryTraversal.jpg">

순회는 필드가 안정적이고 일관된 순서로 실행되고 해결되도록 하며 1차 순회에 이어 필드 실행 함수는 아래와 같은 순서로 각 필드에서 호출된다.

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--mwUY1IsV--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://www.bogdanned.com/media/ExecutionTraversalOrder.jpg">

필드 실행 함수는 필드 값의 분석하는 마법을 포함하고 있으며 해당 함수의 인자로는 type의 이름, typeMap 사전에 정의 되어있는 타입의 정의, resolver 함수로 구성된다.

첫번째, resolver가 실행되면 해당 리턴 값을 저장한다.

두번째, 해당 타입에 의하여 필드 값이 완성된다.

만약 이때 필드 값이 scalar이면 해당 값은 serialization 함수에 의해 강제로 반환된다.

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--UPmBEglJ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://www.bogdanned.com/media/ExecuteField.jpg">

만약 필드의 타입이 Object라면 completeValue 프로세스가 시작된다. collectFields 함수가 해당 오브젝트 내부의 resolver 함수에 의해 해결되지 않은 상태의 필드들을 fieldGroup으로 모아서 리턴한다. 이때 filedGroup는 DFS 순서를 가지고 있는 array이다.

executeField 함수는 해당 array의 원소에 대해 병렬로 실행되며 마지막으로, 알고리즘은 리졸버 함수의 첫 번째 실행 및 completeValue 리턴에 의해 리턴 된 값을 병합 및 강제 변환하고 쿼리 AST 트리의 순서에 따라 최종 결과를 빌드한다.
