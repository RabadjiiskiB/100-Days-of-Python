student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
df = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row["letter"]: row["code"] for (index, row) in df.iterrows()}

input = input("Enter your name ").upper()
try:
    word = [dict.get(s) for s in input]
except KeyError:
    print("Invalid input")
print(word)
for (index, row) in student_data_frame.iterrows():
    pass

