a = []
for i in range(8):
    new_element = input()
    a.append(new_element)
for i in range(0, 8, 2):
    print(a[i], a[i+1], sep = '')
    
