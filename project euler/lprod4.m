function [tmp_i,tmp_j,lar] = lprod4(mat,lar,tmp_i,tmp_j) 
for i = 1:20
    for j = 1:17
        tmp = prod(mat(i,j:j+3));
        if(tmp>lar)
            lar = tmp;
            tmp_i = i;
            tmp_j = j;
        end
    end
end
fprintf('i is %d \n',tmp_i);
fprintf('j is %d \n',tmp_j);
fprintf('%d ',mat(tmp_i,tmp_j:tmp_j+3));
fprintf('\nProd is %ld \n',lar);
end