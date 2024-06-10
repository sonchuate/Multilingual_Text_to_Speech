with open('data/css10/train_v4.txt','r',encoding='utf-8') as f:
    data1 = f.read()
with open('data/css10/train _p3.txt','r',encoding='utf-8') as f:
    data2 = f.read()

with open('data/css10/train.txt','w',encoding='utf-8') as f:
    f.write(data1+data2)