import csv
with open('eggs.csv', 'w', newline = '') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter = ' ', 
                            quotechar ='|', quoting = csv.QUOTE_MINIMAL)
    spamwriter.writerow(['spam'] * 5 + ['Baked beans'])
    spamwriter.writerow(['spam', 'Lovely spam', 'Wonderful Spam'])
    
    

with open('eggs.csv', newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ' ', quotechar ='|')
    for row in spamreader:
        print(", ".join(row))