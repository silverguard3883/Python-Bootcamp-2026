import pandas

with open("nato_phonetic_alphabet.csv", "r") as file:

    """Creates dictionary from the .csv file"""
    nato = pandas.read_csv(file).set_index("letter")["code"].to_dict()

def generate_phonetic_alphabet():
    user_input = input("Please enter a name: ").upper()
    try:
        """Iterates with index "letter" through "user_input", using each iterated letter as a key to retrieve the value (NATO code)"""
        phonetic_list = [nato[letter] for letter in user_input]
    except KeyError:
        print("Please use only alphabetical letters")
        generate_phonetic_alphabet()
    else:
        print(phonetic_list)

generate_phonetic_alphabet()
