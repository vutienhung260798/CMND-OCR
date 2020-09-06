with open ('./all_full_name.txt', 'r') as f:
    data = f.read().splitlines()

with open ('./name.txt', 'w') as f_w:

    for line in data:
        line = line.upper()
        f_w.write(line + '\n')