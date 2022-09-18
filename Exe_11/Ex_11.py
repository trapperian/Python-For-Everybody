import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum.txt"
handle = open(name)

digits = list()
for line in handle:
    x = re.findall("[0-9]+", line)
    if len(x) < 1:
        continue
    else:
        for i in x:
            digits.append(int(i))
total = 0
for d in digits:
    total += d
print(total)
