tmp = 0;
lar = 0;
for i = 100:1:999
    for j = 100:1:999
        if(pal(i*j)==1)
            tmp = i*j;
        end
        if(tmp>lar)
            lar = tmp;
        end
    end
end
fprintf('%d\n',lar)