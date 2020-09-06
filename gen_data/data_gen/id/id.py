import random

with open ('full_id.txt', 'w') as f:
    for i in range(300000):
        a = str(random.randint(0, 5))+ str(random.randint(0, 9))+ str(random.randint(0, 9)) + str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))
        f.write(a + '\n')