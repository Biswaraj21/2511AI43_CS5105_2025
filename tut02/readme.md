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

