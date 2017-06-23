import re
import os

def sentences(text):
    text1 = re.split('[.?!]', text)
    return text1

def lengths(folder):
    d = {}
    for f in os.listdir(folder):
        text = open(os.path.join(folder, f), 'r')
        s = text.read()
        text.close()
        m = re.sub(u'<.*?>', u'', s, flags = re.DOTALL)
        s1 = sentences(m)
        d[f] = len(s1)
    return d

def write_lengths(d):
    f = open('text.txt', 'w')
    for key in d:
        f.write(key + '{:>6}'.format(d[key]) + '\n')
    f.close()

folder = 'news'
d = lengths(folder)
write_lengths(d)

