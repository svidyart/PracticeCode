% Problem 53

% There are exactly ten ways of selecting three from five, 12345: 
% 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
% 
% In combinatorics, we use the notation, 5C3 = 10.
% 
% It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
% 
% How many, not necessarily distinct, values of  nCr, for 1 ? n ? 100, are greater than one-million?

% Solution: In an nCr

y = [0.1353 0.6065 1.0000 0.6065 0.1353];
yup = zeros(1,2*length(y));
yup(1:2:end) = y; 
figure
subplot(2,1,1)
stem(y)
xlabel('----> n')
ylabel('----> y')
subplot(2,1,2)
stem(yup)
xlabel('----> n')
ylabel('----> yup')
f_y = fftshift(fft(y));
f_yup = fftshift(fft(yup));
figure
subplot(2,1,1)
stem(abs(f_y),'r')
xlabel('----> fs')
ylabel('----> Y')
subplot(2,1,2)
stem(abs(f_yup),'r')
xlabel('----> fs')
ylabel('----> YUP')
f_ylp = [f_yup(1:3), 0 0 0 0 0 f_yup(9:10)];
figure
subplot(2,1,1)
stem(abs(f_ylp),'r')
xlabel('----> fs')
ylabel('----> YLP')
ylp = ifft(f_ylp);
ylp2 = 2*ylp;
subplot(2,1,2)
stem(ylp2);
xlabel('----> n')
ylabel('----> ylp2')