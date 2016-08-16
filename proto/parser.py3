f = open('txnlog.dat', 'r')  # We need to re-open the file
data = f.read()
for line in data:
    print(line),
f.close()