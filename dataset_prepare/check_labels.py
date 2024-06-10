with open('dataset_prepare/log (3).txt','r',encoding='utf-8') as f_in:
    data = f_in.read()
lines = data.split('\n')
fail_files = []
for line in lines:
    if len(line) < 5:
        continue
    f, c, l, d, r = line.split('|')
    if float(r) > 0.08:
        fail_files.append(f)
        # print(f)
fail_files.sort()
with open('can_be_fail.txt','w', encoding='utf-8') as f:
    f.write("\n".join(fail_files))