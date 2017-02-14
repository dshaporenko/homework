f = open("isl.xml", "r", encoding = "utf(8)")
d = {}
for line in f:
    if "<w lemma=" in line:
        a = line.find('type="')
        a += 6
        b = line.rfind('"')
        key = line[a:b]
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
f.close()
f1 = open("res1.txt", "w", encoding = "utf(8)")
for key in d:
    f1.write(key + ", " + str(d[key]) + "\n")
f1.close()
