data_found = []
data_found.append('1;1;g')
data_found.append('1;1;')
data_found.append('1;1;g')
data_found.append('2;2;g')
data_found.append('3;3;g')
data_found.append('3;3;g')
data_found.append('4;4;') #<<
data_found.append('5;5;') #<<
data_found.append('6;6;')
data_found.append('6;6;g')
data_found.append('6;6;')
data_found.append('7;7;') #<<
data_found.append('8;8;g')
data_found.append('8;8;')
data_found.append('9;9;')
data_found.append('9;9;g')

data_unique = []
for d in data_found:
    sn = d.split(';')[0]
    if sn not in data_unique:
        data_unique.append(sn)

for i in data_unique:
    print(i)
    
print('------')

data_positive = []
for unique in data_unique:
    positive = False
    for df in data_found:
        if unique == df.split(';')[0]:
            print(f"{unique} == {df.split(';')[0]}")
            if df.split(';')[-1] != '':
                print('break')
                positive = True
                break
    
    if not positive:
        data_positive.append(unique)

print('------')
for i in data_positive:
    print(i)
