% Simon Lee
%
% Fixed Point Recursion

close all; clear; clc;
format long

x(1) = 5;

for i = 1:29
   x(i+1) = cos(sin(x(i)));
end
disp('x_30 = ')
disp(x(30))


