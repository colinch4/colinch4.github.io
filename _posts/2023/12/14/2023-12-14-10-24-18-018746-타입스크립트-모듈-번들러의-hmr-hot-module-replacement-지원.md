---
layout: post
title: "[typescript] 타입스크립트 모듈 번들러의 HMR (Hot Module Replacement) 지원"
description: " "
date: 2023-12-14
tags: [typescript]
comments: true
share: true
---

코드를 수정하고 즉시 변경 사항을 확인할 수 있는 HMR (Hot Module Replacement) 기능은 개발자에게 매우 편리합니다. **HMR**은 모듈의 변경된 부분만을 실시간으로 교체하여 애플리케이션을 다시 로드할 필요 없이 변경 사항을 즉시 반영할 수 있게 해줍니다.

최근에는 **타입스크립트**를 사용하여 프론트엔드 애플리케이션을 개발할 때 **HMR**을 지원하는 모듈 번들러가 많이 등장하고 있습니다. 이러한 번들러를 사용하면 타입스크립트로 작성된 코드를 빌드할 때 HMR을 쉽게 활용할 수 있습니다.

## Webpack

가장 널리 사용되는 모듈 번들러인 **Webpack**은 타입스크립트와 함께 사용할 수 있는 다양한 **HMR** 플러그인을 제공합니다. 이를 통해 코드 변경을 감지하고 해당 모듈을 실시간으로 교체하여 브라우저에서 바로 확인할 수 있습니다. 

**Webpack**을 통해 타입스크립트 애플리케이션을 빌드할 때 **webpack-dev-server**와 함께 HMR을 활성화하면 개발자는 코드 수정을 할 때마다 페이지를 새로고침하지 않고도 변경 사항을 즉시 확인할 수 있습니다.

```typescript
// webpack.config.js

const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.ts',
  devServer: {
    hot: true,
  },
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: 'ts-loader',
        include: [path.resolve(__dirname, 'src')],
      },
    ],
  },
  resolve: {
    extensions: ['.ts', '.js'],
  },
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
    }),
  ],
};
```

## Vite

**Vite**는 최신 프론트엔드 프레임워크 및 라이브러리에 특화될 뿐만 아니라 **HMR**을 지원하면서 빠른 빌드 시간과 개발용 서버 실행 시간을 제공합니다.

```typescript
// vite.config.ts

import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [],
  server: {
    hmr: {
      overlay: false,
    },
  },
});
```

**Vite**를 사용하면 번거로운 설정 없이 타입스크립트 애플리케이션에서 HMR을 손쉽게 활용할 수 있습니다.

위에서 언급한 **Webpack**과 **Vite** 외에도 **Snowpack**, **Parcel** 등의 모듈 번들러들도 타입스크립트와 HMR을 함께 사용할 수 있는 다양한 옵션을 제공하고 있습니다.

개발자는 프로젝트의 요구 사항과 선호도에 따라 적절한 모듈 번들러를 선택하여 타입스크립트 애플리케이션에 효율적으로 **HMR**을 적용할 수 있습니다.

이처럼 타입스크립트 모듈 번들러의 **HMR** 기능을 활용하면 코드 수정 시 바로 결과를 확인할 수 있어 개발 생산성을 향상시킬 수 있습니다.

## 참고 자료

1. Webpack HMR 공식 문서: https://webpack.js.org/concepts/hot-module-replacement/
2. Vite 공식 홈페이지: https://vitejs.dev/
3. Snowpack 공식 홈페이지: https://www.snowpack.dev/
4. Parcel 공식 홈페이지: https://parceljs.org/