def words():
    file = input("Название файла: ")
    f = open(file, "r", encoding = "utf(8)")
    f1 = f.read()
    f1 = f1.lower()
    arr = f1.split()
    for i, word in enumerate(arr):
        arr[i] = word.strip('.,:;!?"()')
    f.close()
    return arr

def un():
    arr = words()
    arr1 = []
    for word in arr:
        if word[0] == "u" and word[1] == "n":
            arr1.append(word)
    return arr1

def percentage():
    arr = un()
    un_number = len(arr)
    print(un_number, "слов с приставкой un")
    count = 0
    length = int(input("Cлова длиннее, чем: "))
    for word in arr:
        if len(word) > length:
            count += 1
    percent = count/un_number * 100
    return percent

number = percentage()
print(number, "%")
