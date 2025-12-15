# Lesson 5: Tables

Tables are an excellent way to display structured data, like spreadsheets or database records, in a clean and organized way.

## Creating Tables

The syntax for tables can look a little complex at first, but it's quite logical. You use pipes (`|`) to separate columns and hyphens (`-`) to create the header row separator.

Here's the basic structure:

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1, Col 1 | Row 1, Col 2 | Row 1, Col 3 |
| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |
```

Renders as:

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1, Col 1 | Row 1, Col 2 | Row 1, Col 3 |
| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |

### Alignment

You can align the text in your columns by adding colons (`:`) to the header separator line.

-   **Left-align (default):** `|:---|` or `|----|`
-   **Right-align:** `|---:|`
-   **Center-align:** `|:---:|`

Example:
```markdown
| Item | Quantity | Price (CAD) |
|:-----------|:----------:|------------:|
| Water Sample Kit | 10 | 25.50 |
| GPS Unit | 2 | 350.00 |
| Waterproof Notebook | 25 | 5.75 |
```

Renders as:

| Item | Quantity | Price (CAD) |
|:-----------|:----------:|------------:|
| Water Sample Kit | 10 | 25.50 |
| GPS Unit | 2 | 350.00 |
| Waterproof Notebook | 25 | 5.75 |

## Your Next Mission

The Land Stewards have collected water quality data from three different locations in the Cowichan River. They need you to organize this data into a table for their weekly report so they can easily compare the results.

Let's get this data organized in `practice.md`!
