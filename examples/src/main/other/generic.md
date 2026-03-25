---
title: Generic Markdown
date: 2026-03-19
tags: [example, tokens]
draft: false
---

# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

Body <br> text with **bold**, *italic*, ***bold italic***, and ~~strikethrough~~.

Inline `code span` and a [link text](https://example.com "title").

Other url <fake@example.com>

<fake@example.com>

> Blockquote with **bold** inside.

Example [hobbit-hole][123]

- Bullet item
  - Nested bullet
    - Deep nested

1. Ordered item
   1. Nested ordered
2. Second item
   - Mixed nested

- [x] Done task
- [ ] Pending task

| Name | Type | Default |
|---|:---:|---:|
| `host` | string <br> other | `localhost` |
| port | number | "5432.123" |

```kotlin
val x = 1
```

```text
some text
some other text
```

---

Image ref: ![alt text](image.png)

[123]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle
