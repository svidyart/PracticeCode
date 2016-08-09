% Problem 1: If we list all the natural numbers below 10 that are multiples
% of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.Find 
% the sum of all the multiples of 3 or 5 below 1000.

clear all
clc
num = 1:999;
ind = or((mod(num,3)==0),(mod(num,5)==0));
sum35 = sum(num.*ind);