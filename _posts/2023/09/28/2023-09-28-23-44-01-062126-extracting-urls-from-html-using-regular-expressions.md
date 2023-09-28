---
layout: post
title: "Extracting URLs from HTML using regular expressions"
description: " "
date: 2023-09-28
tags: [webdevelopment, regex]
comments: true
share: true
---

In this blog post, we will explore how to extract URLs from HTML using regular expressions in various programming languages. Extracting URLs can be useful for tasks such as web scraping, link analysis, or extracting metadata from web pages.

## Regular Expressions for URL Extraction

To extract URLs from HTML, we can use regular expressions to match patterns that represent URLs. Here is an example regular expression pattern that can be used to match basic URLs:

```regex
\b((?:https?|ftp|file):\/\/[\w\-]+(?:\.[\w\-]+)+(?:[\w.,@?^=%&amp;:/~+#-]*[\w@?^=%&amp;/~+#-])?)
```

This regular expression pattern can be used to match URLs starting with `http://`, `https://`, `ftp://`, or `file://`. It also handles URLs with subdomains, domains, and optional path segments.

## Extracting URLs in Different Programming Languages

Let's look at how we can extract URLs using regular expressions in a few popular programming languages:

### Python

```python
import re

html = """
<html>
<body>
  <a href="https://www.example.com">Example Website</a>
  <a href="https://www.google.com">Google</a>
  <a href="https://www.github.com">GitHub</a>
</body>
</html>
"""

urls = re.findall(r'\b((?:https?|ftp|file):\/\/[\w\-]+(?:\.[\w\-]+)+(?:[\w.,@?^=%&amp;:/~+#-]*[\w@?^=%&amp;/~+#-])?)', html)

for url in urls:
    print(url)
```

### JavaScript

```javascript
const html = `
<html>
<body>
  <a href="https://www.example.com">Example Website</a>
  <a href="https://www.google.com">Google</a>
  <a href="https://www.github.com">GitHub</a>
</body>
</html>
`;

const urls = html.match(/\b((?:https?|ftp|file):\/\/[\w\-]+(?:\.[\w\-]+)+(?:[\w.,@?^=%&amp;:/~+#-]*[\w@?^=%&amp;/~+#-])?)/g);

console.log(urls);
```

### Java

```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class URLExtractor {
    public static void main(String[] args) {
        String html = """
                      <html>
                      <body>
                        <a href="https://www.example.com">Example Website</a>
                        <a href="https://www.google.com">Google</a>
                        <a href="https://www.github.com">GitHub</a>
                      </body>
                      </html>
                      """;

        String regex = "\\b((?:https?|ftp|file):\\/\\/\\w[\\w\\-]+(?:\\.[\\w\\-]+)+(?:[\\w.,@?^=%&amp;:\\/~+#-]*[\\w@?^=%&amp;/~+#-])?)";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(html);

        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}
```

## Conclusion

Regular expressions can be a powerful tool for extracting URLs from HTML. However, keep in mind that HTML parsing can be more complex than just using regular expressions, and it is generally recommended to use dedicated HTML parsing libraries when working with HTML documents.

Using regular expressions for URL extraction can be a good option for simple use cases, but it may not handle all edge cases. It's always important to test and validate the results when using regular expressions for extracting URLs from HTML.

#webdevelopment #regex