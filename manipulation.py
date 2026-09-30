str_manip = input("Enter a sentence : ")
length = len(str_manip)
print(length)
last_letter = str_manip[-1]
replace_str = str_manip.replace(last_letter, "@")
print(replace_str)
last_three_backwards =str_manip[-1:-4:-1]
print(f"last 3 character backward :{last_three_backwards}")
five_letter_word = str_manip[:3] + str_manip[-2:]
print("five letter word :",five_letter_word)