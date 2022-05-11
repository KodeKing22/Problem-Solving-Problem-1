# Problem_Solving_Problems_Part_1

# Problems to Solve

# 1. Reverse a string (HINT: Review the Algorithms + Problem Solving PowerPoint!)

word = 'Bogus'
reversed_word = ''

for index in range(len(word) -1, -1, -1):
    reversed_word += word[index]

print(reversed_word)

# a. Write code that takes a string as input and returns the string reversed

from turtle import title


def print_reversed_word(): 
    new_word = input('What word do you want reversed? ')
   
    reversed_word = ''

    for index in range(len(new_word) -1, -1, -1):
        reversed_word += new_word[index]
    return reversed_word

reversed_input = print_reversed_word()
print('Your word reversed: ' + reversed_input)

# b. i.e. “Hello” will be returned as “olleH”

# 2. Capitalize letter

# a. Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”
string = input('Enter string without capital letters: ')
def string_letter_capitalize(string): 
        new_string = string.title()
        return new_string
   
 
#    txt.capitalize(txt.split(string)):
#         list_split_caps = txt.capitalize(txt.split)
#         return list_split_caps

string_letter_capitalize(string)

capitalized_string = string_letter_capitalize(string)
print(capitalized_string)

# 3. Palindrome

# a. A word, phrase, or sequence that reads the same backward as forward i.e. madam
# racecar
# b. Write code that takes a user input and checks to see if it is a Palindrome and reports the result

# 4. BONUS CHALLENGE: Compress a string of characters

# a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"