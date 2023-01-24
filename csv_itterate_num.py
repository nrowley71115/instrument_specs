"""This program is not integral for the overarching program. I used this to output a series of numbers that I could input into a csv file
This issue was I needed 4 digit numbers before 3 digit numbers, 3 before 2, and so on.
I'll keep this file incase I need to generate a large amount of numbers for codes on a CSV file again"""

# in this example, The code was the leading number followed by a length. For example, a 12 in teflon cable's code would be '312'
description_code_dictionary = {'Fiberglass braid': "1", "Teflon (Standard)": "3", "High temperature fiberglass braid": '4', 'Kapton (Standard for Cryogenic)': '5', 'Other - specify': 'X'}

# initalize variable
csv_text = ''


for key, value in description_code_dictionary.items():

    for i in range(100, 400):
        csv_text += f'{value}{i}, {key} {i}in long\n'

    for i in range(10, 100):
        csv_text += f'{value}{i}, {key} {i}in long\n'

    for i in range(0, 10):
        csv_text += f'{value}{i}, {key} {i}in long\n'

with open('csv_itterate_num.txt', 'w') as f:
    f.write(csv_text)