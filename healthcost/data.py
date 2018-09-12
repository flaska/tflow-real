import csv
result = []
with open('insurance.csv', 'rt') as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in reader:
        result.append(row)

def get_data():
    return result[1:]