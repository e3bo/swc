import sys

def count_birds(reader):
    source.readline() #First line is header, so ignore
    total = 0
    for line in reader:
        date, breed, count = line.split(',')
        total += int(count) 
    return total

grand_total = 0
for filename in sys.argv[1:]:
    source = open(filename, 'r')
    total = count_birds(source)    
    grand_total += total
    source.close()
    print total, filename

    source.close()

print grand_total, 'total'
