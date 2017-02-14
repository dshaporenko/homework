f = open("isl.xml", "r", encoding = "utf(8)")
line = f.readline()
count = 1
while "</teiHeader>" not in line:
    count +=1
    line = f.readline()
f.close()
f1 = open("res.txt", "w", encoding = "utf(8)")
f1.write(str(count))
f1.close()
