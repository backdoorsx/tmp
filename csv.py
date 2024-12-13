from datetime import datetime

if __name__ == "__main__":

    s_timer = datetime.now()

    data = []
    with open('data1.csv','r') as f: # vsetky tm
        file = f.readlines()
        for line in file:
            line = line.replace('\n','')
            data.append(line)


    data_bez = []
    with open('bez.csv','r') as f: # bez graviru
        file = f.readlines()
        for line in file:
            line = line.replace('\n','')
            data_bez.append(line)

    print(f'Vsetky TM : {len(data)}')
    print(f'TM bez gravir : {len(data_bez)}')

    data_found = []
    for sn1 in data_bez:
        for sn2 in data:
            if sn1 in sn2:
                save_data = f'{sn1};{sn2}'
                data_found.append(save_data)

    print('data found:')
    print(len(data_found))

    data_unique = []
    for d in data_found:
        sn = d.split(';')[0]
        if sn not in data_unique:
            data_unique.append(sn)

    print('data unique:')
    print(len(data_unique))

    data_positive = []
    '''
    vyhlada unique data v najdenych
    najdene data su data aj s duplikatmi
    pri kazdom SN (unique) nastavi na zaciatku tag nema gravir
    ak najde aspon jeden gravir tak zahodi SN a ide dalej. 
    '''
    for unique in data_unique: # prejde unique data
        positive = False
        for df in data_found:
            if unique == df.split(';')[0]: # SN (UNIQUE) == SN 
                #print(f"{unique} == {df.split(';')[0]}")
                if df.split(';')[-1] != '':
                    positive = True
                    break
    
        if not positive:
            data_positive.append(unique)

    
    print('data positive:')
    print(len(data_positive))

    print(f'[*] Timer: {datetime.now() - s_timer}\n')
    
    with open('data_sorted.csv','w') as f:
        for data_line in data_positive:
            print(data_line)
            data_line = data_line + '\n'
            f.write(data_line)
            

    

    
    
