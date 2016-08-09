mat1 = mat2 = [0 for i in range(0,4)]

fin = open('A-small-practice.in','r')
fout = open('A-small-practice.out','w')
test_case = int(fin.readline())

print(test_case)

for i in range(0,test_case):
     ans1 = int(fin.readline())
     print ans1
     for j in range(0,4):
         mat1[j] = fin.readline()     
     row1 = [int(s) for s in mat1[ans1-1].split(' ')]
     print row1
     ans2 = int(fin.readline())
     print ans2
     for j in range(0,4):
         mat2[j] = fin.readline()
     row2 = [int(s) for s in mat2[ans2-1].split(' ')]        
     sol = [s for s in row1 if s in row2]
     print(row1)
     print(row2)
     print(sol)
     if(len(sol)>1):
         fout.write('Case #%d: Bad magician!\n' %(i+1))
     elif(len(sol)==1):
         fout.write("Case #%d: %d\n" %((i+1),sol[0]))
     else:
         fout.write("Case #%d: Volunteer cheated!\n" %(i+1))
         
fin.close()
fout.close()