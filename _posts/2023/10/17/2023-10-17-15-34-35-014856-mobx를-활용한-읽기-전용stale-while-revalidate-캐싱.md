---
layout: post
title: "MobX를 활용한 읽기 전용(stale-while-revalidate) 캐싱"
description: " "
date: 2023-10-17
tags: []
comments: true
share: true
---

읽기 전용 캐싱은 애플리케이션에서 데이터를 효율적으로 관리하는 데에 매우 유용한 기술입니다. 이를 통해 데이터 요청을 줄이고 응답 시간을 단축시킬 수 있습니다. MobX는 React 애플리케이션에서 데이터 상태를 관리하는 데 사용되는 강력한 라이브러리입니다. 이 포스트에서는 MobX를 활용하여 읽기 전용 캐싱을 구현하는 방법을 알아보겠습니다.

## 읽기 전용 캐싱 작업 흐름

읽기 전용 캐싱은 데이터의 유효성을 검증하고, 캐시된 데이터가 유효한 경우 지연 시간 동안 이를 반환하여 응답 시간을 단축시킵니다. 이를 구현하기 위해 다음과 같은 작업 흐름을 따릅니다:

1. 데이터를 요청합니다.
2. 데이터를 캐시에서 확인합니다.
3. 캐시된 데이터가 유효한 경우 즉시 반환합니다.
4. 캐시된 데이터가 유효하지 않은 경우 신선한 데이터를 요청합니다.
5. 데이터 요청 결과를 캐시에 저장합니다.
6. 반환된 데이터를 사용합니다.

## MobX를 사용한 읽기 전용 캐싱 구현

MobX를 사용하여 읽기 전용 캐싱을 구현하기 위해서는 다음과 같은 단계를 진행해야 합니다.

### 단계 1: MobX 스토어 생성

먼저 MobX 스토어를 생성해야 합니다. 스토어는 데이터 상태를 관리하고, 캐시된 데이터를 저장하는 역할을 합니다. 아래는 MobX 스토어의 예시입니다:

```javascript
import { observable, action } from 'mobx';

class CachedDataStore {
  @observable data = null;

  @action
  fetchData() {
    // 데이터 요청 로직을 작성합니다.
    // ...
    // 요청 결과를 this.data에 저장합니다.
    this.data = responseData;
  }
}
```

스토어에서는 `@observable` 데코레이터를 사용하여 `data`라는 관찰 가능한 상태를 생성하고, `@action` 데코레이터를 사용하여 `fetchData` 메서드를 생성합니다.

### 단계 2: 캐시 유효성 검증

다음으로, 캐시된 데이터가 유효한지 검증하는 로직을 작성해야 합니다. 읽기 전용 캐싱에서는 일정 시간 동안 데이터를 유효하게 유지한 후, 새로운 데이터를 가져와서 업데이트합니다. 아래는 캐시 유효성을 검증하는 메서드의 예시입니다:

```javascript
class CachedDataStore {
  //...

  @observable lastUpdated = null;

  @computed
  get isDataStale() {
    return !this.lastUpdated || (Date.now() - this.lastUpdated) > CACHE_EXPIRY_TIME;
  }

  @action
  fetchData() {
    if (this.isDataStale) {
      // 데이터를 캐시에서 확인하는 로직을 작성합니다.
      // ...
      // 유효하지 않은 경우 데이터를 요청하고 캐시를 업데이트합니다.
      this.data = fetchedData;
      this.lastUpdated = Date.now();
    }
  }
}
```

위의 예시에서 `lastUpdated`라는 상태를 생성하여 마지막으로 데이터를 업데이트한 시간을 저장합니다. `isDataStale`이라는 계산된 속성을 생성하여 캐시된 데이터가 유효한지 확인합니다. `fetchData` 메서드에서는 `isDataStale`이 `true`인 경우에만 데이터를 요청하고, 캐시를 업데이트합니다.

### 단계 3: 캐시된 데이터 사용

마지막으로, 캐시된 데이터를 사용하는 컴포넌트에서 MobX 스토어를 활용합니다. 아래는 예시입니다:

```javascript
import { observer } from 'mobx-react';

const CachedDataComponent = observer(() => {
  const cachedDataStore = useCachedDataStore();

  useEffect(() => {
    cachedDataStore.fetchData();
  }, [cachedDataStore]);

  if (cachedDataStore.isDataStale) {
    return <LoadingSpinner />;
  }

  return <DataDisplay data={cachedDataStore.data} />;
});
```

위의 예시에서 `observer` 함수를 사용하여 컴포넌트를 MobX의 관찰자로 등록합니다. 이를 통해 스토어의 변화를 감지하고, 자동으로 리렌더링될 수 있습니다. `useCachedDataStore` 훅을 사용하여 스토어 인스턴스를 얻고, `fetchData` 메서드를 호출하여 데이터를 요청합니다. 그 후, `isDataStale`이 `true`인 경우 로딩 스피너를 표시하고, 그렇지 않은 경우 데이터를 화면에 표시합니다.

## 결론

MobX를 활용하여 읽기 전용 캐싱을 구현하는 방법을 살펴보았습니다. MobX는 데이터 상태 관리를 용이하게 해주는 라이브러리로, 응답 시간을 단축하고 애플리케이션의 성능을 향상시킬 수 있습니다. 읽기 전용 캐싱을 적용하여 데이터 요청을 줄이고, 사용자 경험을 향상시킬 수 있습니다.

## References

- [MobX 공식 문서](https://mobx.js.org/)
- [MobX와 함께하는 React 상태 관리](https://mobx-react.js.org/)