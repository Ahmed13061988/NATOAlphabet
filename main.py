student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


nato = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {code.letter: code.code for (letter, code) in nato.iterrows()}
user_input = input("Enter a word: ").upper()
user_list = []
users_list = [nato_dict[word] for word in user_input]
print(users_list)
# for letter in user_input:
#     fix = nato_dict.get(letter)
#     user_list.append(fix)
# print(user_list)




