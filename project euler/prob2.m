% Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
% By starting with 1 and 2, the first 10 terms will be:
% 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
% By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
% find the sum of the even-valued terms.

clear all
clc

fib = [1,2];
n = 3;
res = 3;

while(res<4000000) 
    fib(n) = res;
    n = n + 1;
    res = fib(n-2) + fib(n-1);
end

fibo_sum = sum(fib(find(mod(fib,2)==0)));