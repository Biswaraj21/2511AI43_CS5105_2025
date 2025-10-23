# BTP/MTP Allocation Web App

This is a **Streamlit-based web application** for allocating students to faculty for BTP (Bachelor Thesis Project) or MTP (Master Thesis Project) based on student preferences and CGPA.

---

## Features

- Upload a CSV file containing student details and faculty preference ranks.
- Automatic batch-wise allocation based on CGPA (highest first) and student faculty preferences.
- Handles missing or invalid ranks gracefully (fallback allocation if needed).
- Preview allocation results and faculty preference statistics in the app.
- Download:
  - Minimal allocation CSV (`Roll, Name, Email, CGPA, Allocated`)
  - Faculty preference statistics CSV

---

## Input CSV Format

The input CSV must contain the following columns:


- First four columns **must** be: `Roll`, `Name`, `Email`, `CGPA`.
- Faculty columns should have numeric ranks for each student (1 = highest preference). Missing or empty values are allowed.

**Example:**

| Roll  | Name       | Email            | CGPA | ProfA | ProfB | ProfC |
|-------|------------|-----------------|------|-------|-------|-------|
| 101   | Alice      | a@example.com   | 9.2  | 1     | 2     | 3     |
| 102   | Bob        | b@example.com   | 8.5  | 2     | 1     |       |

---

## Output

- **Minimal allocation CSV**:  
  Columns: `Roll, Name, Email, CGPA, Allocated`  

- **Faculty preference statistics CSV**:  
  Shows number of students allocated per faculty, broken down by preference rank.

---

## Installation

1. Clone this repository:

```bash
git clone <repo-url>
cd <repo-folder>


python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
