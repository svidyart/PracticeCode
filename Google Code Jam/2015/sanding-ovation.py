
fin = open('A-smal.in','r')
fout = open('A-small.out','w')

T = int(fin.readline())
print T
for idx in range(T):
    m = 0
    [s_max, si_str] = fin.readline().split(' ')
    si = [int(i) for i in si_str.strip('\n')]
    s = si[0]
    s_max_int = int(s_max)
    print(s_max_int)
    if(s_max_int == 0):
        fout.write("Case #%d: 0\n" %(idx+1))
    else:
        for jdx in range(s_max_int+1):
            if(jdx>sum(si[:jdx])):
                m = m + jdx - s
            print(jdx, s, m)    
            s = m + sum(si[:jdx+1])
            if (s > s_max_int):
                break
        fout.write("Case #%d: %s %d\n" %(idx+1, si_str, m))
        
fin.close()
fout.close()    
        