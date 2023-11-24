---
layout: post
title: "[javascript] Next.js에서의 CDN(Content Delivery Network) 사용 방법은 어떤 것이 있나요?"
description: " "
date: 2023-11-24
tags: [javascript]
comments: true
share: true
---

Next.js는 정적 및 동적 컨텐츠를 효율적인 방법으로 제공하기 위해 CDN(Content Delivery Network)을 사용할 수 있습니다. CDN은 전 세계에 분산된 서버 네트워크를 통해 컨텐츠를 최적의 위치에서 제공하는 서비스입니다.

Next.js에서 CDN을 사용하는 방법에는 여러 가지가 있습니다. 그 중에서도 주요 방법은 다음과 같습니다.

1. Public 폴더 사용: Next.js에서는 프로젝트의 'public' 폴더를 자동으로 CDN으로 제공합니다. 이 폴더에 이미지, CSS 파일, JavaScript 파일 등을 추가하면 Next.js는 이를 CDN으로 제공합니다. 예를 들어, 'public/images' 폴더에 이미지 파일을 추가하는 경우, 이미지를 `<img>` 태그에서 사용할 때 자동으로 CDN 링크로 변환됩니다.

2. External 링크: Next.js에서는 `<head>` 태그에 직접 외부 CDN 링크를 추가할 수도 있습니다. 예를 들어, CSS 파일을 CDN 링크로 가져오는 경우 다음과 같이 작성할 수 있습니다.

   ```javascript
   import Head from "next/head";

   function MyPage() {
     return (
       <>
         <Head>
           <link
             rel="stylesheet"
             href="https://cdn.example.com/styles.css"
           />
         </Head>
         {/* 페이지 컨텐츠 */}
       </>
     );
   }
   ```

위의 방법을 사용하여 Next.js에서 CDN을 효과적으로 활용할 수 있습니다. CDN을 사용하면 전 세계에 분산된 서버에서 컨텐츠를 제공하여 로딩 속도를 향상시킬 수 있으며, 프로젝트 확장성을 향상시킬 수 있습니다.

다만, CDN을 사용할 때 필요한 파일을 정적으로 제공하는지 확인하고, CDN 제공업체의 가격 정책과 서비스 조건을 검토해야 합니다.