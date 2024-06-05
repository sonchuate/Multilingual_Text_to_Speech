import os
# with open('vin_bigdata/labels (1).txt','r',encoding='utf8') as f:
#     data = f.read()

DATA_FOLDER = 'E:/src code 2/python 2/vdt/data/wavs_2'
idx = 2404


allData = {}

for file in  os.listdir(DATA_FOLDER):
    if '.txt' in file:
        folder_name = file.split('.')[0]
        allData[folder_name] = []
        with open(os.path.join(DATA_FOLDER, file), 'r', encoding='utf-8') as f:
            data = f.read()
            allData[folder_name] = data


alphabet = set(list("abcdefghijklmnopqrstuvwxyzàáâãèéêìíòóôõùúýăđĩũơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ"))
with open(f'vin_bigdata/val_{DATA_FOLDER.split("/")[-1]}.txt','w',encoding='utf-8') as f_val:
    with open(f'vin_bigdata/train_{DATA_FOLDER.split("/")[-1]}.txt','w',encoding='utf-8') as f_train:
        for folder_name, data in allData.items():
            for l in data.split('\n'):
                if len(l) < 3: continue
                name_file, content = l.split('\t')
                if len(content.split(' ')) > 35:
                    continue
                #id file| id speaker | id language | file name ||| content|
                if idx < 54000:
                    
                    f_train.write(f'{idx:06d}|vietnamese-00|vietnamese|data/{DATA_FOLDER.split("/")[-1]}/{folder_name}/{name_file.replace("/content","")}|||{content}|\n')     
                else:
                    f_val.write(f'{idx:06d}|vietnamese-00|vietnamese|data/{DATA_FOLDER.split("/")[-1]}/{folder_name}/{name_file.replace("/content","")}|||{content}|\n') 
                idx += 1
                alphabet.update(list(content))

with open('vin_bigdata/alphabet.txt','w',encoding='utf-8') as f:
    f.write(''.join(sorted(list(alphabet))))

print(idx)
#  '<>abcdefghijklmnopqrstuvwxyzàáâãèéêìíòóôõùúýăđĩũơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ