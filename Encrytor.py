letter_no = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10,
    'k' : 11,
    'l' : 12,
    'm' : 13,
    'n' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26,
    '1' : 29,
    '2' : 30,
    '3' : 31,
    '4' : 32,
    '5' : 33,
    '6' : 34,
    '7' : 35,
    '8' : 36,
    '9' : 37,
    '0' : 38,
}

def string_reverse(string):
    return string[::-1]
def word_1(string):
    to_return = ""
    final = ""
    letter_to_remove = string[0]
    for letters in string:
        if letters != letter_to_remove:
            to_return += letters
    final = to_return + letter_to_remove
    return final
def word_2(string):
    final_out = ""
    pos = []
    lett = []
    for letters in string:
        lett.append(letters)
    for i,letter in enumerate(lett):
        print(i,letter)
        lett.append(letter_no[letter])
    print(lett)
    for no in pos:
        if no > 26:
            pass
        if no == 25 or no == 26:
            if no == 25:
                no = 1
            else:
                no = 2
        else:
            no += 2
    for no in pos:
        for key, value in letter_no.items():
            if value == no:
                answer = key
                final_out += answer
                break
    return final_out

word = input("Enter a word: ")
word = word.lower()
print(word)
word = word_1(word)
word = string_reverse(word)
word = word_2(word)
print(word)
