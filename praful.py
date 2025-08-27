import streamlit as st
import pandas as pd
import os
import re
import math
from io import BytesIO

st.set_page_config(page_title="Student Group Generator", layout="wide")


# ------------------- Helper Functions -------------------

def clear_old_data(folder_path):
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".csv"):
                os.remove(os.path.join(folder_path, file))
    else:
        os.makedirs(folder_path)


def make_stats_table(groups_dict):
    stats = {}
    for gname, df in groups_dict.items():
        if "Roll" not in df.columns:
            continue
        df["Department"] = df["Roll"].astype(str).str.extract(r"([A-Z]+)")
        counts = df["Department"].value_counts().to_dict()
        counts["Total"] = len(df)
        stats[gname] = counts

    if stats:
        stats_df = pd.DataFrame(stats).T.fillna(0).astype(int)
        dept_cols = sorted([col for col in stats_df.columns if col != "Total"])
        ordered_cols = dept_cols + (["Total"] if "Total" in stats_df.columns else [])
        stats_df = stats_df[ordered_cols]
        stats_df.index.name = "Group"
        return stats_df
    else:
        return pd.DataFrame()


def generate_branchwise_groups(departments, k, required_cols):
    groups = [[] for _ in range(k)]
    row = 0
    group_index = 0
    while True:
        added_any = False
        for dept, df in departments.items():
            if row < len(df):
                student = df.loc[row, required_cols].to_dict()
                groups[group_index].append(student)
                added_any = True
        row += 1
        group_index = (group_index + 1) % k
        if not added_any:
            break
    return {f"Group {i+1}": pd.DataFrame(g) for i, g in enumerate(groups)}


def generate_uniform_groups(departments, k, required_cols):
    total_students = sum(len(df) for df in departments.values())
    group_size = math.ceil(total_students / k)
    groups = [[] for _ in range(k)]

    remaining_students = {dept: len(df) for dept, df in departments.items()}
    current_indices = {dept: 0 for dept in departments}

    group_index = 0
    while sum(remaining_students.values()) > 0:
        dept = max(remaining_students, key=remaining_students.get)
        if remaining_students[dept] == 0:
            break

        count_to_add = min(group_size - len(groups[group_index]), remaining_students[dept])
        start_idx = current_indices[dept]
        end_idx = start_idx + count_to_add

        group_students = departments[dept].iloc[start_idx:end_idx][required_cols].to_dict(orient="records")
        groups[group_index].extend(group_students)

        current_indices[dept] = end_idx
        remaining_students[dept] -= count_to_add

        if len(groups[group_index]) >= group_size:
            group_index = (group_index + 1) % k

    return {f"Group {i+1}": pd.DataFrame(g) for i, g in enumerate(groups)}


def to_excel_buffer(branchwise_stats, uniform_stats):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
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
    output.seek(0)
    return output


# ------------------- Streamlit App -------------------

st.title("📊 Student Group Generator")

uploaded_file = st.file_uploader("Upload students.xlsx", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file).iloc[:, :3]
    required_cols = ["Roll", "Name", "Email"]

    df['Department'] = df["Roll"].astype(str).str.extract(r'([A-Z]+)')

    st.write("### 📂 All Students Data")
    st.dataframe(df, use_container_width=True)

    # Save branch-wise CSVs internally (not physical files here)
    departments = {
        dept: group.drop(columns="Department").reset_index(drop=True)
        for dept, group in df.groupby("Department")
    }

    k = st.number_input("Enter number of groups:", min_value=1, max_value=50, value=4, step=1)

    if st.button("Generate Groups"):
        with st.spinner("Processing..."):

            # Branchwise mix groups
            branchwise_groups = generate_branchwise_groups(departments, k, required_cols)
            branchwise_stats = make_stats_table(branchwise_groups)

            # Uniform mix groups
            uniform_groups = generate_uniform_groups(departments, k, required_cols)
            uniform_stats = make_stats_table(uniform_groups)

            # --- Display branchwise groups ---
            st.subheader("📌 Branchwise Mix Groups")
            for gname, gdf in branchwise_groups.items():
                st.markdown(f"{gname}** ({len(gdf)} students)")
                st.dataframe(gdf, use_container_width=True)

            # --- Display uniform groups ---
            st.subheader("📌 Uniform Mix Groups")
            for gname, gdf in uniform_groups.items():
                st.markdown(f"{gname}** ({len(gdf)} students)")
                st.dataframe(gdf, use_container_width=True)

            # --- Stats ---
            st.subheader("📊 Group Statistics Comparison")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("*Branchwise Mix Stats*")
                st.dataframe(branchwise_stats)
            with col2:
                st.markdown("*Uniform Mix Stats*")
                st.dataframe(uniform_stats)

            # --- Download Excel ---
            excel_buffer = to_excel_buffer(branchwise_stats, uniform_stats)
            st.download_button(
                "📥 Download Stats Excel",
                data=excel_buffer,
                file_name="group_statistics.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )

else:
    st.info("👆 Please upload a students.xlsx file to begin")