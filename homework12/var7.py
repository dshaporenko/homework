import re

def sentences(text):
    text1 = re.split('[.?!]', text)
    return text1

def del_punct(text):
    text1 = [re.sub('[^\w\s]', '', sentence) for sentence in text]
    return text1

def count(text):
    for sentence in text:
        words = sentence.split()
        arr = []
        for word in words:
            cnt = 0
            if word not in arr:
                arr.append(word)
                for w in words:
                    if word == w:
                        cnt += 1
                if cnt > 1:
                    print(word, '{:^30}'.format(cnt))

f = open('собачка.txt', 'r', encoding = 'utf(8)')
f1 = f.read()
f1 = f1.lower()
s = sentences(f1)
d = del_punct(s)
count(d)

