import sys
grand_total = 0

for filename in sys.argv[1:]:
    source = open(filename, 'r')

    source.readline()
    total = 0
    for line in source:
        date, breed, count = line.split(',')
        total += int(count) 

    grand_total += total
    source.close()
    print total, filename

    source.close()

print grand_total, 'total'
