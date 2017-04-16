import os
import re
    
def cyr_lat(path):
    names = os.listdir(path)
    count = 0
    for name in names:
        path1 = os.path.join(path, name)
        if os.path.isdir(path1):
            if re.search('[a-zA-Z]', name) and re.search('[а-яА-Я]', name):
                count+=1
    return count

n = cyr_lat('.')
print(os.listdir('.'))
print(n)
