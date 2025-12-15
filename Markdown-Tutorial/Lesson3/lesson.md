# Lesson 3: Images and Blockquotes

A picture is worth a thousand words, and a good quote can add powerful emphasis. In this lesson, we'll learn how to add both to our Markdown files.

## Adding Images

To embed an image, you use an exclamation mark, followed by alt text in square brackets, and the path or URL to the image in parentheses.

The syntax is: `![Alt text for the image](URL_or_path_to_image)`

-   **Alt text** is a short, descriptive text that appears if the image cannot be displayed. It's also very important for screen readers used by visually impaired individuals.
-   The **URL or path** can be a link to an image on the web or a local path to an image file on your computer.

For example, to add an image from the web:
`![A picture of a salmon](https://example.com/salmon.jpg)`

To add a local image from the `images` folder in our lesson directory:
`![An oil sheen on the water](./images/oil-sheen.jpg)`

## Quoting Text with Blockquotes

Blockquotes are a great way to visually set apart a quotation from the rest of your text. You create a blockquote by starting a line with a greater-than sign (`>`).

```markdown
> This is a blockquote. It's a great way to highlight a quote from a person or a document.
```

Renders as:
> This is a blockquote. It's a great way to highlight a quote from a person or a document.

You can even have multi-paragraph blockquotes:
```markdown
> This is the first paragraph.
>
> This is the second paragraph.
```

## Your Next Mission

A concerned citizen has reported an abandoned boat leaking fuel into the water at Maple Bay. The Land Stewards need to create an urgent incident report. This report must include a photo of the oil sheen on the water and a quote from the citizen's report.

Time to get to work in `practice.md`!
