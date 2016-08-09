class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if(not numRows):
            return []
        pt = []
        for i in range(numRows):
            if(i == 0):
                pt.append([1])
            elif(i == 1):
                pt.append([1,1])
            else:
                #temp = [1]
                #for j in range(i-1):
                #    temp.append(pt[i-1][j]+pt[i-1][j+1])
                temp = [pt[i-1][j]+pt[i-1][j+1] for j in range(i-1)]
                temp.insert(0,1)
                temp.append(1)
                pt.append(temp)
        return pt