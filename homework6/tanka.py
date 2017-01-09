import random

def words(file):
    f = open(file, "r", encoding = "utf(8)")
    f1 = f.read()
    arr = f1.split()
    f.close()
    return arr

def noun(number):
    singular = words("sing_nouns.txt")
    plural = words("pl_nouns.txt")
    if number == 's':
        return random.choice(singular)
    return random.choice(plural)

def noun2():
    nouns = words("nouns2.txt")
    return random.choice(nouns)

def punctuation():
    marks = [".", "?", "!", "..."]
    return random.choice(marks)

def verb(syllables):
    verbs2 = words("verbs2.txt")
    verbs3 = words("verbs3.txt")
    if syllables == 2:
        return random.choice(verbs2)
    return random.choice(verbs3)

def noun_phrase():
    clitics = words("clitics.txt")
    clitic = random.choice(clitics)
    noun1 = noun('s')
    return clitic + ' ' + noun1

def verse1():
    return noun('s') + ' ' + verb(3) + punctuation()

def verse2():
    return noun('s') + ' ' + verb(2) + ' ' + noun('pl') + punctuation()

def verse3():
    return verb(3) + ' ' + noun('s') + punctuation()

def verse4():
    return noun_phrase() + ' ' + verb(2) + ' ' + noun2() + punctuation()

def make_verse(syllables):
    if syllables == 5:
        verse = random.choice([1,3])
        if verse == 1:
            return verse1()
        else:
            return verse3()
    else:
        verse = random.choice([2,4])
        if verse == 2:
            return verse2()
        else:
            return verse4()

print(make_verse(5))
print(make_verse(7))
print(make_verse(5))
print(make_verse(7))
print(make_verse(7))
