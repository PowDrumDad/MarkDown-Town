import csv

def generate_report():
    """
    Reads salmon data from a CSV and generates a Markdown report.
    """
    report_md = ""
    
    # TODO 1: Add the main title for the report.
    # It should be a Level 1 Heading: "# Weekly Salmon Count Report"
    

    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # The 'row' variable is a dictionary.
            # You can access data like this: row['river'], row['species'], row['count']
            
            # TODO 2: Add a Level 2 Heading for each river.
            # Example: "## Cowichan River"
            

            # TODO 3: Add a bullet point with the species and count.
            # Example: "- Sockeye: 1520"
            
            # TODO: Implement loop body - see lesson instructions
            pass

    with open('salmon_report.md', 'w') as report_file:
        report_file.write(report_md)

    print("Successfully generated salmon_report.md")

if __name__ == "__main__":
    generate_report()
