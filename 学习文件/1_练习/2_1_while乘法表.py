i = 1
while i <= 9:
    txt = ''
    u = 1
    while u <= i:
        txt += f'{u}*{i}={u * i}\t'
        u += 1
    print(txt)
    i += 1
