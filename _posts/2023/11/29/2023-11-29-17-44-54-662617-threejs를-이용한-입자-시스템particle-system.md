---
layout: post
title: "[javascript] Three.js를 이용한 입자 시스템(Particle System)"
description: " "
date: 2023-11-29
tags: [javascript]
comments: true
share: true
---

Three.js는 3D 웹 그래픽을 구현하기 위한 자바스크립트 라이브러리로 널리 사용되고 있습니다. 입자 시스템은 Three.js에서 다양한 효과를 구현하는 데 사용되는 기능 중 하나입니다. 이번 기사에서는 Three.js를 사용하여 입자 시스템을 만드는 방법에 대해 알아보겠습니다.

## 입자 시스템의 개념

입자 시스템은 여러 개의 입자로 이루어져 있으며, 각 입자는 위치, 속도, 색상과 같은 속성을 가지고 있습니다. 이러한 입자들은 화면상에 움직이거나 특정한 패턴을 그릴 수 있습니다. 입자 시스템은 주로 자연 현상을 시뮬레이션하거나 시각적인 효과를 구현하기 위해 사용됩니다.

## Three.js에서 입자 시스템 만들기

Three.js에서 입자 시스템을 만들려면 다음 단계를 따라야 합니다.

1. `THREE.Geometry()`을 사용하여 입자들을 저장할 geometry 객체를 만듭니다.
2. 입자들의 초기 위치, 속도, 색상 등의 속성을 설정합니다.
3. `THREE.PointsMaterial`을 사용하여 입자들의 표면 속성을 정의합니다.
4. `THREE.Points`를 사용하여 입자들을 포함하는 객체를 만듭니다.
5. 입자 시스템을 `scene`에 추가합니다.

아래는 Three.js를 사용하여 입자 시스템을 만드는 예제 코드입니다.

```javascript
// 필요한 변수들을 초기화합니다.
let scene, camera, renderer;

init();
animate();

function init() {
    // scene, camera, renderer를 만듭니다.
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // 입자 시스템에 필요한 변수들을 초기화합니다.
    let particleCount = 1000;  // 입자 개수
    let particles = new THREE.Geometry();  // 입자들을 저장할 geometry 객체

    // 입자들의 초기 위치, 속도, 색상을 설정합니다.
    for (let i = 0; i < particleCount; i++) {
        let particle = new THREE.Vector3(
            Math.random() * 200 - 100,
            Math.random() * 200 - 100,
            Math.random() * 200 - 100
        );

        particles.vertices.push(particle);
    }

    // 입자들의 표면 속성을 정의합니다.
    let particleMaterial = new THREE.PointsMaterial({ color: 0xffffff, size: 2 });

    // 입자들을 포함하는 객체를 만듭니다.
    let particleSystem = new THREE.Points(particles, particleMaterial);

    // 입자 시스템을 scene에 추가합니다.
    scene.add(particleSystem);

    // camera의 위치와 조작 방법을 설정합니다.
    camera.position.z = 5;
    camera.lookAt(scene.position);
}

function animate() {
    requestAnimationFrame(animate);

    // 입자 시스템을 애니메이션화합니다.
    let particleSystem = scene.getObjectByName("particleSystem");
    particleSystem.rotation.x += 0.01;
    particleSystem.rotation.y += 0.01;

    renderer.render(scene, camera);
}
```

위의 코드를 실행하면 3D 공간에서 무작위로 움직이는 입자 시스템을 볼 수 있습니다.

## 결론

Three.js를 사용하여 입자 시스템을 만들어 보았습니다. 입자 시스템은 다양한 효과와 시각적인 효과를 구현하는 데 사용될 수 있으며, Three.js를 통해 상세한 제어가 가능합니다.

더 많은 입자 시스템의 옵션과 기능을 알아보려면 [Three.js 공식 문서](https://threejs.org/docs/index.html#manual/en/introduction/Creating-a-scene)를 참조하십시오.