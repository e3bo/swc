import sys

source = file(sys.argv[1], 'r')
source.readline()
count_sum = 0
for line in source:
    date, breed, count = line.split(',')
    count_sum = count_sum + int(count) 
source.close()
print count_sum

