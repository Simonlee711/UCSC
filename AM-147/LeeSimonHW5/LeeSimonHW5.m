% Simon Lee
%
% Guess Irrational function

close all; clear; clc;

% intialize Matrix A and vector b
A = [1,1,1,-2,-2;1,2,4,-10,-20;1,3,9,-27,-81;1,4,16,4,16;1,5,25,20,100];
b = [2;5;9;-1;-4];

% find the solutions
x = A\b
%x(4,1)

% prepare to plot
t = linspace(-6,6,600);
f=@(t) (x(1,1)+x(2,1)*t+x(3,1)*t.^2)./(1+ x(4,1)*t + x(5,1)*t.^2);

% Plot
figure(1)
plot(t,f(t));
xlabel('t', 'Fontsize', 12);
ylabel('f(t)', 'Fontsize', 12);
title('f(t) vs. t');