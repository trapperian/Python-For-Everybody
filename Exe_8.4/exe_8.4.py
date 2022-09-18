fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    splitline = line.rstrip().split()
    for i in splitline:
        if i not in lst:
            lst.append(i)

lst.sort()
print(lst)

