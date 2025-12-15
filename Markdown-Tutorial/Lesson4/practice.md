# Lesson 4: Practice

**Your Assignment:**

Format a technical brief for The Land Stewards.

1.  Create a main heading: `Technical Brief: Spill Area Calculation`.
2.  Add an introductory paragraph:
    `This document contains the Python script used for calculating the estimated area of a circular spill. The function to use is called 'calculate_spill_area'.`
3.  In the paragraph above, make `calculate_spill_area` appear as inline code.
4.  Add a horizontal rule to separate the introduction from the code.
5.  Add a Level 2 heading: `Python Script`.
6.  Below the heading, create a fenced code block with Python syntax highlighting for the following script:

```
import math

def calculate_spill_area(radius):
  """Calculates the area of a circular spill given a radius."""
  return math.pi * (radius ** 2)

# Example usage:
spill_radius = 10 # meters
area = calculate_spill_area(spill_radius)
print(f"The estimated spill area is {area:.2f} square meters.")
```
7. Add another horizontal rule after the code block.
8. Add a concluding sentence: `End of technical brief.`
