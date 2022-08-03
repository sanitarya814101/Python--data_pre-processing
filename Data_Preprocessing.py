import csv

data_set_1 = []
data_set_2 = []

with open("final.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        data_set_1.append(row)

with open("archieve_dataset_sorted_1.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        data_set_2.append(row)

header1 = data_set_1[0]
planet_data1 = data_set_1[1:]

header2 = data_set_2[0]
planet_data2 = data_set_2[1:]

headers = header1 + header2

planet_data = []

for index,data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index] + planet_data2[index])

with open("merge_dataset.csv","a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planet_data)


