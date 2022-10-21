% calculates roots program
%
% Simon Lee

close all; clear; clc;

%constant variables
tol = 10e-4; 
x_axis = linspace(-1,1);

% build function - computed function with hand for p4
p4 = func()

root1 = bisection(-1, -0.8, p4, tol)
root2 = bisection(-0.5, -0.3, p4, tol)
root3 = bisection(0.8, 1, p4, tol)
root4 = bisection(0.3, 0.5, p4, tol)

figure(1)
plot(x_axis, p4(x_axis));
% professors label code
xlabel('$x$','Interpreter','latex'); 
ylabel('$y$','Interpreter','latex','rotation',0);









