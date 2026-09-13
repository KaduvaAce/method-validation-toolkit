\# Method Validation Toolkit



Python tools that perform ICH Q2(R2) analytical method validation

calculations, verified by reproducing values published in peer-reviewed

HPLC papers.



\## What it does



Reads calibration and recovery data from CSV and calculates:



\- \*\*Linearity\*\* - least-squares slope, intercept, R-squared, r, residuals

\- \*\*LOD / LOQ\*\* - configurable factors and sigma method

\- \*\*Precision\*\* - %RSD against a configurable limit

\- \*\*Accuracy\*\* - % recovery at multiple levels



Acceptance limits and calculation options live in `config/limits.yaml`.

No limit is hard-coded.



\## Verification against published papers



Rather than testing against values I generated myself, each calculation is

checked against data published in open-access papers. Where a recalculated

value differs from the published one, the difference is compared against a

tolerance derived from the paper's own reporting precision.



| Paper | Checks | Reproduced |

|---|---|---|

| Mesalamine, BMC Chem 2025 | 3 recovery, 1 regression | 3/3 recovery; regression not reproduced |

| Caffeine, Electron J Gen Med 2019 | 3 recovery | 0/3 |

| Dihydropyridines, BMC Chem 2025 | 15 recovery | 12/15 |



\*\*Total: 15 of 21 recovery values reproduced within rounding tolerance.\*\*



Full extraction notes, published values and per-paper findings are in

`data/papers/*_SOURCE.md`, each with its DOI and licence.



\### How tolerance is set



Tolerance is calculated from two sources of rounding, not chosen to fit:



\- rounding of the reported "found" value: `(0.005 / added) x 100`

\- rounding of the reported recovery itself: `0.005` percentage points



This scales with concentration. A fixed tolerance would fail low levels and

pass high ones for the same underlying agreement.



\### Selected findings



\*\*Mesalamine (BMC Chem 2025).\*\* Recalculating the regression from the

published Table 1 (n = 7) gives slope 417.13, intercept +337.04,

R-squared 0.9989. The published equation is y = 173.53x - 2435.64. The

R-squared agrees to 0.0003 while the coefficients do not, which is

consistent with the fit having been performed on these data and the

reported coefficients originating elsewhere. Switching the sigma method

from residual SD to intercept standard error changes the LOD by 2.4%,

against a 655% gap to the published value, so the sigma convention does

not account for the difference.



\*\*Caffeine (Electron J Gen Med 2019).\*\* All three recovery values

recalculate lower than reported (-0.031, -0.043, -0.153 percentage points).

Two exceed rounding tolerance. The consistent direction is not what

rounding produces.



\*\*Dihydropyridines (BMC Chem 2025).\*\* Twelve of fifteen reproduce. The

three that do not differ by exactly -0.030 percentage points each; an

identical magnitude across three entries is not consistent with random

rounding. Cause not determinable from published information.



\*\*r versus R-squared.\*\* Two of the three papers report a "correlation

coefficient" where the value appears to be R-squared. The distinction

matters: R-squared = 0.9989 fails a 0.999 limit, while r = sqrt(R-squared)

= 0.99945 passes. The toolkit reports both.



\## Limitations



\- This is a learning and portfolio project. It is \*\*not\*\* validated

