fin = open('B-large-practice.in','r')
fout = open('B-large-practice.out','w')

test_case = int(fin.readline())

for i in range(test_case):
    t = 0.
    [c,f,x] = [float(a) for a in fin.readline().split(' ')]
    n = max(int(((x*f) - (2*c))/(c*f)),0)
    #print n
    for j in range(0,n):
        t = t + (c/((j*f) + 2.0))
        #print t
    t = t + ((x)/(n*f + 2.0))
    fout.write("Case #%d: %.7f\n" %((i+1),t))
    
fin.close()
fout.close()