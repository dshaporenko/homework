import random

d = {}
file = open("words.csv", "r")
for line in file:
    line = line.strip('\n')
    arr = line.split(';')
    d[arr[0]] = arr[1]
file.close()

a = []
for key in d:
    a.append(key)
word = random.choice(a)

print("Подсказка:", word, "...")
noun = input()

if noun == d[word]:
    win = ["ура!", "вы отгадали", "победа"]
    print(random.choice(win))
else:
    lose = ["вы не отгадали", "вы проиграли", "попробуйте еще раз"]
    print(random.choice(lose))
