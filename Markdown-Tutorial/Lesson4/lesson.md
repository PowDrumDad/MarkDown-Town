# Lesson 4: Code Blocks and Horizontal Rules

In this lesson, we'll explore how to display code snippets beautifully and how to visually separate sections of your document.

## Displaying Code

Markdown provides a clean way to display code, which is essential for technical documentation, tutorials, and sharing scripts.

### Inline Code

For short, single-line code snippets, you can use inline code. Simply wrap your code in backticks (`` ` ``).

For example:
To print "Hello, World!" in Python, you can use the `print("Hello, World!")` function.

### Fenced Code Blocks

For longer, multi-line code blocks, you can use "fenced code blocks." You create these by wrapping your code in triple backticks (```` ``` ````).

````
```
# This is a Python comment
name = "World"
print(f"Hello, {name}!")
```
````

Renders as:
```
# This is a Python comment
name = "World"
print(f"Hello, {name}!")
```

#### Syntax Highlighting

One of the best features of fenced code blocks is syntax highlighting. You can specify the programming language right after the opening triple backticks, and many Markdown renderers will color-code your code.

````
```python
# This is a Python comment
name = "World"
print(f"Hello, {name}!")
```
````

Renders with Python-specific colors:
```python
# This is a Python comment
name = "World"
print(f"Hello, {name}!")
```

## Horizontal Rules

A horizontal rule is a simple line that can be used to create a thematic break or a visual separation between sections. You can create one by placing three or more hyphens (`---`), asterisks (`***`), or underscores (`___`) on a line by themselves.

---

## Your Next Mission

The Land Stewards are beginning to use Python to help with their data analysis. They have a small script to calculate the area of a circular oil spill, but it's currently just plain text in a report. They need your help to format it correctly. They also want to separate the different sections of their report more clearly.

Let's get to it in `practice.md`!
