import streamlit as st
import pandas as pd
import os
import shutil
import math
import re
import zipfile
import io


# ------------------ Utility Functions ------------------ #
def reset_output_folder(folder_path):
    """Delete and recreate a folder."""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)


def make_stats_table(groups_folder):
    """Generate department count statistics from CSV group files."""
    group_files = sorted(
        [f for f in os.listdir(groups_folder) if f.endswith(".csv")],
        key=lambda x: int(re.search(r"\d+", x).group()) if re.search(r"\d+", x) else 9999
    )
    stats = {}
    for file in group_files:
        group_name = file.replace(".csv", "").upper()
        try:
            df = pd.read_csv(os.path.join(groups_folder, file))
        except Exception:
            continue
        if "Roll" not in df.columns:
            continue
        df["Department"] = df["Roll"].astype(str).str.extract(r"([A-Z]+)")
        counts = df["Department"].value_counts().to_dict()
        counts["Total"] = len(df)
        stats[group_name] = counts

    if stats:
        stats_df = pd.DataFrame(stats).T.fillna(0).astype(int)
        stats_df.index.name = "Group"

        # --- Fix: Move 'Total' column to the end ---
        if "Total" in stats_df.columns:
            cols = [c for c in stats_df.columns if c != "Total"] + ["Total"]
            stats_df = stats_df[cols]
    else:
        stats_df = pd.DataFrame()
    return stats_df


def zip_multiple_folders_and_file(folder_map, zip_name="all_groups.zip"):
    """Zip multiple folders and files into one archive."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for subfolder_name, folder_path in folder_map.items():
            for root, _, files in os.walk(folder_path):
                for file in files:
                    filepath = os.path.join(root, file)
                    arcname = os.path.join(
                        subfolder_name,
                        os.path.relpath(filepath, folder_path)
                    )
                    zipf.write(filepath, arcname)
    buffer.seek(0)
    return buffer


# ------------------ Core Actions ------------------ #
def load_excel(uploaded_file):
    """Load uploaded Excel and keep only required columns."""
    df = pd.read_excel(uploaded_file)
    df = df.iloc[:, :3]  # Roll, Name, Email
    required_cols = ["Roll", "Name", "Email"]
    df.columns = required_cols
    df['Department'] = df["Roll"].str.extract(r'([A-Z]+)')
    return df, required_cols


def create_full_branchwise_files(df, required_cols):
    """Create full department-wise CSVs inside output folder."""
    folder = os.path.join("output", "full_branchwise")
    reset_output_folder(folder)
    for dept, group in df.groupby("Department"):
        filename = os.path.join(folder, f"{dept}.csv")
        group[required_cols].to_csv(filename, index=False)
    return folder


def branchwise_grouping(departments, k, required_cols):
    """
    Branchwise grouping: fill one group up to target size before moving
    to the next group. Saves CSVs inside output/group_branch_wise_mix.
    """
    groups = [[] for _ in range(k)]
    group_index = 0
    row = 0

    # Calculate target size per group (as even as possible)
    total_students = sum(len(df) for df in departments.values())
    base_size = total_students // k
    remainder = total_students % k
    target_sizes = [base_size + (1 if i < remainder else 0) for i in range(k)]

    while True:
        added_any = False
        for dept, df_dept in departments.items():
            if row < len(df_dept):  # still students left in this dept
                if len(groups[group_index]) < target_sizes[group_index]:
                    student = df_dept.iloc[row].to_dict()
                    groups[group_index].append(student)
                    added_any = True

                    # ✅ If this group reaches target size, move to next
                    if len(groups[group_index]) >= target_sizes[group_index]:
                        group_index = min(group_index + 1, k - 1)
        row += 1
        if not added_any:
            break

    # Save results
    folder = os.path.join("output", "group_branch_wise_mix")
    reset_output_folder(folder)
    for i, group in enumerate(groups, start=1):
        pd.DataFrame(group)[required_cols].to_csv(
            os.path.join(folder, f"g{i}.csv"), index=False
        )
    return folder



def uniform_grouping(departments, k, required_cols):
    """Distribute students uniformly across groups inside output folder."""
    total_students = sum(len(df) for df in departments.values())
    target_size = math.ceil(total_students / k)

    groups = [[] for _ in range(k)]
    group_sizes = [0] * k
    dept_remaining = {d: df.copy() for d, df in departments.items()}

    g = 0
    while any(len(df) > 0 for df in dept_remaining.values()):
        dept = max(dept_remaining, key=lambda d: len(dept_remaining[d]))
        df_dept = dept_remaining[dept]
        if len(df_dept) == 0:
            continue
        space_left = target_size - group_sizes[g]
        take = min(space_left, len(df_dept))
        students = df_dept.iloc[:take].to_dict(orient="records")
        groups[g].extend(students)
        group_sizes[g] += take
        dept_remaining[dept] = df_dept.iloc[take:].reset_index(drop=True)
        if group_sizes[g] >= target_size:
            g = (g + 1) % k

    folder = os.path.join("output", "group_uniform_mix")
    reset_output_folder(folder)
    for i, group in enumerate(groups, start=1):
        pd.DataFrame(group).to_csv(os.path.join(folder, f"g{i}.csv"), index=False)
    return folder


def save_statistics(branchwise_folder, uniform_folder):
    """Save stats to Excel inside output folder."""
    branchwise_stats = make_stats_table(branchwise_folder)
    uniform_stats = make_stats_table(uniform_folder)

    output_file = os.path.join("output", "output.xlsx")
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        start_row = 0
        if not branchwise_stats.empty:
            pd.DataFrame([["Branch Wise Mix"]]).to_excel(
                writer, sheet_name="Statistics", startrow=start_row, header=False, index=False
            )
            start_row += 2
            branchwise_stats.to_excel(writer, sheet_name="Statistics", startrow=start_row)
            start_row += len(branchwise_stats) + 3
        if not uniform_stats.empty:
            pd.DataFrame([["Uniform Mix"]]).to_excel(
                writer, sheet_name="Statistics", startrow=start_row, header=False, index=False
            )
            start_row += 2
            uniform_stats.to_excel(writer, sheet_name="Statistics", startrow=start_row)

    return branchwise_stats, uniform_stats, output_file


# ------------------ Streamlit UI ------------------ #
st.title("🎯 Student Group Maker")

uploaded_file = st.file_uploader("Upload input_Make Groups.xlsx", type=["xlsx"])
k_branchwise = st.number_input("Number of groups for Branchwise Mix", min_value=1, value=3)
k_uniform = st.number_input("Number of groups for Uniform Mix", min_value=1, value=3)

if st.button("Run Grouping"):
    if uploaded_file is None:
        st.error("Please upload an Excel file first!")
    else:
        # Reset master output folder
        reset_output_folder("output")

        # Step 1: Load Excel
        df, required_cols = load_excel(uploaded_file)

        # Step 2: Create full branchwise files
        branch_folder = create_full_branchwise_files(df, required_cols)

        # Step 3: Load departments back
        departments = {}
        for file in sorted(os.listdir(branch_folder)):
            if file.endswith(".csv"):
                dept = file.replace(".csv", "")
                df_dept = pd.read_csv(os.path.join(branch_folder, file))
                df_dept = df_dept[required_cols].dropna(subset=["Roll"])
                departments[dept] = df_dept.reset_index(drop=True)

        # Step 4: Create Branchwise Groups
        branchwise_folder = branchwise_grouping(departments, k_branchwise, required_cols)

        # Step 5: Create Uniform Groups
        uniform_folder = uniform_grouping(departments, k_uniform, required_cols)

        # Step 6: Save statistics to Excel inside output/
        branchwise_stats, uniform_stats, output_file = save_statistics(branchwise_folder, uniform_folder)

        # Step 7: Show results
        st.success("✅ Groups created successfully!")
        st.write("### 📊 Branchwise Stats")
        st.dataframe(branchwise_stats)
        st.write("### 📊 Uniform Stats")
        st.dataframe(uniform_stats)

        # Step 8: Previews
        for label, folder in {
            "Branchwise Groups": branchwise_folder,
            "Uniform Groups": uniform_folder,
            "Full Branchwise Department Files": branch_folder
        }.items():
            st.write(f"### 📂 Preview {label}")
            for file in sorted(os.listdir(folder), key=lambda x: int(re.search(r"\d+", x).group()) if re.search(r"\d+", x) else 9999):
                with st.expander(f"🔍 Preview {file}"):
                    df_preview = pd.read_csv(os.path.join(folder, file)).head(20)
                    st.dataframe(df_preview)

        # Step 9: Download buttons
        with open(output_file, "rb") as f:
            st.download_button("⬇️ Download Output Excel", f, file_name="output.xlsx")

        all_zip = zip_multiple_folders_and_file({"output": "output"})
        st.download_button(
            "⬇️ Download All (Groups + Stats Excel)",
            all_zip,
            file_name="all_groups.zip",
            mime="application/zip"
        )
