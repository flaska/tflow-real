import csv
all_data = []
all_labels = []

string_data = []
with open('insurance.csv', 'rt') as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in reader:
         string_data.append(row)

string_data = string_data[1:]

for row in string_data:
    new_row = [
        float(row[0]),
        float(row[2])
    ]
    all_data.append(new_row)

for row in string_data:
    new_row = [
        float(row[6])
    ]
    all_labels.append(new_row)

train_data = all_data[:1000]
train_labels = all_labels[:1000]

test_data = all_data[1000:]
test_labels = all_labels[1000:]

def get_data():
    return (train_data, train_labels), (test_data, test_labels)