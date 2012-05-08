
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--breed", help="One breed to select for counting")
parser.add_argument("files", help="The names of the data files", nargs='+')
args = parser.parse_args()

def count_birds(reader, selected):
    source.readline() #First line is header, so ignore
    total = 0
    for line in reader:
        date, breed, count = line.split(',')
        if selected == None or selected == breed:
            total += int(count) 
    
    return total

grand_total = 0
for filename in args.files:
    source = open(filename, 'r')
    total = count_birds(source, args.breed)    
    grand_total += total
    source.close()
    print total, filename

    source.close()

print grand_total, 'total'
