# Lesson 4: Quiz Solutions

Here are the answers to the quiz:

**Question 1:** How do you create a fenced code block for JavaScript code?
**Answer:** c) ` ```javascript ... ``` `

**Question 2:** Which of the following will create a horizontal rule?
**Answer:** a) `---` (You can also use `***` or `___`)

**Question 3:** How do you format a single word or function name as inline code?
**Answer:** c) By surrounding it with `` ` ``.

---

### Practice Solution

Here is the solution to the practice exercise:

````markdown
# Technical Brief: Spill Area Calculation

This document contains the Python script used for calculating the estimated area of a circular spill. The function to use is called `calculate_spill_area`.

---

## Python Script

```python
import math

def calculate_spill_area(radius):
  """Calculates the area of a circular spill given a radius."""
  return math.pi * (radius ** 2)

# Example usage:
spill_radius = 10 # meters
area = calculate_spill_area(spill_radius)
print(f"The estimated spill area is {area:.2f} square meters.")
```

---

End of technical brief.
````
