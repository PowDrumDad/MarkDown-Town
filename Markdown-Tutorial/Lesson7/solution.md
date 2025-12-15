# Lesson 7: Quiz Solutions

Here are the answers to the quiz:

**Question 1:** What is the primary benefit of generating Markdown with a script?
**Answer:** c) It automates the creation of reports from data, saving time and reducing errors.

**Question 2:** What is a CSV file?
**Answer:** c) A Comma-Separated Values file, a simple spreadsheet-like format for data.

**Question 3:** In our Python script, what is the general process for creating the report?
**Answer:** a) Read data, open a Markdown file, loop through data writing formatted lines, save the file.

---

### Practice Solution

Here is the solution to the practice exercise.

#### `solution_script.py`

```python
import csv

def generate_report():
    """
    Reads salmon data from a CSV and generates a Markdown report.
    """
    report_md = ""
    
    # Add the main title
    report_md += "# Weekly Salmon Count Report\n\n"

    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # Add a heading for each river
            report_md += f"## {row['river']}\n"
            # Add a list item for the species and count
            report_md += f"- {row['species']}: {row['count']}\n\n"

    with open('salmon_report.md', 'w') as report_file:
        report_file.write(report_md)

    print("Successfully generated salmon_report.md")

if __name__ == "__main__":
    generate_report()
```

#### Generated `salmon_report.md`

```markdown
# Weekly Salmon Count Report

## Cowichan River
- Sockeye: 1520

## Chemainus River
- Chum: 3250

## Nanaimo River
- Coho: 850

## Koksilah River
- Chinook: 430

```
