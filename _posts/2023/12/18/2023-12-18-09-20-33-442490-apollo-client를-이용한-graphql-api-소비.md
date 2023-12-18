---
layout: post
title: "[nodejs] Apollo Client를 이용한 GraphQL API 소비"
description: " "
date: 2023-12-18
tags: [nodejs]
comments: true
share: true
---

GraphQL은 클라이언트가 필요한 데이터를 서버로부터 효율적으로 가져오는 데 도움을 주는 강력한 쿼리 언어입니다. Apollo Client는 GraphQL을 이용하여 데이터를 가져오고 상태를 관리하는 데 사용되는 JavaScript 라이브러리입니다.

이번 글에서는 Apollo Client를 사용하여 GraphQL API를 호출하는 방법에 대해 알아보겠습니다. 

## Apollo Client란 무엇인가?

[Apollo Client](https://www.apollographql.com/docs/react/)는 GraphQL을 위한 풍부한 기능을 제공하는 JavaScript 클라이언트 라이브러리입니다. 매우 유연하고 확장 가능하며, React, Vue, Angular 및 기타 JavaScript 프레임워크와 통합할 수 있습니다.

## Apollo Client 설치

Apollo Client를 사용하려면 먼저 프로젝트에 Apollo Client 라이브러리를 설치해야 합니다. 

```bash
npm install @apollo/client graphql
```

## Apollo Client를 사용하여 GraphQL API 소비

Apollo Client를 초기화하고 GraphQL API를 호출하려면 먼저 `ApolloProvider`를 설정해야 합니다. 

```javascript
import { ApolloClient, InMemoryCache, ApolloProvider } from '@apollo/client';
import { createHttpLink } from '@apollo/client/link/http';
import { setContext } from '@apollo/client/link/context';

const httpLink = createHttpLink({
  uri: 'https://example.com/graphql',
});

const authLink = setContext((_, { headers }) => {
  const token = localStorage.getItem('token');
  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : "",
    }
  }
});

const client = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache()
});

ReactDOM.render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>,
  document.getElementById('root')
);
```

위의 예제에서 `createHttpLink`를 사용하여 GraphQL 엔드포인트를 설정하고, `setContext`를 사용하여 각 요청에 인증 헤더를 추가합니다. 그런 다음 `ApolloClient`를 생성하고 `ApolloProvider`로 클라이언트를 설정하여 앱의 최상위 수준에 제공합니다.

이제 Apollo Client를 사용하여 쿼리를 보내고 상태를 관리할 수 있습니다. 아래는 간단한 GraphQL 쿼리를 수행하는 예제입니다.

```javascript
import { useQuery, gql } from '@apollo/client';

const GET_BOOKS = gql`
  query {
    books {
      title
      author
    }
  }
`;

function Books() {
  const { loading, error, data } = useQuery(GET_BOOKS);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return data.books.map(({ title, author }) => (
    <div key={title}>
      <p>{title} by {author}</p>
    </div>
  ));
}
```

위의 예제에서 `useQuery`를 사용하여 GraphQL 쿼리를 보내고, 결과 데이터를 효율적으로 처리합니다.

## 결론

이상으로 Apollo Client를 사용하여 GraphQL API를 호출하는 방법에 대해 알아보았습니다. Apollo Client는 GraphQL을 사용하여 데이터를 효율적으로 관리하고 가져오는 데 매우 유용한 도구입니다. GraphQL을 사용하는 프로젝트에는 Apollo Client를 적극적으로 고려해 보시기를 권장합니다.