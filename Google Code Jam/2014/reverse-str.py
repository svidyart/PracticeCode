def rev_str(st):
    return st[::-1]


fin = open('reverse-word-large.in','r')
fout = open('reverse-word-large.out','w')

T = int(fin.readline())

for i in range(T):
    st = fin.readline().strip()
    st = rev_str(st)
    sol = [rev_str(j) for j in st.split(' ')]
    
    fout.write('Case #' + str(i+1) + ': ' + ' '.join(sol)+'\n')
    
fin.close()
fout.close()
        
