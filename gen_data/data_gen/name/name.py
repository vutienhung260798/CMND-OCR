import json
import random
from tqdm import tqdm

first_name = []
last_name = []
dem = []

with open('./uit_member.json', 'r') as f_r:
    data = json.load(f_r)

for member in data:
    first_name.append(member['first_name'])
    A = member['last_name'].split(' ')
    last_name.append(A[0])
    dem.extend(A[1:])

a = len(first_name)
b = len(last_name)
c = len(dem)

with open('name.txt', 'a') as f_w:
    for i in tqdm(range(200000)):
        l_n = last_name[random.randint(0, b-1)]
        # print(l_n)
        d = dem[random.randint(0, c-1)]
        # print(d)
        f_n = first_name[random.randint(0, a-1)]
        # print(f_n)
        name = l_n + ' ' + d + ' ' + f_n
        name = name.upper()
        # print(name)
        f_w.write(name + '\n')

    