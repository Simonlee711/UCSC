% Simon Lee - AM 147 Winter 2022
%
% Estimating sinc(5)

close all; clear; clc;

% true value
tv = sin(5)/5;

% intialize sum & prod variable
Sum = 0.0;
total = 1.0; % you can't multiply the product by 0

% summation
for n = 0:6
    Sum = Sum + ((-1)^n * 5^(2*n))/(factorial(2*n+1));
end

%product
for m = 1:7
    total = total * cos(5/(2^m));
end

% print statements
msg1 = ['sin(5)/5 = ', num2str(round(tv,4))];
msg2 = ['summation = ', num2str(round(Sum,4))];
msg3 = ['product = ',num2str(round(total,4))];
disp(msg1)
disp(msg2)
disp(msg3)

% calculate relative error
re1 = abs(tv - Sum)/abs(tv);
re2 = abs(tv - total)/abs(tv);
msg4 = ['relative error (i) = ',num2str(round(re1,4))];
msg5 = ['relative error (ii) = ',num2str(round(re2,4))];
disp(msg4)
disp(msg5)

