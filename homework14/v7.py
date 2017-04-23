import os

def num_files(path):
    c = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            c += 1
    return c

def most_files(path):
    n = num_files(path)
    name = path
    for root, dirs, files in os.walk(path):
        for d in dirs:
            new = os.path.join(root, d)
            c = num_files(new)
            if c > n:
                n = c
                name = d
    return name


print(most_files('.'))
