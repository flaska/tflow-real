import csv
import numpy as np

all_data = []
all_labels = []

string_data = []
with open('data.csv', 'rt') as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in reader:
         string_data.append(row)

string_data = string_data[1:]

for row in string_data:
    new_row = [
        float(row[46]), #AU GrLivArea - square footage
        float(row[81]) #CD Age
    ]
    all_data.append(new_row)

for row in string_data:
    new_row = [
        float(row[80]) #CC SalePrice
    ]
    all_labels.append(new_row)

train_data_orig = all_data[:1000]
train_labels = np.array(all_labels[:1000])

test_data_orig = all_data[1000:]
test_labels = np.array(all_labels[1000:])

train_data_orig = np.array(train_data_orig)
test_data_orig = np.array(test_data_orig)

mean = train_data_orig.mean(axis=0)
std = train_data_orig.std(axis=0)

print("mean1: {}".format(mean[0]))
print("mean2: {}".format(mean[1]))
print("std1: {}".format(std[0]))
print("std2: {}".format(std[1]))

train_data = (train_data_orig - mean) / std
test_data = (test_data_orig - mean) / std

def get_data():
    return (train_data, train_labels), (test_data, test_labels)