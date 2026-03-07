"""
Practice Tasks
Task 1

Create a DataFrame:

Name   Age   Score
Aman   21    85
Riya   22    90
Raj    20    78
Task 2

Print:

first rows
dataset info
statistical summary

Task 3 :Select the Age column.
Task 4 :Create a new column:Score + 5
Name it "AdjustedScore".
"""
data = {
    "Name" :[ "Ram", "Shyam" ,"Kewat"],
    "Age" :[23,45,34],
    "Score" : [65,45,85]
}

frame = pd.DataFrame(data);

print(frame['Age'])
frame["New_Score"] = frame["Score"] + 5
print(frame,frame.head(),frame.info(),frame.describe())