name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From '):
        line = line.rstrip()
        pieces = line.split()
        #print(pieces) checking results
        # getting just the time section
        time = pieces[5]
        #print(time)
        # Picking just the hours out
        split_time = time.split(':')
        #print(split_time)
        hours = split_time[0]
        #print(hours)
        counts[hours] = counts.get(hours, 0) + 1

x = sorted(counts.items())

for a, b in x:
    print(a + ' ' + str(b))

