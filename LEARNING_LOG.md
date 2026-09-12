Learning Log



\## 11 September 2026 — Linearity calculation



\*\*What I built\*\*

\- Set up the project: Git repository, Python 3.13 virtual environment, pandas and numpy.

\- Created data/example\_calibration.csv with 5 standards (10-50 ug/mL) and their peak areas.

\- Wrote src/linearity.py to calculate slope, intercept, R-squared, sigma and residuals.



\*\*Result\*\*

\- Slope 100.10, intercept 17.00, R-squared 0.99970, sigma 31.57.

\- These matched the values I had worked out by hand beforehand, so the code is correct.



\*\*What I learned\*\*



1\. Least squares finds the best line by

&#x20;  \[YOUR ANSWER — what does it make as small as possible, and why square the residuals?]



2\. Sigma is divided by n - 2 because

&#x20;  \[YOUR ANSWER — what two things were calculated from the same 5 points?]



3\. R-squared is not enough on its own because

&#x20;  \[YOUR ANSWER — what can it hide that a residual plot would show?]



\*\*Problem I hit\*\*

\- I pasted the CSV data into the .py file by mistake and got a NameError. Fixed by keeping data in .csv and code in .py.

