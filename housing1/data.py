import csv
import data_conv
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
        float(row[46]), # AU: GrLivArea - square footage
        float(row[1]),  # B: MSSubClass
        float(row[4]),  # E: LotArea
        float(data_conv.neighborhood(row[12])),  # M: Neighborhood
        float(data_conv.housestyle(row[16])),  # Q: Housestyle
        float(row[20]),  # U: YearRemodAdd - year remodeled
        float(row[26] if row[26]!="NA" else 0),  # U: MasVnrArea
        float(row[38]),  # AM: TotalBsmtSF

        float(data_conv.heating(row[40])),  # AO: HeatingQC
        float(data_conv.ac(row[41])),  # AP: CentralAi

        float(row[54]),  # BC: TotRmsAbvGrd
        float(row[56]),  # BE: Fireplaces

        float(row[61]),  # BJ: GarageCars
        float(row[62]),  # BK: GarageArea

        float(row[66]),  # B0: WoodDeckSF
        float(row[67]),  # BP: OpenPorchSF
        float(row[68]),  # BQ: EnclosedPorch

        float(row[81])  # CD: Age
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