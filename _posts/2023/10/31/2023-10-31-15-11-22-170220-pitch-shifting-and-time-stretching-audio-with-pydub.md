---
layout: post
title: "Pitch shifting and time stretching audio with Pydub"
description: " "
date: 2023-10-31
tags: [tags, audio]
comments: true
share: true
---

In this tutorial, we will explore how to perform pitch shifting and time stretching on audio files using the Pydub library in Python. Pydub is a simple and easy-to-use audio processing library that provides various functionalities for manipulating audio files.

## Table of Contents

- [Introduction](#introduction)
- [Installing Pydub](#installing-pydub)
- [Pitch Shifting](#pitch-shifting)
- [Time Stretching](#time-stretching)
- [Conclusion](#conclusion)

## Introduction

Pitch shifting is a technique used to change the pitch of an audio file, making it sound higher or lower. Time stretching, on the other hand, alters the duration of an audio file while maintaining the same pitch. These techniques are commonly used in music production, sound design, and audio effects processing.

## Installing Pydub

Before we proceed, make sure you have Pydub installed in your Python environment. You can install it using pip:

```shell
pip install pydub
```

## Pitch Shifting

To perform pitch shifting with Pydub, we can use the `pydub.effects.pitch_shift` function. This function takes the audio file as input and allows us to specify the number of semitones to shift the pitch. Positive values shift the pitch higher, while negative values shift it lower.

Here's an example that demonstrates how to shift the pitch of an audio file by 2 semitones higher:

```python
from pydub import AudioSegment
from pydub.effects import pitch_shift

# Load the audio file
audio = AudioSegment.from_file("input.wav", format="wav")

# Shift the pitch by 2 semitones higher
shifted_audio = pitch_shift(audio, n=2)

# Export the pitch-shifted audio
shifted_audio.export("output.wav", format="wav")
```

## Time Stretching

To perform time stretching with Pydub, we can use the `pydub.effects.time_stretch` function. This function takes the audio file as input and allows us to specify the speed or duration of the output audio file. A speed greater than 1 will stretch the audio, while a speed less than 1 will compress it.

Here's an example that demonstrates how to time stretch an audio file by a factor of 1.5:

```python
from pydub import AudioSegment
from pydub.effects import time_stretch

# Load the audio file
audio = AudioSegment.from_file("input.wav", format="wav")

# Stretch the audio by a factor of 1.5
stretched_audio = time_stretch(audio, factor=1.5)

# Export the time-stretched audio
stretched_audio.export("output.wav", format="wav")
```

## Conclusion

In this tutorial, we have learned how to perform pitch shifting and time stretching on audio files using the Pydub library in Python. These techniques can be useful for various applications, such as music production, sound design, and audio effects processing. By leveraging the power of Pydub, you can easily manipulate and transform audio files to achieve the desired effects.

#tags: #audio-processing #python