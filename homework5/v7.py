file_name = input("Введите путь к файлу: ")
f = open(file_name, "r", encoding = "utf(8)")
lines = 0
i = 0
for line in f:
    arr = line.split()
    if len(arr) > 5:
        i += 1
    lines += 1
percentage = i/lines * 100
print(percentage, "% строк содержит больше 5 строк.")
f.close()
