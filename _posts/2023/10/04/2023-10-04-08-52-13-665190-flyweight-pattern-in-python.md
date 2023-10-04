---
layout: post
title: "Flyweight pattern in Python"
description: " "
date: 2023-10-04
tags: [flyweightpattern]
comments: true
share: true
---

The **Flyweight pattern** is a design pattern that enables the efficient sharing of objects to reduce memory usage. It is particularly useful when dealing with large numbers of similar objects, as it minimizes the memory footprint by reusing objects instead of creating new ones.

### How does it work?

In the Flyweight pattern, objects are divided into two categories: **intrinsic** and **extrinsic** state. 

- The **intrinsic state** of an object represents the properties that can be shared and are independent of the object's context. These properties can be stored as part of the object's class and can be reused across multiple instances.

- The **extrinsic state** represents the properties that are unique to each object and cannot be shared. These properties are typically passed as method parameters when invoking the object's behavior.

The Flyweight pattern aims to separate and manage the intrinsic and extrinsic states. It maintains a **flyweight factory** that stores already created objects and returns them if they exist, otherwise it creates new ones.

### Example of Flyweight Pattern

Let's take an example of a text editor where we have to render multiple characters on a screen. Instead of creating separate objects for each character, we can use the Flyweight pattern to reuse the character objects.

```python
class Character:
    def __init__(self, char):
        self.char = char
        
    def render(self, font_size):
        print(f"Rendering character '{self.char}' with font size {font_size}")

class CharacterFactory:
    def __init__(self):
        self.characters = {}

    def get_character(self, char):
        if char not in self.characters:
            self.characters[char] = Character(char)
        return self.characters[char]

class TextEditor:
    def __init__(self, font_size):
        self.font_size = font_size
        self.character_factory = CharacterFactory()
        self.characters = []

    def add_character(self, char):
        character = self.character_factory.get_character(char)
        self.characters.append(character)

    def render_text(self):
        for character in self.characters:
            character.render(self.font_size)

# Example usage
text_editor = TextEditor(font_size=12)
text_editor.add_character('A')
text_editor.add_character('B')
text_editor.add_character('A')
text_editor.add_character('C')
text_editor.add_character('B')

text_editor.render_text()
```

In the code above, the `Character` class represents the flyweight object and the `CharacterFactory` class acts as the flyweight factory. The `TextEditor` class uses the flyweight objects to render the characters on the screen.

By reusing the flyweight objects, we minimize the memory usage, as only a single instance of each character is created and shared among multiple occurrences in the text.

### Conclusion

The Flyweight pattern is a powerful technique for optimizing memory usage when dealing with large numbers of similar objects. By separating intrinsic and extrinsic state and reusing flyweight objects, we can significantly reduce the memory footprint of our applications.

#python #flyweightpattern