import pandas

file_data = pandas.read_csv('nato_phonetic_alphabet.csv')

new_dict = {row.letter: row.code for (index, row) in file_data.iterrows()}

word_ = input('Enter a word: ').upper()

output_list = [new_dict[letter] for letter in word_]

print(output_list)
