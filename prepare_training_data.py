with open('vin_bigdata/labels (1).txt','r',encoding='utf8') as f:
    data = f.read()
alphabet = set()
idx = 0
with open('vin_bigdata/train.txt','w',encoding='utf-8') as f:
    for l in data.split('\n'):
        if len(l) < 3: continue
        name_file, content = l.split('\t')
        f.write(f'{idx:05d}|vietnamese|vietnamese|{name_file}|||{content}|\n')
        idx += 1
        alphabet.update(list(content))
with open('vin_bigdata/alphabet.txt','w',encoding='utf-8') as f:
    f.write(''.join(sorted(list(alphabet))))

    
