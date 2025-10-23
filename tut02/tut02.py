# app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="BTP/MTP Allocation (fixed)", layout="wide")
st.title("BTP / MTP Allocation (fixed)")

# Upload CSV
uploaded = st.file_uploader(
    "Upload input CSV (Roll,Name,Email,CGPA,<Faculty columns with numeric ranks>)", 
    type=["csv"]
)
if uploaded is None:
    st.info("Please upload an input CSV to proceed.")
    st.stop()

df = pd.read_csv(uploaded)
st.subheader("Input preview")
st.dataframe(df.head(20))

# Validate first four columns
expected_prefix = ["Roll", "Name", "Email", "CGPA"]
if len(df.columns) < 5 or list(df.columns[:4]) != expected_prefix:
    st.error(f"Expected first four columns: {expected_prefix}. Found: {list(df.columns[:4])}")
    st.stop()

# Faculty columns (each column is a faculty; cell values = numeric rank: 1 best)
faculties = list(df.columns[4:])
n_faculties = len(faculties)
st.write(f"Detected {n_faculties} faculty columns (each column is a faculty).")

# Ensure CGPA numeric and sort descending
df['CGPA'] = pd.to_numeric(df['CGPA'], errors='coerce').fillna(-1)
df_sorted = df.sort_values(by='CGPA', ascending=False).reset_index(drop=True)

# Convert faculty rank columns to numeric
for f in faculties:
    df_sorted[f] = pd.to_numeric(df_sorted[f], errors='coerce')

students = df_sorted.to_dict('records')

# Helper: choose best available faculty for a student
def choose_best_faculty(stu_record, available_set):
    cand = []
    for fac in available_set:
        rank_val = stu_record.get(fac)
        if pd.isna(rank_val):
            rank = None
        else:
            rank = int(rank_val)
        cand.append((fac, rank))
    numeric_candidates = [(fac, r) for fac, r in cand if r is not None]
    if numeric_candidates:
        best = min(numeric_candidates, key=lambda x: (x[1], x[0]))
        return best[0], best[1]
    fallback = sorted([fac for fac, _ in cand])[0]
    return fallback, None

# Process in batches
batches = [students[i:i + n_faculties] for i in range(0, len(students), n_faculties)]

alloc_rows = []
pref_count = {fac: {rank: 0 for rank in range(1, n_faculties + 1)} for fac in faculties}
pref_count_total = {fac: 0 for fac in faculties}
unranked_count = {fac: 0 for fac in faculties}

for batch_idx, batch in enumerate(batches, start=1):
    available = set(faculties)
    for stu in batch:
        allocated_fac, allocated_rank = choose_best_faculty(stu, available)
        if allocated_fac in available:
            available.remove(allocated_fac)
        alloc_rows.append({
            "Roll": stu.get("Roll"),
            "Name": stu.get("Name"),
            "Email": stu.get("Email"),
            "CGPA": stu.get("CGPA"),
            "Allocated_Faculty": allocated_fac,
            "Allocated_Pref_Rank": allocated_rank if allocated_rank is not None else "",
            "Batch": batch_idx
        })
        pref_count_total[allocated_fac] += 1
        if isinstance(allocated_rank, int) and 1 <= allocated_rank <= n_faculties:
            pref_count[allocated_fac][allocated_rank] += 1
        else:
            unranked_count[allocated_fac] += 1

# Build full allocation DataFrame
alloc_df = pd.DataFrame(alloc_rows)

# Build minimal allocation DataFrame (for preview and download)
alloc_min_df = alloc_df[["Roll", "Name", "Email", "CGPA", "Allocated_Faculty"]].copy()
alloc_min_df.rename(columns={"Allocated_Faculty": "Allocated"}, inplace=True)

# Show minimal allocation preview
st.subheader("Allocation preview (first 200 rows, minimal)")
st.dataframe(alloc_min_df.head(200))

# Faculty preference statistics
fac_pref_rows = []
for fac in faculties:
    row = {"Faculty": fac}
    for r in range(1, n_faculties + 1):
        row[f"Allocated_as_pref_{r}"] = pref_count[fac].get(r, 0)
    row["Allocated_unranked_or_fallback"] = unranked_count.get(fac, 0)
    row["Total_Allocated"] = pref_count_total.get(fac, 0)
    fac_pref_rows.append(row)
fac_pref_df = pd.DataFrame(fac_pref_rows)

st.subheader("Faculty preference statistics")
st.dataframe(fac_pref_df)

# Helper to convert DataFrame to CSV bytes
def df_to_csv_bytes(df_in):
    return df_in.to_csv(index=False).encode('utf-8')

# Download buttons
st.download_button(
    "Download minimal allocation CSV", 
    data=df_to_csv_bytes(alloc_min_df),
    file_name="output_btp_mtp_allocation_minimal.csv", 
    mime="text/csv"
)
st.download_button(
    "Download faculty preference counts", 
    data=df_to_csv_bytes(fac_pref_df),
    file_name="fac_preference_count.csv", 
    mime="text/csv"
)

st.success("Done. Allocation done batch-wise with correct lowest-rank (1 is best) selection per student.")
