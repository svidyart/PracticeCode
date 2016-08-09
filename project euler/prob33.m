for i = 1:9
    for j = 1:9
        for k = 1:9
            if(((9*i*j + j*k)/(10*k))==i)
                fprintf('%d,%d,%d\n',i,j,k)
            end
        end
    end
end