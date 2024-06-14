with open('data/css10/train.txt','r',encoding='utf-8') as f:
    data = f.read()
    lines = data.split('\n')
    for line in lines:
        if len(line.split('|')) != 8:
            print(line)