from os import listdir as l
l = l(".")
l.remove("count.py")
for file in l:
 print(file, end=" - ")
 with open(file) as f:
  a = f.read()
  print(len(a))