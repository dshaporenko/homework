import re

f = open("Птицы.html", "r", encoding = "utf(8)")
f1 = f.read()
f.close()
m = re.sub(u"\\bптиц(?=(\\b|(ы|у|а(х|ми?)?|е)\\b))", "рыб", f1)
k = re.sub(u"\\bПтиц(?=(\\b|(ы|у|а(х|ми?)?|е)\\b))", "Рыб", m)
m = re.sub(u"\\bПтицей\\b", "Рыбой", k)
k = re.sub(u"\\bптицей\\b", "рыбой", m)
f = open("new.html", "w", encoding = "utf(8)")
f.write(k)
f.close
