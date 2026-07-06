import pandas as pd
# Create the DataFrame
students = {
    "Roll No": [101, 102, 103, 104, 105],
    "Name": ["Anu", "Rahul", "Priya", "John", "Meena"],
    "Department": ["CSE", "IT", "ECE", "CSE", "IT"],
    "Age": [20, 21, 19, 20, 22],
    "Marks": [89, 76, 92, 65, 84]
}
df = pd.DataFrame(students)
print("===== Complete DataFrame =====")
print(df)
print("\n===== Name and Marks =====")
print(df[["Name", "Marks"]])
print("\n===== Student with Highest Marks =====")
print(df.loc[df["Marks"].idxmax()])
print("\n===== Student with Lowest Marks =====")
print(df.loc[df["Marks"].idxmin()])
average_marks = df["Marks"].mean()
print("\nAverage Marks:", average_marks)
print("\n===== Students Scoring 80 or Above =====")
print(df[df["Marks"] >= 80])
print("\n===== IT Department Students =====")
print(df[df["Department"] == "IT"])
def grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "F"
df["Grade"] = df["Marks"].apply(grade)
print("\n===== DataFrame with Grade =====")
print(df)
sorted_df = df.sort_values(by="Marks", ascending=False)
print("\n===== Sorted by Marks (Descending) =====")
print(sorted_df)
sorted_df.to_csv("students.csv", index=False)
print("\nstudents.csv has been saved successfully.")
new_df = pd.read_csv("students.csv")
print("\n===== Data Read from students.csv =====")
print(new_df)