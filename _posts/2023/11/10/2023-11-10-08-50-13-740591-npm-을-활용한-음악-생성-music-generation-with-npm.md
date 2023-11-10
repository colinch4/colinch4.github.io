---
layout: post
title: "npm 을 활용한 음악 생성 (Music generation with npm)"
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

음악은 우리 생활에 많은 영향을 끼칠 수 있는 힘을 지니고 있습니다. 그런데, 여러분은 npm을 활용하여 음악을 생성할 수 있다는 사실을 알고 계셨나요? npm은 Node.js 패키지 매니저로, 다양한 모듈을 설치하고 사용할 수 있게 해줍니다. 이번 글에서는 npm을 활용하여 음악 생성을 위한 모듈들을 알아보고, 간단한 예제 코드를 작성해보겠습니다.

## 음악 생성을 위한 npm 모듈

### `tone.js`

`tone.js`는 웹 오디오를 다루기 위한 JavaScript 라이브러리로, 여러분이 웹 브라우저에서 음악을 만들고 조작할 수 있게 도와줍니다. 이 라이브러리는 MIDI 기반의 음악 생성을 지원하며, 다양한 악기와 이펙트를 사용할 수 있습니다.

### `midi-writer-js`

`midi-writer-js`는 MIDI 파일을 생성하는 JavaScript 라이브러리로, MIDI 표준 포맷에 따라 악보와 여러 이벤트를 작성할 수 있습니다. 이 라이브러리를 활용하면 JavaScript 코드로 MIDI 파일을 생성하고 다양한 음악 정보를 컨트롤할 수 있습니다.

## 예제 코드

아래는 `tone.js`와 `midi-writer-js`를 사용하여 간단한 미디 파일을 생성하는 예제 코드입니다.

```javascript
const Tone = require('tone');
const MidiWriter = require('midi-writer-js');

// Tone.js를 사용하여 음악 생성
const synth = new Tone.Synth().toMaster();
synth.triggerAttackRelease("C4", "8n", 0);
synth.triggerAttackRelease("E4", "8n", "8n");
synth.triggerAttackRelease("G4", "8n", "4n");

// midi-writer-js를 사용하여 MIDI 파일 생성
const track = new MidiWriter.Track();
track.addEvent(new MidiWriter.NoteEvent({pitch: ['C4', 'E4', 'G4'], duration: '4n', velocity: 127}));

const write = new MidiWriter.Writer([track]);
const fileContent = write.buildFile();

console.log(fileContent);
```

위의 예제 코드에서는 `tone.js`로 간단한 음악을 생성하고, `midi-writer-js`로 MIDI 파일을 생성하는 과정을 보여줍니다. 이 코드를 실행하면 콘솔에 MIDI 파일의 내용이 출력됩니다.

## 결론

npm을 활용하여 음악 생성을 위한 모듈들을 사용할 수 있다는 것을 알게 되었습니다. `tone.js`와 `midi-writer-js`는 각각 웹에서 음악을 생성하고 MIDI 파일을 생성하는 데 도움을 주는 라이브러리입니다. 이러한 모듈들을 활용하여 음악을 만들고 컨트롤하는 재미있는 프로젝트를 시작해보세요!

- Reference: [Tone.js Documentation](https://tonejs.github.io/docs/)