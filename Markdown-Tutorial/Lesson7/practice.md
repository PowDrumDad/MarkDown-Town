# Lesson 7: Practice

**Your Assignment:**

Your goal is to complete the Python script `generate_report.py` to automatically create a Markdown report named `salmon_report.md`.

1.  **Examine the Data:** Open `data.csv` to understand its structure. You'll see it has three columns: `river`, `species`, and `count`.

2.  **Open the Script:** Open the `generate_report.py` file. You'll see it already has some code, but there are parts marked with `# TODO` that you need to complete.

3.  **Complete the Script:**
    *   **TODO 1:** The script needs to write a main (Level 1) heading to the report file. The title should be `Weekly Salmon Count Report`.
    *   **TODO 2:** Inside the `for` loop, the script is reading each row of data. For each row, you need to write a Level 2 heading to the report file that includes the river name. For example: `## Cowichan River`.
    *   **TODO 3:** Below the river name heading, create an unordered list that contains the species and the count. For example: `- Sockeye: 1500`.

4.  **Run the Script:** Once you've filled in the `TODO` sections, run the script from your terminal. If you're in the `Lesson7` directory, you can run it with the command: `python generate_report.py`.

5.  **Check the Output:** If your script is correct, it will create a new file called `salmon_report.md`. Open it to see your automatically generated report!

Compare your generated report and your script with the files in `solution.md`.
