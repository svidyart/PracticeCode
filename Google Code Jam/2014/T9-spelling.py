fin = open('t9-spelling-large.in','r')
fout = open('t9-spelling-large.out','w')

T = int(fin.readline())
apl = {' ':0, 'a':2, 'd':3, 'g':4, 'j':5, 'm':6, 'p':7, 't':8, 'w':9, 'b':22, 'e':33, 'h':44, 'k':55, 'n':66, 'q':77, 'u':88, 'x':99, 'c':222, 'f':333, 'i':444, 'l':555, 'o':666, 'r':777, 'v':888, 'y':999, 's':7777, 'z':9999}

for i in range(T):
    sol=' '
    st = fin.readline().strip('\n')
    for k in st:
        if(sol[-1]==(str(apl[k]))[0]):
            sol = sol + ' ' + str(apl[k])
        else:
            sol = sol + str(apl[k])
    fout.write('Case #' + str(i+1) +': ' + sol.strip() + '\n')
    
fin.close()
fout.close()    
    