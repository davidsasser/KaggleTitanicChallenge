import csv

# Start train file cleaning
train_file = 'data/train.csv'
with open(train_file, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    data = list(reader)

wtr = csv.writer(open ('data/titanic_train.csv', 'w'), delimiter=',', lineterminator='\n')
clean_data = []
for row in data:
    info = [None] * 7
    info[0] = row[0]
    info[1] = row[2]
    
    # male is 0
    # female is 1
    if(row[4] == 'male'):
        info[2] = 0
    elif(row[4] == 'female'):
        info[2] = 1

    info[3] = row[5]
    info[4] = row[6]
    info[5] = row[7]
    info[6] = row[1]

    clean_data.append(info)


for x in clean_data:
    if (any(i == '' for i in x)):
        continue
    wtr.writerow(x)
# end train file cleaning



# start test file cleaning
test_file = 'data/test.csv'
with open(test_file, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    data = list(reader)

wtr = csv.writer(open ('data/titanic_test.csv', 'w'), delimiter=',', lineterminator='\n')
clean_data = []
for row in data:
    info = [None] * 6
    info[0] = row[0]
    info[1] = row[1]
    
    # male is 0
    # female is 1
    if(row[3] == 'male'):
        info[2] = 0
    elif(row[3] == 'female'):
        info[2] = 1

    info[3] = row[4]
    info[4] = row[5]
    info[5] = row[6]

    clean_data.append(info)


for x in clean_data:
    if (any(i == '' for i in x)):
        for i in range(0,5):
            if(x[i] == ''):
                x[i] = 30
                print(x)
    wtr.writerow(x)
# end test file cleaning