---
layout: post
title: "Implementing audio equalization and dynamic range compression with Pydub"
description: " "
date: 2023-10-31
tags: []
comments: true
share: true
---

Audio post-processing techniques like equalization and dynamic range compression can greatly enhance the quality and clarity of audio recordings. In this blog post, we will explore how to implement these techniques using the Pydub library in Python.

## Table of Contents
- [Introduction to Pydub](#introduction-to-pydub)
- [Audio Equalization](#audio-equalization)
- [Dynamic Range Compression](#dynamic-range-compression)
- [Conclusion](#conclusion)

## Introduction to Pydub

Pydub is a simple and easy-to-use library for audio processing in Python. It provides a high-level interface for manipulating audio files and applying various audio effects. To get started, we first need to install the Pydub library by running the following command:

```python
pip install pydub
```

Once installed, we can import the necessary modules and begin working with audio files.

```python
from pydub import AudioSegment
from pydub.playback import play
```

## Audio Equalization

Audio equalization is the process of adjusting the balance between different frequency components of an audio signal. This technique can be used to enhance specific frequencies or flatten the audio response across the entire frequency spectrum.

Pydub provides a convenient `equalize()` method that allows us to equalize an audio file. The method takes a list of frequency bands and the corresponding gain values, and applies the equalization effect to the audio.

```python
def equalize_audio(filepath, bands):
    audio = AudioSegment.from_file(filepath)
    audio = audio.equalize(bands)
    return audio


# Example usage
filepath = "audio.wav"
bands = [(0, 80, -5), (80, 5000, 3), (5000, None, 0)]
equalized_audio = equalize_audio(filepath, bands)
equalized_audio.export("equalized_audio.wav", format="wav")
```

In the above example, we define a list of frequency bands where we want to alter the gain of the audio. The first band reduces the gain by 5 dB up to 80 Hz, the second band increases the gain by 3 dB from 80 Hz to 5 kHz, and the last band maintains the gain at 0 dB above 5 kHz. The `equalize_audio()` function loads the audio file, applies the equalization effect based on the specified bands, and returns the modified audio.

## Dynamic Range Compression

Dynamic range compression is a technique used to reduce the difference between the loudest and softest parts of an audio signal. It is commonly applied to normalize the volume levels and make the audio more consistent.

Pydub provides the `compress()` method to apply dynamic range compression to an audio file. The method takes parameters like threshold, ratio, attack time, and release time to control the extent and timing of the compression effect.

```python
def compress_audio(filepath, threshold, ratio, attack, release):
    audio = AudioSegment.from_file(filepath)
    audio = audio.compress_dynamic_range(threshold, ratio, attack, release)
    return audio


# Example usage
filepath = "audio.wav"
threshold = -20  # in decibels
ratio = 4
attack_time = 10  # in milliseconds
release_time = 100  # in milliseconds
compressed_audio = compress_audio(filepath, threshold, ratio, attack_time, release_time)
compressed_audio.export("compressed_audio.wav", format="wav")
```

In the above example, we specify the compression parameters to control the compression effect. The `compress_audio()` function loads the audio file, applies the dynamic range compression effect based on the specified parameters, and returns the modified audio.

## Conclusion

By using the Pydub library, we can easily apply audio equalization and dynamic range compression to enhance our audio recordings. These techniques can significantly improve the audio quality and make it more enjoyable for listeners. Experiment with different settings and frequencies to achieve the desired audio effect.

Remember to install the Pydub library by running `pip install pydub` before implementing these audio post-processing techniques.

# References
- [Pydub documentation](https://github.com/jiaaro/pydub)
- [Audio equalization](https://en.wikipedia.org/wiki/Equalization_(audio))