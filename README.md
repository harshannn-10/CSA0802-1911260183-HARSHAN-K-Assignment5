# AT5 — CO5: Data Processing, Visualisation and Introductory AI

**Student:** Harshan K  
**Register number:** 1911260183  
**Course:** CSA08 — Python Programming

## About
This repository contains the AT5 CO5 task-wise programs for data acquisition, cleaning, normalisation, SQLite storage, visualisation, profiling, SQL security, method comparison, and introductory sentiment analysis.

## Original CO5 tasks
| Task | File | Topic |
|---|---|---|
| B1 | `AT5_CO5/TaskB1/task_b1_clean_sql.py` | Data cleaning, scaling and SQLite |
| B2 | `AT5_CO5/TaskB2/task_b2_sql_security.py` | Parameterised SQL and adversarial input |
| B3 | `AT5_CO5/TaskB3/task_b3_compare.py` | Python loop, pandas and SQL comparison |
| B4 | `AT5_CO5/TaskB4/task_b4_sentiment.py` | Lexicon sentiment and extractive summary |

## Supplementary reproducible demonstrations
The `AT5_Supplementary/python_tasks` folder contains A1–A4 and supplementary B1/B4 scripts extracted from the supplied supplementary report. These use a small synthetic air-quality sample dataset.

## Requirements
- Python 3.10 or later recommended.
- Install plotting dependency: `python -m pip install matplotlib`
- pandas is optional for Task B3: `python -m pip install pandas`
- Other scripts use the Python standard library.

## Run
From the repository root:

```powershell
python AT5_CO5/TaskB1/task_b1_clean_sql.py
python AT5_CO5/TaskB2/task_b2_sql_security.py
python AT5_CO5/TaskB3/task_b3_compare.py
python AT5_CO5/TaskB4/task_b4_sentiment.py
```

Run supplementary tasks from the repository root:

```powershell
python AT5_Supplementary/python_tasks/task_a1.py
python AT5_Supplementary/python_tasks/task_a2.py
python AT5_Supplementary/python_tasks/task_a3.py
python AT5_Supplementary/python_tasks/task_a4.py
python AT5_Supplementary/python_tasks/task_b1.py
python AT5_Supplementary/python_tasks/task_b4.py
```

## Dataset disclosure
The supplementary scripts use a synthetic demonstration dataset, not official monitoring-station measurements. Performance timings and sample sentiment agreement are illustrative and environment-dependent.

## Source note
The uploaded ZIP contained empty AT5 task folders. The programs in this repository are transcribed/reconstructed from the code appendix in the supplied AT5 report and its supplementary source appendix.

## Author
Harshan K — 1911260183
