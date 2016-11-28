line = input() 
j = len(line) - 1
k = 1
for i in range(len(line)//2):
    print(line[k:j:])
    j = j-1
    k = k+1
