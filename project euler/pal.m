function p = pal(n)
    s = num2str(n);
    l = length(s);
    rs = s(l:-1:1);
    if(s==rs)
        p = 1;
    else
        p = 0;
    end
end
        
    