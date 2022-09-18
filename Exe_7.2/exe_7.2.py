# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    dec = line.find('.')
    extract = line[dec-1:].strip()
    num = float(extract)
    total += num


print("Average spam confidence: " + str(total/count))
