from tqdm import tqdm

char = open('char.txt', 'r').read().rstrip()
char = [c for c in char]

# def check_line(line):
#     for c in line:
#         if c in char:
#             return False
#     return True

# with open('name.txt', 'r') as f:
#     data = f.read().splitlines()

# index = open('index.txt', 'r').read().splitlines()

# with open('name_last.txt', 'w') as f_w:
#     for i in tqdm(range(len(data))):
#         if str(i) not in index:
#             f_w.write(data[i]+ '\n')


with open('name_last1.txt', 'r') as f:
    data = f.read().splitlines()

check_line = []
print(len(data))
for line in data:
    for c in line:
        if c == 'Ł':
            print(line)
            check_line.append(data.index(line))
            break

# with open ('name_last1.txt', 'w') as f_w:
#     for line in tqdm(data):
#         if data.index(line) not in check_line:
#             f_w.write(line + '\n')