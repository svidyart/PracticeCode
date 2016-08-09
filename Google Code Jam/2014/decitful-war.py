import copy 

def optimal_war(M1,N1):
    M1_sum = 0
    N1_sum = 0
    
    for jdx in range(len(M1)):
        #print(jdx,M1[jdx])
        for idx,val in enumerate(N1):
            #print(idx,val)
            if(val>M1[jdx]):
                N1_sum += 1
                N1.pop(idx)
                break
        else:
            M1_sum += 1
            N1.pop(-1)
        #print("Sum")
        #print(M1_sum, N1_sum)
    return[M1_sum, N1_sum]
    

    
def deceitful_war(M2,N2):
    M2_sum = 0
    N2_sum = 0
    jdx = 0
    #print M2
    #print N2
    while(len(M2)>0):
        #print(jdx,M2[jdx])
        for idx,val in enumerate(N2):
            #print(idx,val)
            if(M2[jdx]>val):
                M2_sum += 1
                M2.pop(0)
                N2.pop(0)
                break
        else:
            N2_sum += 1
            N2.pop(-1)
            M2.pop(0)
        #print("Sum")
        #print(M2_sum, N2_sum)
    return[M2_sum, N2_sum]        

fin = open('D-large-practice.in', 'r')
fout = open('D-large-practice.out', 'w')
T = int(fin.readline().strip())
for kdx in range(T):
    N = int(fin.readline().strip())
    M = [float(i) for i in fin.readline().split(' ')]
    N = [float(i) for i in fin.readline().split(' ')]
    #M = [0.186, 0.389, 0.907, 0.832, 0.959, 0.557, 0.300, 0.992, 0.899]
    M.sort()
    M2 = copy.deepcopy(M)
    #print M
    #N = [0.916, 0.728, 0.271, 0.520, 0.700, 0.521, 0.215, 0.341, 0.458]
    N.sort()
    N2 = copy.deepcopy(N)
    #print N
    score_deceitful = deceitful_war(M2,N2)
    score_war = optimal_war(M,N)
    fout.write('Case #%d: %d %d\n'%(kdx+1,score_deceitful[0], score_war[0]))

fin.close()
fout.close()
    #print(optimal_war(M,N))
    #print(deceitful_war(M2,N2))