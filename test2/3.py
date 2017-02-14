import re

f = open("isl.xml", "r", encoding = "utf(8)")
f1 = open("res2.txt", "w", encoding = "utf(8)")
for line in f:
    m = re.search(r'type="f.h\w*">', line)
    if m != None:
        s = line[m.end():]
        n = re.search(r'\w*', s)
        if n != None:
            f1.write(n.group() + ', ')
f1.close()
f.close()

f = open("isl.xml", "r", encoding = "utf(8)")
f1 = f.read()
a = re.search("<body>", f1)
b = re.search(r"\s*</body>", f1)
f2 = f1[a.end()+1:b.start()]
dtags = re.sub(r'<.*?>', '', f2, flags = re.DOTALL)
f.close()

#тут не до конца доделано
