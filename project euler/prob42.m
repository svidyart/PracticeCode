clear all
clc
data = {}
su(1:50) = 0;
for i = 1:50
    su(i) = i*(i+1)/2;
end

for i = 1:length(data)
    asciieq(i,1) = (sum(double(data{i})))-(64*length(data{i}));
end


num = sum(ismember(asciieq,su));
