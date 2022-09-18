name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if not line.startswith("From:"):
        continue
    pieces = line.split()
    email = pieces[1]
    if email not in counts:
        counts[email] = 1
    else:
        counts[email] += 1

mostcount = None
mostemail = None
for email, count in counts.items():
    if mostcount is None or count > mostcount:
        mostemail = email
        mostcount = count
print(mostemail, mostcount)

