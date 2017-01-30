import re

rex = r"\bси(жу|д(я(т|щ(и(й|е|х|ми?)|е(го|му?|й|е)|ая|ую))?|и(шь|т(е|ся)?)?|е(ть|л(а|о(сь)?|и)?|в(ш(и(й|е|х|ми?)?|е(го|му?|й|ю|е)|ая|ую))?)))\b"

file = input("Введите название файла: ")
f = open(file, "r", encoding = "utf(8)")
f1 = f.read()
f1 = f1.lower()
arr = f1.split()
for i, word in enumerate(arr):
    arr[i] = word.strip('.,:;&!«»()/-')
f.close()

found = []
for word in arr:
    m = re.search(rex, word)
    if m != None:
        if word not in found:
            print(word)
            found.append(word)
