with open ('./dmy.txt', 'a') as f:
    for y in range(1950, 2200):
        y = str(y)
        for m in range(1, 13):
            if m < 10:
                m  = '0' + str(m)
            else:
                m = str(m)
            for d in range(1, 32):
                if d < 10:
                    d = '0' + str(d)
                else:
                    d = str(d)
                f.write(y + '\n' + m + '-' + y + '\n' + d + '-'+ m + '-'+ y + '\n')
