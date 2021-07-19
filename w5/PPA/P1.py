
def upper(s):
    upper = 0
    for c in s:
        if c.isupper():
            upper += 1
    return(upper)

def lower(s):
    lower = 0
    for c in s:
        if c.islower():
            lower += 1
    return lower

def word_count(s):
    space = 0
    for c in s:
        if c.isspace():
            space += 1
    return space+1

sentence = input("Enter the sentence :")
uLetters = upper(sentence)
lLetters = lower(sentence)
length = len(sentence)
words = word_count(sentence)
print(f'{uLetters} {lLetters} {length} {words}')