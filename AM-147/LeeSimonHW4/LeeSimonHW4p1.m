% Simon Lee
%
% Newtons Method

close all; clear; clc;
format long

% equation 3^(1/5) can be rewritten as x^5 = 3
y=@(x)(x.^100) - 2022;
dy=@(x)100*(x.^99);

% intial guess
x = 1;

% Newtons Method
for i = 1:1
    x = x - y(x)/dy(x);
    
end

x_1 = x

%part b of part 1

num = (x_6 - 1);
denom = (x_6 + 1);
x_approx = num/denom;

% graph
f=@(x) 2*(x.^5)-5*(x.^4)+20*(x.^3) - 10*(x.^2) + 10*x - 1
x_axis = linspace(0,1);

figure(1)
plot(x_axis, f(x_axis))
hold on 
plot(x_approx, 0, 'ro', 'LineWidth', 2, 'MarkerSize', 10)
hold off



