import random

def passwordmanagment(n):

    d = [str(x) for x in range(10)]
    lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                        'z'] 
    uc = [x.upper() for x in (lc)]
    s = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
            '*', '(', ')', '<&# 039;']

    k = d + lc + uc + s
    Pass = random.choice(d) + random.choice(lc) + random.choice(uc) + random.choice(s)

    while len(Pass) < 12:
        Pass += random.choice(k)
    b = str(n) +  '    ' + str(Pass)

    f = open("database.txt", "a")
    f.write('\n')
    f.write(b)
    f.close()

    print(b)

a = input()
passwordmanagment(a)