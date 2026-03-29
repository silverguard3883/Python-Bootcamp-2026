import pandas

with open("nato_phonetic_alphabet.csv", "r") as file:

    """Creates dictionary from the .csv file"""
    nato = pandas.read_csv(file).set_index("letter")["code"].to_dict()

user_input = input("Please enter a name: ").upper()

"""Iterates with index "letter" through "user_input", using each iterated letter as a key to retrieve the value (NATO code)"""
phonetic_list = [nato[letter] for letter in user_input]
print(phonetic_list)
