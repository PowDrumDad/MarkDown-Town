# Lesson 7: Advanced Markdown - The Python Connection

Welcome to our most advanced lesson! So far, we've been writing Markdown by hand. But what if we could generate our reports automatically? In this lesson, we'll see how we can use a simple Python script to create a Markdown file from a data source.

## The Power of Automation

Imagine The Land Stewards conduct the same survey every week. They collect data, and then someone has to manually type up a report in Markdown. This is time-consuming and prone to errors.

By using a programming language like Python, we can automate this entire process. We can write a script that:
1.  Reads data from a source (like a CSV file, a database, or an API).
2.  Processes that data.
3.  Writes the data into a new `.md` file, complete with all the Markdown formatting we've learned (headings, lists, tables, etc.).

## How it Works

We'll be working with a simple Python script that reads from a CSV (Comma-Separated Values) file. A CSV file is a basic spreadsheet format that's easy for both humans and computers to read.

Our script will:
1.  Open a CSV file containing survey data.
2.  Open a new `.md` file to write to.
3.  Write a title and introduction.
4.  Loop through the data in the CSV file.
5.  For each row of data, it will format and write a section to our Markdown file.
6.  Save the completed report.

## Your Final Mission

The Land Stewards have a CSV file with the latest salmon count data from several rivers. They want to create a script that generates a summary report from this data automatically. This is your most important mission yet, as it will save them hours of work each week!

You'll find the data in `data.csv` and a starter script in `generate_report.py`. Head over to `practice.md` for your instructions.
