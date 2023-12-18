---
layout: post
title: "[javascript] Nuxt.js에서의 SSR(Server Side Rendering) vs CSR(Client Side Rendering) 비교"
description: " "
date: 2023-12-19
tags: [javascript]
comments: true
share: true
---

Nuxt.js는 Vue.js 기반의 웹 애플리케이션을 구축할 때 사용되는 프레임워크이며, SSR과 CSR 둘 다 지원됩니다. 이 두 가지 렌더링 방식에는 각각 장단점이 있으며, 프로젝트의 요구 사항과 목표에 따라 적합한 방식을 선택해야 합니다.

## SSR(Server Side Rendering)

SSR은 서버에서 웹 페이지의 HTML을 생성하여 클라이언트에게 제공하는 방식입니다. Nuxt.js에서 SSR을 활용하면, 초기 로딩 시 클라이언트에서 필요한 데이터가 모두 렌더링되고, 검색 엔진이 페이지를 색인화할 때 유용합니다. 또한, 초기 로딩 속도가 빠르고 SEO에 유리합니다.

```javascript
export default {
  async asyncData({ params }) {
    const { data } = await fetch(`https://api.example.com/post/${params.id}`)
    return { post: data }
  }
}
```

## CSR(Client Side Rendering)

CSR은 서버에서 기본적인 HTML과 자바스크립트 파일을 제공하고, 클라이언트에서 자바스크립트를 이용하여 동적으로 페이지를 렌더링하는 방식입니다. Nuxt.js에서 CSR을 사용할 경우, 초기 로딩 시에는 빠르지만 SEO에는 불리할 수 있습니다. 또한, 초기 로딩 이후 클라이언트에서 추가적인 데이터를 가져와야 하는 경우가 있을 수 있습니다.

```javascript
export default {
  async fetch() {
    this.posts = await this.$axios.$get('https://api.example.com/posts')
  }
}
```

## Conclusion

SSR은 SEO 및 초기 로딩 성능 측면에서 우수하지만, 서버 부하와 렌더링 시간이 더 많이 소요될 수 있습니다. 반면 CSR은 초기 로딩이 빠르고 서버 부하가 적지만, SEO에 불리할 수 있습니다. 프로젝트의 특성과 목표에 따라 SSR 또는 CSR 중 적합한 방식을 선택해야 합니다.

이러한 SSR과 CSR의 특징을 고려하여 프로젝트에 적합한 렌더링 방식을 선택하고, 웹 애플리케이션의 성능 및 사용자 경험을 향상시킬 수 있습니다.

## References
- [Nuxt.js 공식 문서](https://nuxtjs.org/guide#server-rendering)